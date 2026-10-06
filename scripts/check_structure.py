"""Check the architecture without a TeX installation (Python standard library)."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []


def require(condition, message):
    if not condition:
        errors.append(message)


def uncomment(text):
    return "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0]
                     for line in text.splitlines())


tex_files = sorted(ROOT.rglob("*.tex"))
tex_files = [p for p in tex_files if "build" not in p.relative_to(ROOT).parts]
texts = {p: uncomment(p.read_text(encoding="utf-8")) for p in tex_files}
main = texts[ROOT / "main.tex"]
includes = re.findall(r"\\include\{([^}]+)\}", main)
chapter_paths = sorted((ROOT / "chapters").glob("*.tex"))
appendix_paths = sorted((ROOT / "appendices").glob("*.tex"))
require(len(chapter_paths) == 27, "Expected 27 chapter files")
require(len(appendix_paths) == 6, "Expected six appendix files")
require(len(includes) == 33 and len(set(includes)) == 33,
        "Each chapter/appendix must be included exactly once")
expected = {p.relative_to(ROOT).with_suffix("").as_posix()
            for p in chapter_paths + appendix_paths}
require(set(includes) == expected, "Main inclusion list differs from source files")

labels = {}
refs = []
for path, text in texts.items():
    relative = path.relative_to(ROOT)
    # Input paths in this project are deliberately relative to the root.
    for target in re.findall(r"\\(?:input|include)\{([^}]+)\}", text):
        require((ROOT / (target if target.endswith(".tex") else target + ".tex")).is_file(),
                f"{relative}: missing input {target}")
    depth = 0
    for token in re.finditer(r"(?<!\\)[{}]", text):
        depth += 1 if token.group() == "{" else -1
        require(depth >= 0, f"{relative}: premature closing brace")
    require(depth == 0, f"{relative}: unbalanced braces")
    # The solution macro deliberately opens/closes a group in separate arguments;
    # this check is lexical and is not a TeX parser.
    for label in re.findall(r"\\label\{([^}]+)\}", text):
        require(label not in labels, f"Duplicate label: {label}")
        labels[label] = relative
    for group in re.findall(r"\\(?:[cC]ref|ref|eqref)\{([^}]+)\}", text):
        refs.extend((relative, key.strip()) for key in group.split(",")
                    if "#" not in key)
    envs = []
    for action, name in re.findall(r"\\(begin|end)\{([^}]+)\}", text):
        if action == "begin":
            envs.append(name)
        else:
            require(bool(envs) and envs[-1] == name,
                    f"{relative}: mismatched environment {name}")
            if envs:
                envs.pop()
    require(not envs, f"{relative}: unclosed environments {envs}")

for path, key in refs:
    require(key in labels, f"{path}: unresolved reference {key}")
for path in chapter_paths + appendix_paths:
    source = path.read_text(encoding="utf-8")
    require(source.startswith("% Scope:"), f"{path.name}: missing scope comment")
    require(len(re.findall(r"\\chapter\{", texts[path])) == 1,
            f"{path.name}: expected exactly one chapter")
    require(r"\subsection{" in texts[path], f"{path.name}: missing subsections")
for path in chapter_paths:
    text = texts[path]
    require(r"\section{Challenge problems}" in text,
            f"{path.name}: missing challenge section")
    require(r"\section{Worked examples}" in text,
            f"{path.name}: missing worked examples section")
    source = path.read_text(encoding="utf-8")
    for field in ("Prerequisites:", "Planned figures:", "Planned challenge problems:"):
        require(field in source, f"{path.name}: missing {field}")

bib = (ROOT / "bibliography/references.bib").read_text(encoding="utf-8")
keys = re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib)
require(len(keys) == len(set(keys)), "Duplicate bibliography keys")
for text in texts.values():
    for group in re.findall(r"\\(?:cite|textcite|parencite|nocite)\{([^}]+)\}", text):
        for key in group.split(","):
            require(key == "*" or key.strip() in keys, f"Missing citation: {key}")
require(r"\setcounter{tocdepth}{2}" in texts[ROOT / "preamble/styles.tex"],
        "Contents must include subsections")
require(includes[-1] == "appendices/F_cheatsheet",
        "Reference sheet must remain last")
require(r"\author" not in main, "Cover must have no author command")
if errors:
    print("\n".join("ERROR: " + error for error in errors))
    sys.exit(1)
sections = sum(len(re.findall(r"\\section\{", texts[p])) for p in chapter_paths)
subsections = sum(len(re.findall(r"\\subsection\{", texts[p])) for p in chapter_paths)
print(f"PASS: 27 chapters, 6 appendices, {sections} chapter sections, "
      f"{subsections} chapter subsections, {len(labels)} labels, {len(keys)} references.")
print("Static checks passed; TeX compilation is a separate required check when available.")

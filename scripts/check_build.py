"""Reject unresolved references/citations and TeX errors after latexmk."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
build = root / "build"
log_path = build / "main.log"
if not log_path.exists() or not (build / "main.pdf").exists():
    sys.exit("Missing build/main.log or build/main.pdf; compile first.")
log = log_path.read_text(encoding="utf-8", errors="replace")
patterns = [
    r"^! ", r"LaTeX Error:", r"Undefined control sequence",
    r"(?:Reference|Citation) .* undefined",
    r"There were undefined references",
    r"multiply[- ]defined", r"Please \(re\)run Biber",
    r"Rerun to get cross-references right",
]
failures = [p for p in patterns if re.search(p, log, re.MULTILINE)]
blg = build / "main.blg"
if not blg.exists():
    failures.append("Biber log missing")
elif re.search(r"\bERROR\b", blg.read_text(encoding="utf-8", errors="replace")):
    failures.append("Biber reported an error")
if failures:
    sys.exit("Build diagnostics failed: " + ", ".join(failures))
boxes = re.findall(r"Overfull \\[hv]box[^\n]*", log)
if boxes:
    print("Layout review needed:\n" + "\n".join(boxes))
    sys.exit(1)
print("PASS: PDF exists; no unresolved references/citations, Biber errors or overfull boxes.")

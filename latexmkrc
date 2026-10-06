# Run latexmk from the repository root.
$pdf_mode = 1;
$out_dir = 'build';
$pdflatex = 'pdflatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$max_repeat = 6;
# latexmk detects biblatex/biber and makeindex from generated auxiliary files.

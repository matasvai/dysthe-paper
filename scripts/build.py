"""Compile the manuscript using an installed LaTeX engine."""
import argparse
from pathlib import Path
import shutil
import subprocess
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--engine',help='Path to tectonic or pdflatex')
args=parser.parse_args()
engine=args.engine or shutil.which('tectonic') or shutil.which('pdflatex')
if not engine:
    parser.exit(2,'Install Tectonic or pdfLaTeX, or pass --engine /path/to/tectonic.\n')
output=ROOT/'output/pdf'
output.mkdir(parents=True,exist_ok=True)
if 'tectonic' in Path(engine).name:
    subprocess.run([engine,'--keep-logs','--outdir',str(output),'main.tex'],cwd=ROOT/'manuscript',check=True)
else:
    for _ in range(2):
        subprocess.run([engine,'-interaction=nonstopmode','-halt-on-error',f'-output-directory={output}','main.tex'],cwd=ROOT/'manuscript',check=True)
print(output/'main.pdf')

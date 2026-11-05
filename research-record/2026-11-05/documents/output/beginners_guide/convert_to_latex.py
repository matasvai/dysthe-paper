from pathlib import Path
import re
P=Path(__file__).resolve().parent
text=(P/'guide.md').read_text()
def esc(s):
 s=s.replace('\\','\\textbackslash{}')
 for a,b in [('&',r'\&'),('%',r'\%'),('_',r'\_'),('#',r'\#')]:s=s.replace(a,b)
 return s
out=[r'''\documentclass[10pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{graphicx}
\title{Reading the Wave Pictures}
\author{}
\date{}
\begin{document}
\maketitle
''']
for block in text.strip().split('\n\n'):
 if block=='# Reading the wave pictures':continue
 if block.startswith('# '):out.append('\\section{'+esc(re.sub(r'^\d+\.\s*','',block[2:]))+'}\n')
 elif block=='## The picture in one sentence':out.append('\\section{What the picture represents}\n')
 elif block.startswith('## '):out.append('\\subsection{'+esc(block[3:])+'}\n')
 elif block.startswith('Illustration, not simulation data.') or block.startswith('Illustration of the two display rules.'):
  name='envelope_and_phase.png' if block.startswith('Illustration,') else 'normalization.png'
  out.append('\\begin{figure}[htbp]\n\\centering\n\\includegraphics[width=\\linewidth]{'+name+'}\n\\caption{'+esc(block)+'}\n\\end{figure}\n')
 else:out.append(esc(block)+'\n')
out.append('\\end{document}\n');(P/'guide.tex').write_text('\n'.join(out))

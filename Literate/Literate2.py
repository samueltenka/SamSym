definitions = {}; documentation = []
DEF_BEG, DEF_END, EXP_BEG, EXP_END = '<'*3, '>'*3, '<'+'@', '@'+'>'
START_MACRO = 'START'; MAKE_FILE_NAME = 'make.txt'
filenames = []
with open(MAKE_FILE_NAME) as file:
   filenames = file.read().split('\n')
out, ins, doc = filenames[0], filenames[1:-1], filenames[-1]
for filename in ins:
   with open(filename) as file:
      text = file.read()
      while '\n\n\n' in text:
          text = text.replace('\n\n\n', '\n\n')
      sections = text.split('\n\n')
      for section in sections:
         lines = section.split('\n')
         strp = lines[0].strip()
         if len(strp)>=6 and strp[:3]==DEF_BEG and strp[-3:]==DEF_END:
            name = strp[3:-3].strip()
            if name in definitions:
               print('may not redefine macro', name)
               exit(-1)
            definitions[name]='\n'.join(lines[1:])
            d_insert = documentation
            while d_insert and isinstance(d_insert[-1], list):
               d_insert = d_insert[-1]
            d_insert.append(('CODE', name))
         if len(strp)>=5:
            if strp[:5]=='=====':
               documentation = [lines[1], lines[3:]] ## top heading
            elif strp[:5]=='-----':
               documentation.append([lines[1], lines[3:]]) ## section
            elif strp[:5]=='_____':
               documentation[-1].append([lines[1], lines[2:]]) ## subsection
         d_insert = documentation
         while d_insert and isinstance(d_insert[-1], list):
            d_insert = d_insert[-1]
         d_insert.append('\n' + ''.join(lines[3:]))
with open(out, 'w') as f:
   text = definitions[START_MACRO]
   while EXP_BEG in text:
      lines = text.split('\n')
      text = ''
      for line in lines:
         if EXP_BEG in line:
            spacing = line[:len(line)-len(line.lstrip())]
            name = line.replace(EXP_BEG, '').replace(EXP_END, '').strip()
            if name not in definitions:
               print('macro not found:', name)
               exit(-1)
            for defline in definitions[name].split('\n'):
               text += spacing + defline + '\n'
         else:
             text += line+'\n'
   f.write(text)

tex_begin = '\\documentclass{article} \\usepackage{amsmath} \\begin{document}'
tex_end =   '\\end{document}'
tex_title = '\\title{'+documentation[0]+'} \\maketitle' if isinstance(documentation[0], str) else ''
tex_body = ''
def translate(body):
  if isinstance(body, str):
     return body
  elif isinstance(body, tuple) and body[0]=='CODE':
     return '\\begin{verbatim}'+\
            definitions[body[1]]+\
            '\\end{verbatim}'
for section in documentation[1:]:
  if isinstance(section, list):
     tex_body += '\\section{'+section[0]+'}'
     for subsect in section[1:]:
        if isinstance(section, list):
           tex_body += '\\subsection{'+subsect[0]+'}'
           for subsubsect in subsect[1:]:
              tex_body += translate(subsubsect)
        else:
            tex_body += translate(subsect)
  else:
     tex_body += translate(section)
tex = tex_begin+tex_title+tex_body+tex_end
with open(doc, 'w') as f:
   f.write(tex)





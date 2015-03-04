definitions = {}; tex_body = ''
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
            tex_body += '\\'+'begin{verbatim}\n'+\
                        definitions[name]+'\n'+\
                        '\\'+'end{verbatim}\n'
         elif strp[:5] in ['=====','-----','_____']:
            if strp[:5]=='=====':
                tex_body += '\\'+'title{'+lines[1]+'}\n' +\
                            '\\'+'maketitle\n'
            elif strp[:5]=='-----':
                tex_body += '\\'+'section{'+lines[1]+'}\n'
            elif strp[:5]=='_____':
                tex_body += '\\'+'subsection{'+lines[1]+'}\n'
            lines = lines[3:]
            tex_body += '\n'.join(lines)+'\n\n'
         else:
            tex_body += '\n'.join(lines)+'\n\n'
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
with open(out, 'w') as f:
   f.write(text)
tex_begin = '\\'+'documentclass{article}'+\
            '\\'+'usepackage{amsmath}'+\
            '\\'+'begin{document}\n'
tex_end =   '\\'+'end{document}'
tex = tex_begin+tex_body+tex_end
with open(doc, 'w') as f:
   f.write(tex)




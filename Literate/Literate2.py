definitions = {}; tex_body = ''
DEF_BEG, DEF_END, EXP_BEG, EXP_END = '<'*3, '>'*3, '<'+'@', '@'+'>'
START_MACRO='START'; MAKE_FILENAME='make.txt'; SNIPPETS_FILENAME='snippets.tex'
filenames = []
with open(MAKE_FILENAME) as file:
   filenames = file.read().split('\n')
out, ins, doc = filenames[0], filenames[1:-1], filenames[-1]
with open(SNIPPETS_FILENAME, 'r') as f:
   DOC_SNIPPET, \
   TITLE_SNIPPET, SECTION_SNIPPET, SUBSECTION_SNIPPET, \
   REGULAR_SNIPPET, EXPANDABLE_SNIPPET = f.read().split('\n\n')
for filename in ins:
   with open(filename) as file:
      text = file.read()
      text = '\n'.join((line if line.strip() else '') for line in text.split('\n'))
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
            is_expandable = lambda line: EXP_BEG in line
            lines = definitions[name].split('\n')
            while lines:
               if lines and not is_expandable(lines[0]):
                  code = ''
                  while lines and not is_expandable(lines[0]):
                      code += lines[0]+'\n'
                      lines = lines[1:]
                  tex_body += REGULAR_SNIPPET.replace('REGULAR CODE', code)
               if lines and is_expandable(lines[0]):
                  code = ''
                  while lines and is_expandable(lines[0]):
                      code += lines[0]+'\n'
                      lines = lines[1:]
                  tex_body += EXPANDABLE_SNIPPET.replace('EXPANDABLE', code)
         elif strp[:5] in ['=====','-----','_____']:
            if strp[:5]=='=====':
                tex_body += TITLE_SNIPPET.replace('TITLE', lines[1])
            elif strp[:5]=='-----':
                tex_body += SECTION_SNIPPET.replace('S HEADING', lines[1])
            elif strp[:5]=='_____':
                tex_body += SUBSECTION_SNIPPET.replace('SS HEADING', lines[1])
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
tex = DOC_SNIPPET.replace('BODY', tex_body)
with open(doc, 'w') as f:
   f.write(tex)





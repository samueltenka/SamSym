definitions = {}
DEF_START, DEF_END, EXP_START, EXP_END = '<'*3, '>'*3, '<'+'@', '@'+'>'
START_MACRO = 'START'; MAKE_FILE_NAME = 'make.txt'
filenames = []
with open(MAKE_FILE_NAME) as file:
   filenames = file.read().split('\n')
out, ins = filenames[0], filenames[1:]
for filename in ins:
   with open(filename) as file:
      text = file.read()
      sections = text.split(DEF_START)
      for sect in sections[1:]:
         name, defn = sect.split(DEF_END) ## error if multiple DEF_END's
         name, defn = name.strip(), defn.strip()
         if name in definitions:
            print('may not redefine macro', name)
            exit(-1)
         definitions[name] = defn
with open(out, 'w') as f:
    text = definitions[START_MACRO]
    while EXP_START in text:
       lines = text.split('\n')
       text = ''
       for line in lines:
          if EXP_START in line:
             spacing = line[:len(line)-len(line.lstrip())]
             name = line.replace(EXP_START, '').replace(EXP_END, '').strip()
             if name not in definitions:
                print('macro not found:', name)
                exit(-1)
             for defline in definitions[name].split('\n'):
                text += spacing + defline + '\n'
          else:
              text += line+'\n'
    f.write(text)




definitions = {}

def learn_from(text):
    defs = text.split('<<<')
    for d in defs[1:]:
        name, rest = d.split('>>>') ## error if multiple ">>>"s
        name, rest = name.strip(), rest.strip()
        if name not in definitions:
            definitions[name] = rest
        else:
            print('may not redefine macro', name)
            exit(-1)

def unweave(start='START'):
    text = definitions[start]
    while '<@' in text:
        new_text = ''
        lines = text.split('\n')
        for line in lines:
            if '<@' in line:
                spacing = line[:len(line)-len(line.lstrip())]
                name = line.replace('<@', '').replace('@>', '').strip()
                if name in definitions:
                    for defline in definitions[name].split('\n'):
                        new_text += spacing + defline + '\n'
                else:
                    print('macro not found:', name)
                    exit(-1)
            else:
                new_text += line+'\n'
        text = new_text
    return text


filenames = []
with open('make.txt') as file:
    filenames = file.read().split('\n')
out, ins = filenames[0], filenames[1:]

for filename in ins:
    with open(filename) as file:
        learn_from(file.read())

with open(out, 'w') as f:
    f.write(unweave())

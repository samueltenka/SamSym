definitions = {}

def learn_from(text):
    defs = text.split('<<<')
    for d in defs[1:]:
        sym, rest = d.split('>>>') ## error if multiple ">>>"s
        sym, rest = sym.strip(), rest.strip()
        if sym not in definitions:
            definitions[sym] = rest
        else:
            print('may not redefine macro', sym)
            exit(-1)

def unweave(start='START'):
    text = definitions[start]
    while '<@' in text:
        sects = text.split('<@')
        new_text = sects[0]
        for s in sects[1:]:
            sym, rest = s.split('@>') ## error if multiple "@>"s
            spacing = sym[:len(sym)-len(sym.lstrip())]
            sym, rest = sym.strip(), rest.strip()
            if sym in definitions:
                new_text += ''.join(spacing+line+'\n' for line in definitions[sym].split('\n')) + \
                            rest + '\n'
            else:
                print('could not find macro', sym)
                exit(-1)
        text = new_text
    return text


def remove_whitespace(text):
    while '\n\n' in text:
        text = text.replace('\n\n', '\n')
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

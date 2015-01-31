def floor(x): return int(x)
def ceil(x): return -floor(-x)

class ExprTree:
    def __init__(self, op=None, pieces=[]):
        if op and not pieces:
            self.op='atom'; self.pieces=[op]
        else:
            self.op=op; self.pieces=pieces
        self.height = None; self.width = None
    def __call__(self): return ExprTree('paren', [self]) #use later for parens? ... or should parens be calculated automatically?
    def __add__(self, other): return ExprTree('+', [self,other])
    def __sub__(self, other): return ExprTree('-', [self,other])
    def __mul__(self, other): return ExprTree('*', [self,other])
    def __truediv__(self, other): return ExprTree('/', [self,other])

    def get_height(self):
        if self.height: return self.height
        if self.op=='atom': self.height = 1
        elif self.op in '+-*': self.height = max(p.get_height() for p in self.pieces)
        elif self.op=='/': self.height = sum(p.get_height() for p in self.pieces) + 1
        elif self.op=='paren':
            self.height = self.pieces[0].get_height()
            if self.height >= 3: self.height += 2
        return self.height
    def get_width(self):
        if self.width: return self.width
        if self.op=='atom': self.width = len(str(self.pieces[0]))
        elif self.op in '+-*': self.width = sum(1+p.get_width() for p in self.pieces) - 1
        elif self.op=='/': self.width = max(p.get_width() for p in self.pieces)
        elif self.op=='paren':
            self.width = 2+self.pieces[0].get_width()
            if self.get_height() >= 3: self.width += 2
        return self.width

    def __str__(self):
        if self.op=='atom': return str(self.pieces[0])
        h = self.get_height(); w = self.get_width()
        hps = [p.get_height() for p in self.pieces]
        wps = [p.get_width() for p in self.pieces]
        substrs = [str(p).split('\n') for p in self.pieces]
        lines = []
        if self.op in '+-*':
            offsets = [(h-hps[j])/2.0 for j in range(len(self.pieces))]
            for i in range(h):
                lines.append('')
                for j in range(len(self.pieces)):
                    if j!=0:
                        if i==int(h/2): lines[i] += self.op
                        else: lines[i] += ' '
                    fo, co = floor(offsets[j]), ceil(offsets[j])
                    if fo<=i<h-co: lines[i] += substrs[j][i-fo]
                    else: lines[i] += ' '*wps[j]
        elif self.op=='/':
            offsets = [(w-wps[j])/2.0 for j in range(len(self.pieces))]
            i=0
            for j in range(len(self.pieces)):
                if i==int(h/2): lines.append('-'*w)
                fo, co = floor(offsets[j]), ceil(offsets[j])
                for l in substrs[j]: lines.append(' '*fo + l + ' '*co)
                i += hps[j]
        elif self.op=='paren':
            lines = substrs[0]
            if hps[0] == 1: lines = ['('+lines[0]+')']
            elif hps[0] == 2: lines = ['/'+lines[0]+'\\', '\\'+lines[1]+'/']
            elif hps[0] >= 3: lines = [' /'+' '*wps[0]+'\\ '] + \
                                      ['| '+l+' |' for l in lines] + \
                                      [' \\'+' '*wps[0]+'/ ']
        return '\n'.join(lines)
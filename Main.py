import ExprTree

e8 = ExprTree.ExprTree('a')
e9 = ExprTree.ExprTree(99)
ed = (e8+e9)/(e9+e8)
print(ed()()()+e8()()())
#print((ed+ed/ed)/(ed/ed+ed))

'''
OUTPUT:
 /            \
|  /        \  |
| |  /    \  | |
| | | 8+99 | | |
| | | ---- | | |+(((8)))
| | | 99+8 | | |
| |  \    /  | |
|  \        /  |
 \            /
'''

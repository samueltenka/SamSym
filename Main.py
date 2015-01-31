import ExprTree

a = ExprTree.ExprTree('a')
b = ExprTree.ExprTree('b')
c = ExprTree.ExprTree('c')
_4 = ExprTree.ExprTree(4)
_2 = ExprTree.ExprTree(2)
print(((b**_2-_4*a*c).sqrt()()-b)/(_2*a))

'''
OUTPUT:
 /           \
|    ________ |
|   | 2       |-b
| \/ b -4*a*c |
 \           /
-----------------
       2*a
'''

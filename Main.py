import ExprTree

a = ExprTree.ExprTree('a')
b = ExprTree.ExprTree('b')
c = ExprTree.ExprTree('c')
_4 = ExprTree.ExprTree('c')
_2 = ExprTree.ExprTree('c')
print(((b*b+_4*a*c).sqrt()-b)/(_2*a))
'''
OUTPUT:
  _________  
\/b*b+c*a*c-b
-------------
     c*a     
'''

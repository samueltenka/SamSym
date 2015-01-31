import ExprTree

a = ExprTree.ExprTree('a')
b = ExprTree.ExprTree('b')
c = ExprTree.ExprTree('c')
_4 = ExprTree.ExprTree(4)
_2 = ExprTree.ExprTree(2)
print((-b+(b**_2+_4*a*c).sqrt())/(_2*a))

'''
OUTPUT:
      ______
-b+  | 2
   \/ b +4ac
------------
     2a     
'''

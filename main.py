"""
@author: Amilcar Rodriguez
@e-mail: aar.velasquez@gmail.com
@github: mkhi26
"""

from BST.BST import BST
from Graph.Graph import BstToNx
b = BST()
b.add(10)
b.add(5)
b.add(4)
b.add(8)
b.add(9)
b.add(18)
b.add(12)
b.add(21)
b.add(2)
b.add(1)
b.add(3)

g = BstToNx(b)
g.addToGraph()
print(g.draw("binario"))


"""
@author: Amilcar Rodriguez
@e-mail: aar.velasquez@gmail.com
@github: mkhi26
"""
import networkx as nx
import matplotlib.pyplot as plt

class BstToNx:
    def __init__(self, tree):
        """
        Recibe como prarametro un árbol binario
        """
        self.tree = tree

        self.g = nx.Graph()
        self.g.add_node(self.tree.root.value)

    def addToGraph(self):
        """
        Agrega un árbol en inorden al grafo de networkX
        """
        return self.inorder(self.tree.root)
          
    def inorder(self, current):
        if current == None:
            return None
        else:
            parent = current.value
            left = current.left
            right = current.right
            if left:
                self.g.add_edge(parent, left.value)
            if right:
                self.g.add_edge(parent, right.value)
            self.inorder(current.left)
            
            self.inorder(current.right)

    def draw(self, nameImg):
            """
            Dibuja el árbol
            """
            plt.clf()
            G = self.g
            pos=nx.nx_agraph.graphviz_layout(G, prog="dot")
            nx.draw(G, pos, with_labels=True, node_size=800, node_color="purple", arrows=False, node_shape ="o", font_size=10 )
            plt.savefig("%s.png"%nameImg)
            plt.show()
            return True

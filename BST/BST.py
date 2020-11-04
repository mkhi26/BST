"""
@author: Amilcar Rodriguez
@e-mail: aar.velasquez@gmail.com
@github: mkhi26
"""
class NodeBST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BST:

    def __init__(self):
        self.root = None
    
    def add(self, value):
        """
        Nombre: add

        Parametros:
                value: elemento que se desea agregar en el árbol.

                retorna: Retorna un llamado a la función self.addInner para agregar internamente en el árbol.
        """
        return self.addInner(value, self.root)

    def addInner(self, value, current):
        """
        Nombre: addInner

        Parametros:
            value: elemento que se va a agregar al árbol.

            current: nodo del árbol en el que se buscara un lugar para agregar el nodo.

            Retorna: True si se agrego el nodo al árbol
        """
        if not self.root:
            self.root = NodeBST(value)
            return True
               
        elif value > current.value:
            if not current.right:
                current.right = NodeBST(value)
                return True
            else:
                return self.addInner(value,current.right)
        elif value < current.value:
            if not current.left:
                current.left = NodeBST(value)
                return True
            else:
                return self.addInner(value, current.left)
        
    
    def posorden(self, current = None):
        """
        Nombre: posorden

        Parametros: 
                current: nodo actual en el que nos encontramos en el árbol

        Retorno:
            No retorna

        Descripción: Recorre el árbol en posorden:
            
        """
        if current:
            self.posorden(current.left)
            self.posorden(current.right)
            print(current.value)

    def inorden(self, current = None):
        """
        Nombre: inorden

        Parametros: 
                current: nodo actual en el que nos encontramos en el árbol

        Retorno:
            No retorna

        Descripción: Recorre el árbol en inorden:
            
        """
        if current:
            self.inorden(current.left)
            print(current.value)
            self.inorden(current.right)

    def preorden(self, current = None):
        """
        Nombre: preorden

        Parametros: 
                current: nodo actual en el que nos encontramos en el árbol

        Retorno:
            No retorna

        Descripción: Recorre el árbol en preorden:
            
        """
        if current:
            print(current.value)
            if current.left:
                self.preorden(current.left)
            if current.right:
                self.preorden(current.right)


    def search(self, value):
        """
        Nombre: search

        Parametros: 
                value: valor a buscar dentro del árbol.

        Retorno:
            retorna el llamado a la función searchinner para buscar el nodo internamente.

        Descripción: Busca si existe un elemento en especifico dentro del árbol 
            
        """
        return self.searchInner(self.root, value)

    def searchInner(self, current, value):
        """
        Nombre: searchInner

        Parametros: 
                current: elemento actual en el que nos encontramos en el árbol.

                value: valor que se desea buscar dentro del árbol.
        """
        if not isinstance(current, NodeBST):
            return False
        if current.value == value:
            return True
        if current.value > value:
            if not current.left:
                return False
            return self.searchInner(current.left, value)
        elif(current.value < value):
            if not current.right:
                return False
            return self.searchInner(current.right, value)
        return False


    def delete(self, value):
        """
        Nombre: delete
        Parametros: 
                value: valor que se desea eliminar dentro del árbol.
        Retorno: retorna un llamado a la función self.deleteInner
        """
        return self.deleteInner(self.root, value)

    def deleteInner(self, current, value):
        """
        Posibilidades:
            1. El nodo a eliminar no tiene hijos.
            2. El nodo a eliminar tiene un hijo.
            3. El nodo a eliminar tiene sus dos hijos.

        * Si el nodo no tiene hijos se apunta el nodo a None.
        * Si el nodo tiene un hijo:
            - Si el nodo hijo es un hijo izquierdo entonces el nodo a eliminar se apunta al hijo izquierdo.
            - Si el nodo hijo es un hijo derecho entonces el nodo a eliminar se apunta sl hijo derecho.

        * Si el nodo a eliminar tiene sus dos hijos:


        """

        if not self.root or not self.search(value):
            """
            En caso de que el árbol este vació o no exista el valor del Nodo a eliminar entonces no realizara ninguna acción.
            """
            return False

        if current.value == value:
            """
            Si se encuentra el nodo a eliminar.
            """
            if (not current.left) and (not current.right):
                """
                El árbol no tiene hijos, entonces se elimina el nodo sin problema.
                """

                self.deleteChildless(current)
                return True
            elif (current.left) and not (current.right):
                """
                El árbol tiene un hijo izquierdo, pero no un hijo derecho, entonces se apunta el nodo a eliminar a su hijo izquierdo.
                """
                self.deleteWithOneChildren(current)
                return True
            elif(current.right) and not (current.left):
                """
                El árbol tiene un hijo derecho pero no un hijo izquierdo, entonces se apunta el nodo a eliminar a su hijo derecho.
                """
                self.deleteWithOneChildren(current)
                return True
            elif current.left and current.right:
                """
                El árbol tiene sus dos hijos.
                """
                self.deleteWithTwoChildren(current)
                return True

        elif current.value > value:
            """
            Si todavía no se ha encontrado el nodo a eliminar, entonces se sigue buscando de manera recursiva.
            """

            return self.deleteInner(current.left, value)
        elif current.value < value:
            """
            Si todavía no se ha encontrado el nodo a eliminar, entonces se sigue buscando de manera recursiva.
            """
            return self.deleteInner(current.right, value)

    def deleteChildless(self, current):
        current.value = None

    def deleteWithOneChildren(self, current):
        if current.left and not current.right:
            current = current.left
            return True
        if current.right and not current.left:
            current = current.right
            return True

    def deleteWithTwoChildren(self,current):
        """
        Para eliminar un nodo que tiene dos hijos:
                * Encontramos el nodo con menor valor posible (A la izquierda)
                
                
        """
        lowerChildrenLeft = self.getLowerValue(current.right)
        self.delete(lowerChildrenLeft.value)
        current.value = lowerChildrenLeft.value
        return True
        
    def getLowerValue(self, current):
        """
        Se busca el menor valor posible del nodo.
        """
        if not current.left:
            return current
        else:
            return self.getLowerValue(current.left)


    def subTree(self, value):
        """
        busca un nodo dentro del árbol, si el nodo existe entonces retornaara este como un nuevo árbol.
        """
        if not self.search(value):
            """
            Si el nodo no existe dentro del árbol, entonces no hará ninguna acción.
            """
            return False
        """
        Si el nodo existe, entonces procederá a encontrar el sub árbol.
        """
        return self.subTreeInner(self.root, value)

    def subTreeInner(self, current, value):
        if not self.root:
            """
            Si el árbol esta vació no se realiza ninguna acción.
            """
            return False
        if not isinstance(current, NodeBST):
            """
            Si current no es un Nodo del árbol, entonces no realiza ninguna acción.
            """
            return False

        if current.value == value:
            """
            Si se encuentra el nodo del sub árbol, entonces se crea una nueva instancia de árbol para agregar el sub arbol como un nuevo árbol, de esta manera el tree.root sera igual al sub arbol.
            Se retornara el nuevo árbol.
            """
            tree = BST()
            tree.root = current
            return tree

        if current.value < value:
            """
            se sigue buscando el nodo.
            """
            if not current.right:
                return False
            return self.subTreeInner(current.right, value)
        elif current.value > value:
            """
            se sigue buscando el nodo.
            """
            if not current.left:
                return False
            return self.subTreeInner(current.left, value)


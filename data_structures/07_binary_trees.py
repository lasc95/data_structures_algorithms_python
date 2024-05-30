"""
árbol binario: es una estructura de datos no lineal con un nodo raíz. Cada nodo del árbol puede contener máximo 2 nodos hijos, 
a su vez también pueden ser padres de dos más.

Propiedades fundamentales de un árbol binario:
* un nodo no puede tener más de dos hijos
* el hijo izquierdo es un nodo menor (o igual) que el valor del NODO PADRE
* el hijo derecho de un nodo es mayor (o igual) que el valor del NODO PADRE

"""

# implementation

class NodeBinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None # nodo hijo izquierdo
        self.right = None # nodo hijo derecho

class BinaryTree:
    def __init__(self, root):
        self.root = root
    
    def inorder(self, root):
        """
        inorder: de izquierda a derecha, es decir, de manera ascendente. primero revisa el nodo hijo izquierdo, luego el raíz
        finalmente el derecho (que es el que posee valor más grande que el padre).
        Este método por lo general se utiliza para las búsquedas binarias.
        1. left_child
        2. root
        3. right_child
        """
        if root:
            self.inorder(root.left) # recorremos el subarbol izquierdo
            print(root.data, end=" ") # imprimimos la data del arbol
            self.inorder(root.right) # recorremos el subarbol derecho

    # metodo recursivo para recorrer arbol en preorden
    def preorder(self, root):
        """
        preorder: primero vamos a la raíz, luego al izquierdo y finalmente al derecho. Este método se utiliza comunmente 
        para crear una copia del arbol.
        1. root
        2. left_child
        3. right_child
        """
        if root:
            print(root.data, end=" ")
            self.preorder(root.left) # recorremos el subarbol izquierdo
            self.preorder(root.right) # recorremos el subarbol derecho
    
    # metodo para recorrer postorder
    def postorder(self, root):
        """
        postorder: primero visitamos izquierdo, luego el derecho y finalmente la raíz. por lo general este método se utiliza para eliminar el arbol

        """
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")
    
    # método para buscar
    def search(self, root, value):
        if not root:
            return None
        
        if root.data == value:
            return root # valor encontrado en el nodo actual
        
        elif value < root.value:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)
        
    
    def insert(self, root, new_node):
        if not root:
            return new_node
        
        if new_node.data < root.value:
            root.left = self.insert(root.left, new_node)
        else:
            root.right = self.insert(root.right, new_node)

        return root
        

# uso
# creamos los nodos. Recordar que el nodo hijo derecho es mayor que el valor del nodo padre
root = NodeBinaryTree(10)
root.left = NodeBinaryTree(5)
root.right = NodeBinaryTree(15)

# creamos el arbol
binary_tree = BinaryTree(root)

binary_tree.inorder(root)

binary_tree.preorder(root)

binary_tree.postorder(root)

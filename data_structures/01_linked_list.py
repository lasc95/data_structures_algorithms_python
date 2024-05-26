"""
Linked list / Lista enlazada:
la lista enlazada es fundamental en las ciencias de la computación. 
Es una colección de Nodos donde cada Nodo tiene un campo de datos y una referencia (enlace) 
al siguiente nodo de la secuencia. El último Nodo de la lista apunta a un null, indicando que es el final de la lista

Cada Nodo consta de dos partes: los datos y el puntero al siguiente Nodo. Los datos almacenan información real, mientras 
que el puntero almacena la referencia al siguiente Nodo, generando una secuencia en Cadena.

"""

class Node:
    def __init__(self, data=None):
        self.data = data # la data almacenada
        self.next = None # referencia al nodo siguiente

class LinkedList:
    def __init__(self):
        self.head = None # inicializamos la cabeza de la lista como None

    def insert(self, data):
        if not self.head: # si la lista está vacía
            self.head = Node(data) # creamos Nodo y lo hacemos cabeza de lista
        else:
            cur = self.head # empezamos desde la cabeza
            while cur.next: # Mientras el nodo actual tenga un siguiente nodo
                cur = cur.next # avanzamos al siguiente nodo
            cur.next = Node(data) # creamos un nuevo Nodo al final de la lista

    # Método para mostrar los datos de la lista
    def display(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

# crear una lista enlazada e insertamos datos
l1 = LinkedList()
l1.insert(1)
l1.insert(2)

# Mostrar los datos de la lista enlazada
l1.display()

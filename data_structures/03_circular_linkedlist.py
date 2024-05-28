"""
Una lista donde todos los nodos están conectados formando un círculo. Es decir, el primer y último nodo están conectados
entre sí. NO HAY NULOS. 
En este caso no tendremos un puntero al nodo previo, ya que todos están enlazados
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data) # creamos el nuevo nodo
        if self.head is None: # en el caso de que la lista esté vacía
            self.head = new_node # la cabeza del nodo
            new_node.next = self.head # la anexamos a la misma cabeza
        else:
            current = self.head
            while current.next != self.head: # mientras el siguiente nodo no sea la cabeza (recordar que no existen nulos)
                current = current.next # actualizamos el currrent al siguiente
            current.next = new_node # el nuevo nodo lo asignamos al siguiente del actual
            new_node.next = self.head # el nuevo nodo tendrá como siguiente la cabeza (circular)
    
    # eliminamos
    def remove(self, node_value):
        if self.head: # si la lista no está vacía
            if self.head.data == node_value: # si el nodo a eliminar es la cabeza
                current = self.head
                while current.next != self.head: # vamos hasta el último nodo. 
                    current = current.next
                current.next = self.head.next # este sería el último nodo al que asignamos como siguiente, al que viene después del head
                self.head = self.head.next # actualizamos el primer nodo y se eliminaría
            else: # en el caso que no sea el primer nodo
                current = self.head
                prev = None
                while current.next != self.head: # iremos iterando hasta el último nodo (el que conecta con la cabeza de la lista)
                    prev = current # guardamos el actual en esta variable
                    current = current.next
                    if current.data == node_value:
                        prev.next = current.next # el anterior tendrá ahora como siguiente, el siguiente del actual. mantenemos la cadena
                        current = current.next # el nodo actual será el siguiente del que estamos eliminando

    # buscamos
    def search(self, node_value):
        if self.head: # empezamos desde la cabeza
            current = self.head
            while current.next != self.head:
                if current.data == node_value: # si lo encuentra retornamos True
                    return True
                current = current.next # avanzamos
        return False
    
    def display(self):
        current = self.head
        while current: 
            print(current.data)
            current = current.next
            if current == self.head:
                break

# creación de la lista
l1 = CircularLinkedList()

# agregamos
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)

# buscamos
print(l1.search(2))

# eliminamos
l1.remove(2)

#display
l1.display()

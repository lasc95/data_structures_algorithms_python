"""
A diferencia de la Simple linkedList (01). La double linkedList posee dos punteros: uno que va hacia el Nodo anterior
y otro al siguiente. Esto permite que se puedan hacer otras operaciones como insertar, eliminar e iterar.

Nodo: ahora el nodo tendrá 3 atributos: los datos, puntero al siguiente (self.next) y el puntero al anterior (self.prev), estos punteros nos
permiten navegar tanto hacia el nodo siguiente como al anterior
"""


class Node:
    def __init__(self, data):
        self.data = data # almacenamos los datos
        self.next = None # puntero al nodo siguiente
        self.prev = None # puntero al nodo anterior


class DoublyLinkedList:
    def __init__(self):
        self.head = None # Inicializamos la lista

    # insertar datos al final de la lista
    def append(self, data):
        if self.head is None: # si la lista está vacía
            self.head = Node(data) # creamos la cabeza de la lista
        else:
            current = self.head # empezamos desde la cabeza
            while current.next: # si existe un nodo siguiente
                current = current.next # avanzamos al siguiente nodo
                # recordar que este while se detendrá hasta que llegue al valor current.next == None (último Nodo)
            # ya una vez llegando al final de la lista
            new_node = Node(data) # creamos un nodo, aun no lo asignamos
            current.next = new_node # agregamos un Nodo al final de la lista.
            new_node.prev = current # el nodo anterior del nuevo nodo lo asignamos al nodo actual
    
    # insertar luego de un nodo ya dado
    def insert_after_node(self, prev_node, data):
        if prev_node is None: # si el nodo dado es None
            return # no se hace ninguna operación
        new_node = Node(data) # creamos un nodo con la data recibida
        new_node.next = prev_node.next # actualizamos el siguiente nodo, es decir, el siguiente del prev_node pasa a ser el siguiente del new_node
        prev_node.next = new_node # ahora el siguiente nodo del prev_node será new_node
        if new_node.next is not None: # si el nuevo nodo tiene un siguiente (si es que se insertó en medio de dos nodos)
            new_node.next.prev = new_node # actualizamos el prev del nodo siguiente, asignando que será el new_node, para que siga la cadena
    
    # método para eliminar un nodo
    def remove(self, node_value):
        current = self.head # comenzamos de la cabeza
        while current:
            if current.data == node_value: # si los datos del nodo actual son los que se entregaron
                if current.prev: # si existe un nodo previo al actual
                    current.prev.next = current.next # acomodamos, el siguiente del anterior, será el siguiente del actual
                if current.next: # si existe un nodo siguiente
                    current.next.prev = current.prev # acomodamos, el anterior del siguiente, será en este caso el anterior del actual
                if current == self.head: # si el nodo actual es la cabeza
                    self.head = current.next # desplazamos la cabeza hacia el siguiente
                # una vez actualizados todas las conexiones
                current = None # eliminamos el Nodo actual
                return # salimos de la función
            current = current.next # avanzamos al siguiente nodo

    # método para buscar
    def search(self, node_value):
        current = self.head # empezamos desde la cabeza
        while current: # mientras el nodo actual exista
            if current.data == node_value: #si los datos del nodo actual son los mismos que el nodo buscado
                return True # devolvermos bandera
            current = current.next # avanzamos al siguiente nodo
        return False

    # método para devolver el largo de nuestra lista
    def length(self):
        count = 0 # creamos un contador
        current = self.head # empezamos desde la cabeza
        while current: # mientras el nodo actual exista
            count += 1
            current = current.next
        return count # devolvermos el contador

    # método para mostrar nuestros nodos
    def display(self):
        current = self.head # empezamos desde la cabeza
        while current: # mientras el nodo actual exista
            print(current.data)
            current = current.next # avanzamos al siguiente nodo

# ejemplos de uso
l1 = DoublyLinkedList()

# append
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)

# insert after node
l1.insert_after_node(l1.head.next.next, 23)

# display
l1.display()

# remove
l1.remove(2)

# search
print(l1.search(4))
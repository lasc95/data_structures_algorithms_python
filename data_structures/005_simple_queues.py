"""
Simple Queue: cola simple, también se le conoce como Cola FIFO (First In, First Out).
Es decir: el primer elemento agregado, es el primer elemento que sale. 
Podríamos imaginarnos una fila de supermercado, el primer cliente en la fila, será el primero en salir
"""

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, element):
        # se agrega elemento al final de la cola
        self.items.append(element)
        print(f'element {element} added!')
    
    def dequeue(self):
        if not self.items.isEmpty():
            # se obtiene y elimina el primer elemento de la lista
            deleted_element = self.items.pop(0)
            print(f'element {deleted_element} has been deleted')
            return deleted_element

        return None
    
    def front(self):
        # retornamos el primer elemento de la cola sin eliminarlo
        if not self.items.isEmpty():
            first_element = self.items[0]
            return first_element

        return None
    
    def isEmpty(self):
        return len(self.items) == 0
    

# uso
queue = Queue()

queue.enqueue("elemento 1")
queue.enqueue("elemento 2")
queue.enqueue("elemento 3")
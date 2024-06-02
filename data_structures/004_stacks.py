"""
un Stack, conocido como Pila, es una estructura de datos LIFO (Last In, First Out), significa que el último elemento agregado, es el primer eliminado.
Podría asemejarse a una pila de platos, el último que se apila, es el primero que usamos.

"""

class Stack:
    def __init__(self):
        self.items = [] # almacenamos los elementos del stack

    def push(self, element):
        self.items.append(element)
        print(f'Added element {element}')
    
    def pop(self):
        if not self.isEmpty():
            deleted_element = self.items.pop()
            print(f'Element deleted {deleted_element}')
            return deleted_element
        else:
            print('Error, stack is Empty')
            return None
        
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print('Error: Stack is Empty')
            return None
    
    def isEmpty(self):
        return len(self.items) == 0
    
# ejemplo el uso
stack = Stack()

stack.push("Elemento 1")
stack.push("Elemento 2")
stack.push("Elemento 3")

print(f'Elemento {stack.peek()}')

stack.pop()
stack.pop()

print(f'Es vacío? {stack.isEmpty()}')
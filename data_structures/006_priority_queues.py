class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:

    def __init__(self):
        self.heap = []

    def insert(self, value, priority):
        new_node = Node(value, priority)
        self.heap.append(new_node)
        self.float_up(len(self.heap) - 1)

    def float_up(self, index):
        parent_index = (index - 1) // 2 # formula estandar para encontrar al nodo padre
        if parent_index >= 0  and self.heap[index].priority > self.heap[parent_index].priority:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.float_up(parent_index)
    
    def extract_max(self):
        if not self.heap:
            raise Exception('Priority queue is Empty')
        
        max_node = self.heap[0]
        last_node = self.heap.pop()

        if self.heap: # verifica si el montículo no está vacío
            self.heap[0] = last_node
            self.sink_down(0)

        return max_node.value, max_node.priority
    
    def sink_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = left_child_index + 1

        largest_index = index

        if left_child_index < len(self.heap) and self.heap[left_child_index].priority > self.heap[largest_index].priority:
            largest_index = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index].priority > self.heap[largest_index].priority:
            largest_index = right_child_index

        if largest_index != index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.sink_down(largest_index)

priority_queue = PriorityQueue()

priority_queue.insert('Tarea urgente!', 10)
priority_queue.insert('Tarea no tan urgente', 7)
priority_queue.insert('Tarea', 4)

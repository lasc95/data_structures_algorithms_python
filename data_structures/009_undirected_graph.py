"""
un grafo no dirigido está compuesto por:
 - vértices (nodos): representan entidades
 - Aristas (enlaces): Conectan dos nodos (vertices) sin ninguna dirección, es decir, la conexión no tiene sentido 
 específico

Propiedades:
    simetría: si existe una arista entre el vértice A y el vértice B entonces también existe entre B y A
    conectividad: un grafo es conexo si hay un camino entre cualquier par de vertices

"""

class UndirectedGraph:
    def __init__(self):
        # inicializamos un diccionario vacio para almacenar el grafo
        self.graph = {}

    def add_vertex(self, vertex):
        # agregamo un vertice al grafo si no existe
        if vertex not in self.graph:
            self.graph[vertex] = []
        
    def add_edge(self, vertex1, vertex2):
        # agrega una arista entre dos vertices (no dirigida)
        # agregamos vertice1 a la lista de adyacencia de vertice2 y viceversa
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
        else:
            print('uno o dos vertices no existen')
        
    def display_graph(self):
        # imprimimos cada vertice y conexiones
        for vertex in self.graph:
            print(f'vertex: {vertex}: {self.graph[vertex]}')


# Ejemplo de uso:
graph = UndirectedGraph()

# Agregar vértices
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")

# Agregar aristas
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")

# Mostrar el grafo
graph.display_graph()
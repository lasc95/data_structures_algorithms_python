"""
Grafo dirigido: estructura compuesta por un conjunto de vértices (nodos) y un conjunto de aristas (enlaces) que conectan pares de
vértices (nodos). Los grafos se utilizan en diversidad de disciplinas

Dígrafo es un tipo de grafo donde las aristas tienen dirección. Esto quiere decir que una arista va de un vértice a otro específico.

Un grafo dirigido "G" se define como un par G = (V, E) donde: 
* V conjunto de vértices
* E es un conjunto de aristas, donde cada arista es un par ordenado de vértices (u, v) indicando una conexión de u a v

Terminología:
* Vértice: también conocido como nodo, es un punto de conexión en el grafo
* Arista: también conocido como enlace o arco, es una conexión entre dos vértices. En un dígrafo, cada arista tiene dirección
* Grado de entrada: el n de aristas que llegan a un vértice
* Grado de salida: el n de aristas que salen de un vértice
* Camino: Una secuencia de vértices donde cada vértice(nodo) está conectado al siguiente a una arista(enlace)
* Ciclo: Un camino que comienza y termina en el mismo vértice

Representación de los grafos: usualmente se pueden representar de estass maneras
* Lista de Adyacencia: Usa una lista (o diccionario) donde cada vértice tiene una lista de los vértices a los que está conectado
* Matriz de adyacencia: Usa una matriz donde las filas y columnas representan vértices y las entradas indican si existe 
una arista entre dos vértices
"""

class DirectedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        # agregamos un vertice (nodo) al grafo
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        # agrega una arista dirigidade nodo "u" a nodo "v"
        # ambos nodos deben ya existir
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u].append(v)
        else:
            raise ValueError("uno o ambos vértices no existen.")

    def remove_vertex(self, v):
        # elimina un vértice (nodo), todas sus conexiones asociadas
        if v in self.adj_list: # verificamos si el nodo existe
            for key in self.adj_list:
                if v in self.adj_list[key]: # verificamos si el vertive está en alguna conexión proveniente de otro
                    self.adj_list[key].remove(v) # eliminamos el vertice
            # eliminamos el vértice 
            del self.adj_list[v]

    def remove_edge(self, u, v):
        # elimina la arista dirigida de u a v
        if u in self.adj_list and v in self.adj_list[u]:
            self.adj_list[u].remove(v)

    def get_vertices(self):
        return list(self.adj_list.keys())
    
    def get_edges(self):
        # devuelve una lista con todas las aristas de un grafo
        edges = []
        for u in self.adj_list:
            for v in self.adj_list[u]:
                edges.append((u, v))
        return edges
    
    def __str__(self):
        # devuelve una representación en cadena de grafo
        return '\n'.join([f"{v}: {self.adj_list[v]}" for v in self.adj_list])
    

# Ejemplo de uso
grafo = DirectedGraph()
grafo.add_vertex('A')
grafo.add_vertex('B')
grafo.add_vertex('C')

grafo.add_edge('A', 'B')
grafo.add_edge('B', 'C')
grafo.add_edge('A', 'C')

# grafo.remove_vertex('A')

print("Vértices (nodos) del grafo:", grafo.get_vertices())
print("Aristas (enlaces) del grafo:", grafo.get_edges())
print('\n')
print("Representación del grafo:\n", grafo)

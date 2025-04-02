from collections import defaultdict

class Graph:
    def __init__(self):
        # Diccionario con la lista de adyacencia
        self.graph = defaultdict(list)
        # Diccionario para asignar índices a los nodos
        self.nodes = {}
        # Diccionario inverso para traducción
        self.reverse_nodes = {}
        # Número de vértices
        self.V = 0

    def addNode(self, name):
        """Asigna un índice a cada nodo único"""
        if name not in self.nodes:
            self.nodes[name] = self.V
            self.reverse_nodes[self.V] = name
            self.V += 1

    def addEdge(self, u, v):
        """Agrega una arista entre nodos"""
        self.graph[self.nodes[u]].append(self.nodes[v])

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        stack.append(v)

    def topologicalSort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        # Convertir índices de vuelta a nombres de nodos y mostrar el resultado
        print([self.reverse_nodes[i] for i in stack[::-1]])

def main():
    g = Graph()
    # Agregar nodos
    for node in ['a', 'b', 'm', 't', 'g', 'k', 's']:
        g.addNode(node) 
    # Agregar aristas según la descripción
    g.addEdge('b', 'm')
    g.addEdge('b', 't')
    g.addEdge('a', 's')
    g.addEdge('a', 'b')
    g.addEdge('t', 'g')
    g.addEdge('t', 'k')
    g.addEdge('g', 's')
    print("EL ORDENAMIENTO TOPOLOGICO SERIA:-----------------------:")
    g.topologicalSort()

if __name__ == "__main__":
    main()

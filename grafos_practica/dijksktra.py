import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        """Imprime la solución del algoritmo Dijkstra."""
        print("Vértice \tDistancia desde el Origen")
        for node in range(self.V):
            node_label = chr(65 + node)  # Convierte índice a letra (A=0, B=1, etc.)
            print(f"{node_label} \t\t{dist[node]}")

    def minDistance(self, dist, sptSet):
        """
        Encuentra el vértice con la distancia mínima entre los vértices
        no incluidos aún en el árbol de caminos más cortos.
        """
        min_dist = sys.maxsize
        min_index = -1

        for u in range(self.V):
            if dist[u] < min_dist and sptSet[u] == False:
                min_dist = dist[u]
                min_index = u

        return min_index

    def dijkstra(self, src):
        """
        Implementa el algoritmo de Dijkstra para calcular caminos más cortos
        desde un vértice origen hacia todos los demás vértices.
        """
        # Inicialización de estructuras
        dist = [sys.maxsize] * self.V  # Inicializar todas las distancias como infinito
        dist[src] = 0  # Distancia del nodo origen a sí mismo es 0
        sptSet = [False] * self.V  # Ningún vértice está incluido en el SPT inicialmente
        
        # Vector para guardar el predecesor de cada vértice (para reconstruir caminos)
        predecessor = [-1] * self.V

        # Encontrar el camino más corto para todos los vértices
        for count in range(self.V):
            # Seleccionar el vértice con distancia mínima del conjunto de vértices
            # que aún no han sido procesados
            u = self.minDistance(dist, sptSet)
            
            # Si no se encontró un vértice válido (todos los nodos restantes son inalcanzables)
            if u == -1:
                break
                
            # Marcar el vértice seleccionado como procesado
            sptSet[u] = True

            # Actualizar la distancia de los vértices adyacentes al vértice seleccionado
            for v in range(self.V):
                # Actualizar dist[v] solo si:
                # 1. Hay una arista de u a v (peso > 0)
                # 2. v no está en sptSet
                # 3. La distancia total a través de u es menor que el valor actual de dist[v]
                if (self.graph[u][v] > 0 and 
                    sptSet[v] == False and 
                    dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
                    predecessor[v] = u

        # Imprimir la solución
        print(f"\nResultados desde el nodo origen {chr(65 + src)}:")
        self.printSolution(dist)
        
        # Imprimir caminos
        self.printPaths(src, dist, predecessor)
        
        return dist, predecessor
    
    def printPaths(self, src, dist, predecessor):
        """Imprime los caminos más cortos desde el nodo origen a cada destino."""
        print("\nCaminos más cortos:")
        for i in range(self.V):
            if i != src:
                path = []
                self.getPath(i, predecessor, path)
                if dist[i] == sys.maxsize:
                    print(f"{chr(65 + src)} → {chr(65 + i)}: No alcanzable")
                else:
                    path_str = " → ".join([chr(65 + node) for node in path])
                    print(f"{chr(65 + src)} → {chr(65 + i)} (Distancia: {dist[i]}): {path_str}")
    
    def getPath(self, current, predecessor, path):
        """Reconstruye recursivamente el camino desde el origen hasta el nodo current."""
        # Si el nodo actual no tiene predecesor, hemos llegado al origen
        if predecessor[current] == -1:
            path.append(current)
            return
        
        self.getPath(predecessor[current], predecessor, path)
        path.append(current)

def main():
    # Crear un grafo con 8 vértices correspondientes a los nodos A-H
    g = Graph(8)
    
    # Definir la matriz de adyacencia del grafo basado en la descripción
    g.graph = [
        # A  B  C  D  E  F  G  H
        [0, 3, 5, 2, 0, 0, 0,10],  # A
        [3, 0, 5, 8, 4, 0, 6, 6],  # B
        [5, 5, 0, 0, 1, 7, 9, 0],  # C
        [2, 8, 0, 0, 12, 0, 0, 14],  # D
        [0, 4, 1, 12, 0, 0, 15, 0],  # E
        [0, 0, 7, 0, 0, 0, 0, 9],  # F
        [0, 6, 9, 0, 15, 0, 0, 3],  # G
        [10,6, 0, 14, 0, 9, 3, 0]   # H
    ]
    
    # Imprimir la estructura del grafo (matriz de adyacencia)
    print("Estructura del grafo (matriz de adyacencia):")
    print("   ", " ".join([f"{chr(65+i):2}" for i in range(g.V)]))
    for i in range(g.V):
        print(f"{chr(65+i):2}", end=" ")
        for j in range(g.V):
            print(f"{g.graph[i][j]:2}", end=" ")
        print()
    
    # Ejecutar el algoritmo de Dijkstra desde todos los nodos origen
    start_nodes = range(g.V)  # Ejecutar para todos los nodos A-H
    for src in start_nodes:
        g.dijkstra(src)
        print("\n" + "-"*50)

if __name__ == "__main__":  # Correcto
    main()
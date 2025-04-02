# 📊 Algoritmos de Grafos en Python

Implementaciones de tres algoritmos fundamentales para el procesamiento de grafos:

1. Ordenamiento Topológico (`topologico.py`)
2. Algoritmo de Kruskal (`kruskal.py`)  
3. Algoritmo de Dijkstra (`dijksktra.py`)

## 🚀 Cómo usar cada algoritmo

### 1. Ordenamiento Topológico
```python
from topologico import Graph

g = Graph()
# Agregar nodos
for node in ['a', 'b', 'c']:
    g.addNode(node)
# Agregar aristas
g.addEdge('a', 'b')
g.addEdge('b', 'c')
# Obtener orden
g.topologicalSort()  # Output: ['a', 'b', 'c']

2. Algoritmo de Kruskal
python

# Configuración automática en el archivo
nodes = {'a':1, 'b':2, 'c':3}
edges = [('a','b',3), ('b','c',5)]

mst = kruskal_mst(edges)
# Output: 
# Aristas del árbol de mínima expansión:
# a - b : 3
# b - c : 5


3. Algoritmo de Dijkstra
python

from dijksktra import Graph

g = Graph(3)  # 3 nodos (A,B,C)
g.graph = [
    [0, 1, 4],  # A
    [1, 0, 2],  # B 
    [4, 2, 0]   # C
]

g.dijkstra(0)  # Calcula desde nodo A
# Output muestra distancias y caminos


📦 Estructura del proyecto

/algoritmos-grafos
│
├── topologico.py    # Ordenamiento topológico
├── kruskal.py       # Árbol de mínima expansión  
├── dijksktra.py     # Caminos más cortos
└── README.md        # Este archivo



🛠️ Requisitos
Python 3.6+

Módulos estándar (no se requieren instalaciones adicionales)

📌 Notas importantes
Kruskal solo funciona con grafos no dirigidos

El ordenamiento topológico requiere un DAG (grafo acíclico)

Dijkstra usa matriz de adyacencia con índices numéricos

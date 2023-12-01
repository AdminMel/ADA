import heapq  # Importamos el módulo heapq para implementar la cola de prioridad
import time  # Importamos el módulo time para medir el tiempo de ejecución
import random  # Importamos el módulo random para generar números aleatorios
import matplotlib.pyplot as plt  # Importamos matplotlib para graficar

# Creamos una clase para representar nuestro Grafo
class Graph:
    def __init__(self):
        # Inicializamos un diccionario para almacenar los vértices y sus conexiones
        self.vertices = {}
    
    # Método para agregar un nuevo vértice al grafo
    def add_vertex(self, vertex):
        # Verificamos si el vértice no existe ya antes de agregarlo
        if vertex not in self.vertices:
            # Agregamos el vértice al diccionario con una lista vacía de conexiones
            self.vertices[vertex] = []
    
    # Método para agregar una arista (con peso) entre dos vértices
    def add_edge(self, from_vertex, to_vertex, weight):
        # Añadimos la conexión desde un vértice de inicio a otro con su respectivo peso
        self.vertices[from_vertex].append((to_vertex, weight))

# Función para el algoritmo de Dijkstra
def dijkstra(graph, start_vertex):
    # Creamos un diccionario para almacenar las distancias mínimas
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    # Establecemos la distancia mínima desde el vértice inicial a él mismo como 0
    distances[start_vertex] = 0
    # Creamos una cola de prioridad con la distancia actual y el vértice actual
    priority_queue = [(0, start_vertex)]

    # Mientras haya elementos en la cola de prioridad
    while priority_queue:
        # Obtenemos el vértice actual y su distancia
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Si la distancia actual es mayor que la registrada, no hacemos nada
        if current_distance > distances[current_vertex]:
            continue

        # Iteramos sobre los vecinos del vértice actual
        for neighbor, weight in graph.vertices[current_vertex]:
            # Calculamos la nueva distancia
            distance = current_distance + weight

            # Si la nueva distancia es menor que la registrada, actualizamos la distancia
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Agregamos el vecino y su nueva distancia a la cola de prioridad
                heapq.heappush(priority_queue, (distance, neighbor))

    # Devolvemos las distancias mínimas
    return distances

# Función para generar un grafo aleatorio
def generate_random_graph(num_vertices):
    G = Graph()
    
    for i in range(1, num_vertices + 1):
        G.add_vertex(str(i))

    for i in range(1, num_vertices + 1):
        for j in range(i + 1, num_vertices + 1):
            if random.choice([True, False]):
                weight = random.randint(1, 10)
                G.add_edge(str(i), str(j), weight)

    return G

# Realizar experimentos
max_vertices = 100
execution_times = []
num_vertices_list = []

# Iteramos sobre diferentes tamaños de grafo
for i in range(5, max_vertices + 1, 5):
    total_time = 0
    # Realizamos 10 experimentos por tamaño de grafo
    for _ in range(10):
        graph = generate_random_graph(i)

        start_time = time.time()
        dijkstra(graph, "1")
        end_time = time.time()

        total_time += end_time - start_time

    # Calculamos el tiempo promedio de ejecución
    avg_time = total_time / 10
    execution_times.append(avg_time)
    num_vertices_list.append(i)

# Graficar los resultados
plt.plot(num_vertices_list, execution_times, marker='o')
plt.xlabel('Número de Vértices')
plt.ylabel('Tiempo Promedio de Ejecución (s)')
plt.title('Comportamiento del algoritmo de Dijkstra con Grafos Aleatorios')
plt.show()

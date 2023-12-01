import heapq
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

# Ejemplo de uso
grafo = Graph()
grafo.add_vertex("A")
grafo.add_vertex("B")
grafo.add_vertex("C")
grafo.add_edge("A", "B", 3)
grafo.add_edge("A", "C", 5)
grafo.add_edge("B", "C", 2)

# Definimos el vértice de inicio
start_vertex = "A"
# Llamamos a la función dijkstra para obtener las distancias mínimas
resultado = dijkstra(grafo, start_vertex)
# Imprimimos los resultados
print(f"Caminos mínimos desde {start_vertex}: {resultado}")


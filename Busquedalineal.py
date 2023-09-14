import time

n = int(input("Ingrese el tamaño del arreglo: "))
x = [float(input(f"Ingrese el elemento {i + 1}: ")) for i in range(n)]
t = float(input("Ingrese el valor a buscar "))

def busqueda_lineal(lista, elemento):
    start_time = time.time()
    for i, valor in enumerate(lista):
        if valor == elemento:
            end_time = time.time()  
            elapsed_time = end_time - start_time 
            return i, elapsed_time  
    end_time = time.time()  
    elapsed_time = end_time - start_time  
    return -1, elapsed_time  

indice, tiempo_ejecucion = busqueda_lineal(x, t)

if indice != -1:
    print(f"El elemento {t} se encuentra en el índice {indice}")
else:
    print(f"El elemento {t} no se encuentra en el arreglo")

print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")
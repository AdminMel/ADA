import time
start_time = time.time()
n = int(input("Ingrese el tamaño del arreglo: "))
x = [float(input(f"Ingrese el elemento {i + 1}: ")) for i in range(n)]
t = float(input("Ingrese el valor a buscar "))

def busqueda_lineal(lista, elemento):
    for i, valor in enumerate(lista):
        if valor == elemento:
            return i 
    return -1  
indice = busqueda_lineal(x, t)
if indice != -1:
    print(f"El elemento {t} se encuentra en el índice {indice}")
else:
    print(f"El elemento {t} no se encuentra en el arreglo")
end_time = time.time() 
elapsed_time = end_time - start_time 
print(f"Tiempo de ejecución: {elapsed_time} segundos")
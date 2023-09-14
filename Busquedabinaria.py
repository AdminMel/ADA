import time
n = int(input("Ingrese el tamaño del arreglo: "))
x = [float(input(f"Ingrese el elemento {i + 1}: ")) for i in range(n)]
t = float(input("Ingrese el valor a buscar "))
def mezcla(inicio, medio, fin):
    n1 = medio - inicio + 1
    n2 = fin - medio
    izquierda = [0] * n1
    derecha = [0] * n2
    for i in range(n1):
        izquierda[i] = x[inicio + i]
    for j in range(n2):
        derecha[j] = x[medio + 1 + j]
    i = 0
    j = 0
    k = inicio
    while i < n1 and j < n2:
        if izquierda[i] <= derecha[j]:
            x[k] = izquierda[i]
            i += 1
        else:
            x[k] = derecha[j]
            j += 1
        k += 1
    while i < n1:
        x[k] = izquierda[i]
        i += 1
        k += 1
    while j < n2:
        x[k] = derecha[j]
        j += 1
        k += 1
def omezcla(inicio, fin):
    if inicio < fin:
        medio = inicio + (fin - inicio) // 2
        omezcla(inicio, medio)
        omezcla(medio + 1, fin)
        mezcla(inicio, medio, fin)
omezcla(0, len(x) - 1)
def busqueda_binaria():
    b = 0
    a = len(x) - 1
    central = 0

    while b <= a:
        central = (b + a) // 2

        if t < x[central]:
            a = central - 1
        elif t > x[central]:
            b = central + 1
        else:
            break

    if t == x[central]:
        print(f"Elemento encontrado :D en la posición: {central + 1}")
    else:
        print("El elemento no está en el vector D:")
start_time = time.time()  
busqueda_binaria()
end_time = time.time()  
elapsed_time = end_time - start_time  
print(f"Tiempo de ejecución de la búsqueda binaria: {elapsed_time} segundos")
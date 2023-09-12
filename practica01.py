#Hecho por Melanie Aileen Roman Espitia
import time 
def Burbuja(x):
    print("ordenado: burbuja\n")
    n = len(x)
    for i in range(n):
        for j in range(0, n - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
def Burbujam(x):
   print( "ordenado:burbuja mejorada\n")
   n = len(x)
   ayuda = int
   for i in range(n):
        for j in range(0, n-1-i):
            if(x[j]>x[j+1]):
                ayuda=x[j]
                x[j]=x[j+1]
                x[j+1]=ayuda
while True:
    s = int(input("Menu\n1) Ordenamiento Burbuja\n2) Ordenamiento Burbuja mejorada\n3) Salir\n"))
    if s == 1 or s == 2:
        n = int(input("Ingrese el tamaño del arreglo: "))
        print("Ingrese el arreglo1")
        x = [float(input(f"Ingrese el elemento {i + 1}: ")) for i in range(n)]
        
        if s == 1:
            Burbuja(x)
        else:
            Burbujam(x)
        print("Arreglo ordenado:", x)
    elif s == 3:
        print("Adiós")
        break
    else:
        print("Ingrese una opción válida")
    
    
        

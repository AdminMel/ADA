# Hecho por Melanie Aileen Roman Espitia
import time

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))

while True:
    s = int(input("Menu\n1) Suma\n2) Resta\n3) Multiplicacion\n4) Division\n5) Salir\n"))

    if s == 1:
        print(n1 + n2)
    elif s == 2:
        print(n1 - n2)
    elif s == 3:
        print(n1 * n2)
    elif s == 4:
        if n2 == 0:
            print("Error: No se puede dividir por cero.")
        else:
            print(n1 / n2)
    elif s == 5:
        print("Adiós")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")

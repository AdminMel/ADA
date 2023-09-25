def Fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibo(n - 1) + Fibo(n - 2)
def Fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*Fact(n-1)
def main():
    while True:
        print("Menú")
        print("1) Fibonacci")
        print("2) Factorial")
        print("3) Salir")
        opcion = int(input("Ingrese un número de opción: "))
        if opcion == 1:
            n = int(input("Ingrese un número de la posición que desea saber de la sucesión Fibonacci: "))
            print(f"El término {n}-ésimo de la secuencia de Fibonacci es {Fibo(n)}.")
        elif opcion == 2:
            n = int(input("Ingrese el número para calcular su factorial: "))
            Fact(n)
            print(f"El factorial de {n} es {Fact(n)}.")
        elif opcion == 3:
            print("Adióh")
            break
        else:
            print("Opción no válida")
main()
def Fibo():
    n = int(input("Ingrese el valor n: "))
    fibo = [0, 1]
    if n < 2:
        print("El valor de n debe ser igual o mayor a 2.")
    else:
        for i in range(2, n + 1):
            fibo.append(fibo[i - 2] + fibo[i - 1])
    print("El término Fibonacci en la posición", n, "es:", fibo[n])
def Fact():
    n=int(input("Ingrese el numero a calcular el factorial: "))
    fact=1
    for i in range (1,n+1):
        fact=fact*i
    print("factorial de ",n," = ",fact)
def main():
    while True:
        print("Menú")
        print("1) Fibonacci")
        print("2) Factorial")
        print("3) Salir")
        opcion = int(input("Ingrese un número de opción: "))
        if opcion == 1:
            Fibo()
        elif opcion == 2:
            Fact();
        elif opcion == 3:
            print("Adióh")
            break
        else:
            print("Opción no válida")
main()
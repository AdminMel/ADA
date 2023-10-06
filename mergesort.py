#Función para dividir el arreglo
def mergesort(x):
    #CASO BASE
    if len(x)<=1:
        return x
    #Dividir
    #Obtener la mitad del arreglo
    mitad=len(x)//2
    #Divide el arreglo en mitades
    izq=x[:mitad]
    der=x[mitad:]
    #conquistar
    #Llamar a la función recursiva
    izq=mergesort(izq)
    der=mergesort(der)
    #COMBINAR
    return merge(izq,der)
def merge(izq,der):
    ordenar=[]
    i_izq, i_der=0,0
    #Ciclo para comparar todos los elementos
    while i_izq<len(izq) and i_der<len(der):
        if izq[i_izq]<der[i_der]:
            ordenar.append(izq[i_izq])
            i_izq+=1
        else:
            ordenar.append(der[i_der])
            i_der+=1
    #Agregar todos los valores restantes
    ordenar.extend(izq[i_izq:])
    ordenar.extend(der[i_der:])
    return ordenar
if __name__=='__main__':
    n = int(input("Ingrese el tamaño del arreglo: "))
    x = [float(input(f"Ingrese el elemento {i + 1}: ")) for i in range(n)]
    ordener=mergesort(x)
    print("Arreglo ordenado: ", ordener)
            
        
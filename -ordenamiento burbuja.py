scores=[60,40,1,95,84,63,78,43,61,58,96,2,48,6]
def bubble_Short(arreglo):
    longitud=len(arreglo)-1
    for a in range(0,longitud):
        for b in range(0,longitud):
            aux=arreglo[b]
            if arreglo[b]>arreglo[b+1]:
                arreglo[b]=arreglo[b+1]
                arreglo[b+1]=aux
    return arreglo
print("Desordenado: ",scores)
print("Ordenado: ",bubble_Short(scores))
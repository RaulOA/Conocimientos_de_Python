scores=[1, 2, 6, 40, 43, 48, 58, 60, 61, 63, 78, 84, 95, 96]
def binary_Search(buscar):
    inicio=0
    final=len(scores)-1
    contador=0
    while inicio<=final:
        puntero=(inicio+final)//2
        contador+=1
        print("Step #",contador)
        if scores[puntero]==buscar:
            return print("Tu busqueda se ha encontrado en la pocicion: ",puntero+1)
        elif scores[puntero]<buscar:
            inicio=puntero+1
        else:
            final=puntero-1
    return print("Tu busqueda no ha sido encontrada")
binary_Search(661)
"""
    definir una funcion superpocicion[] 2 listas devolver true 
    si tienen al menos un elemento en comun
"""

def superpocicion(lista1,lista2):
    for miki in lista1:
        if miki in lista2:
            return True
    return False

print(superpocicion([1,2,4],[4,5,6]))
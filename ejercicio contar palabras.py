""" Escribir un programa que reciba una cadena de caracteres y 
devuelva un diccionario con cada palabra que contiene y su frecuencia. 
Escribir otra función que reciba el diccionario generado con la función 
anterior y devuelva una tupla con la palabra más repetida y su frecuencia."""
def dic(string):
    characters = "'!?.,;:"
    string.lower()
    for x in range(len(characters)):
        string = string.replace(characters[x],"")
    string=string.title()
    lista=string.split(" ")
    respuesta={}
    for a in lista:
        respuesta[a]=lista.count(a)
    return respuesta
diccionario=dic("Estos ejercicios, tienen Como? propósito mejorar; nuestras: Como habilidades, tienen?? como: programador; Como python")
print(diccionario)
def tup(a):
    mayor1=0
    mayor2=""
    for x,y in a.items():
        if y>mayor1:
            mayor1=y
            mayor2=x
    lista=[mayor2,mayor1]
    respuesta=tuple(lista)
    return respuesta
print(tup(diccionario))



""" Escribir un programa que reciba una cadena de caracteres y 
devuelva un diccionario con cada palabra que contiene y su frecuencia. 
Escribir otra función que reciba el diccionario generado con la función 
anterior y devuelva una tupla con la palabra más repetida y su frecuencia."""
def dic(string):
    characters = "'!?.,;:"
    respuesta={}
    for x in range(len(characters)):
        string = string.replace(characters[x],"")
    string=string.title().split(" ")
    for a in string:
        respuesta[a]=string.count(a)
    return respuesta

def tup(a):
    mayor=[0,0]
    for x,y in a.items():
        if y>mayor[0]:
            mayor[0]=y
            mayor[1]=x
    respuesta=tuple(mayor)
    return respuesta

diccionario=dic("Estos ejercicios, tienen Como? propósito mejorar; nuestras: Como habilidades, tienen?? como: programador; Como python")
print(diccionario)
print(tup(diccionario))



import os
os.system("cls")

#Solicitar un nombre por teclado y cuenta cuantas vocales tiene

def obtener_vocales(frase):
    vocales="aeiouAEIOU"
    return set([c for c in frase if c in vocales])
print(obtener_vocales("hola"))






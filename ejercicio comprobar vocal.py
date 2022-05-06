"""Ingresa un texto y verifica si tiene el punto al final de la oración"""
import os
os.system("cls")

a=input("Ingrese el texto: ")
b=a.lower()

if "a" in b or "e" in b or "i" in b or "o" in b or "u" in b:
    print("Si Tiene vocales")

else:
    print("No Tiene vocales")

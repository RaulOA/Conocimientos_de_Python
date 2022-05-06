palabra=input("ingrese una frase:")
inversa=palabra[::-1]
if inversa in palabra:
    print("en un palindrome")
else:
    print(inversa,", y no es un palindromo")
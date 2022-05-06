import os
os.system("cls")

cadena="   te quiero mucho   "
# 2 primeros caracteres
print(cadena[0:2])
# 3 ultimos caracteres
print(cadena[-3:])
# cada 2 caracteres
print(cadena[::2])
# de atras hacia adelante
print(cadena[::-1])
# contar caracteres
print(len(cadena))
# si "t" esta dentro de cadena
print("t" in cadena)
# Mayusculas
print(cadena.upper())
# Minusculas
print(cadena.lower())
# Titulo
print(cadena.title())
# Quitar espacios al final de la cadena
print(cadena.rstrip())
# Quitar espacios al principio de la cadena
print(cadena.lstrip())

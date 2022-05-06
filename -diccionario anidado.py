import os
os.system("cls")

# Añadir a un diccionario anidado
def append_value(Diccionario, Clave, Valor):
    if Clave in Diccionario:
        # Compruebe si el tipo de valor de la clave es una lista o no
        if not isinstance(Diccionario[Clave], list):
            # Si el tipo no es una lista, hazlo una lista
            Diccionario[Clave] = [Diccionario[Clave]]
        Diccionario[Clave].append(Valor)
    else:
        Diccionario[Clave] = Valor
Datos = {"7-1": {"1-1537-0036":["Ronald","Arias FAllas"]}}
append_value(Datos, '7-1', {"1-1111-1111":["Raul","asd ssss"]})
print(Datos)

# Recorriendo un diccionario anidado con una sola clave
secciones1={'10-1': {'206780934': ['raul', 'ortega']}}
for a,b in secciones1['10-1'].items():
    print(a,b[0],b[1])

# Recorriendo un diccionario anidado con varias claves
secciones2={'10-1': 
[{'0001': ['raul', 'ortega']}, 
{'0002': ['luis', 'armando']}, 
{'0003': ['david', 'solis']}]}
for a in secciones2.keys():
    print(a)
while True:
    seccion=input("Digite la seccion")
    secciones2.setdefault(seccion)
    print(secciones2)

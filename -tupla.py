import os
os.system("cls")
print("==============declarar tuplas===================")
tupla1=(["uno",["dos","tres"]],3,4,4,4,4,4,4,4,4,5,6,7,8,9)
tupla2=2,3,4,5,6,["sol","luna"]
tupla3=tupla1[0][1][1]
print(tupla3)
print("==============convertir lista en tupla===================")
lista=[["uno",["dos","tres"]],3,4,5,6,7,8,9]
tupla=tuple(lista)
print(tupla)
print("==============iterar una tupla===================")
for t in tupla1:
    print(t)
print("==============asignar valores===================")
l = (1, 2, 3)
x, y, z = l
print(x,y,z)
print("==============recorrer la tupla===================")
print(tupla1)
print(tupla2)
print(tupla1[1])
print(tupla1[0][0])
print(tupla1[0][1][0])
print(tupla1[1:9:2]) # recorrer del uno al nueve en saltos de dos
print("==============metodos de listas===================")
print(tupla1.index(5,2)) # posicion de un elemento y apartir de que pocision se empieza a buscar
print(tupla1.count(4)) # veces que se repite un elemento
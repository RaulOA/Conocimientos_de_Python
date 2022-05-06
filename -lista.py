import os
os.system("cls")

print("==============declarar lista===================")
lista=[["uno",["dos","tres"]],3,4,5,6,7,8,9,"diez"]
print("==============recorrer la lista===================")
print(lista)
print(lista[1])
print(lista[0][0])
print(lista[0][1][0])
print(lista[1:9:2]) # recorrer del uno al nueve en saltos de dos
print("==============iterar una lista===================")
for t in lista:
    print(t)
print("==============asignar valores===================")
l = [1, 2, 3]
x, y, z = l
print(x,y,z)
print("==============metodos de listas===================")
lista.extend((10,11,11,11,11,12,13,14)) # agregar una cantidad de elementos
lista.append([5,5]) # agregar un elemento
lista.remove(7) # remover un elemento
print(lista.index("diez",2)) # posicion de un elemento y apartir de que pocision se empieza a buscar
print(lista.count(11)) # veces que se repite un elemento
print(lista)
lista.reverse() # invertir los elementos
print(lista)
lista.sort()
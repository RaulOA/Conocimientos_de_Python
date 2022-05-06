import os
os.system("cls")

print("==============declarar diccionario===================")
diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }
diccionario["Apellido"]=["Ortega","Acuña"]
print(diccionario)
print("==============elementos===================")

# acceder a los elementos
print (diccionario['nombre'])
print (diccionario['edad'])
print (diccionario['cursos'])
print("==============lista dentro de diccionario===================")

# acceder a los elementos de la lista
print (diccionario['cursos'][0])
print (diccionario['cursos'][1])
print (diccionario['cursos'][2])
print("==============recorrer diccionario===================")

# recorrer todo el diccionario
for key in diccionario:
    print (key, ":", diccionario[key])
diccionario["cursos"][3]="Java"
print(diccionario)

# metodos de los diccionarios
print("==============dict ()===================")
# dict () Recibe como parámetro una representación de un diccionario y si es factible, devuelve un diccionario de datos.
dic1 =  dict(nombre='nestor', apellido='Plasencia', edad=22)
print(dic1)

print("===============zip()==================")
# zip() Recibe como parámetro dos elementos iterables, ya sea una cadena, una lista o una tupla. 
# Ambos parámetros deben tener el mismo número de elementos. 
# Se devolverá un diccionario relacionando el elemento i-esimo de cada uno de los iterables.
dic2 = dict(zip('abcd',[1,2,3,4]))
print(dic2)

print("===============items()==================")
# items() Devuelve una lista de tuplas, cada tupla se compone de dos elementos: 
# el primero será la clave y el segundo, su valor.
dic3 =   {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
items = dic3.items()
print(items)

print("===============keys()==================")
# keys() Retorna una lista de elementos, los cuales serán las claves de nuestro diccionario.
dic4 =  {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
keys= dic4.keys()
print(keys)

print("===============values()==================")
# values() Retorna una lista de elementos, que serán los valores de nuestro diccionario.
dic5 =  {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
values= dic5.values()
print(values)

print("===============clear()==================")
# clear() Elimina todos los ítems del diccionario dejándolo vacío.
dic6 =  {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
dic6.clear()
print(dic6)

print("===============copy()==================")
# copy() Retorna una copia del diccionario original.
dic7 =  {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
copy = dic7.copy()
print(copy)

print("===============fromkeys()==================")
# fromkeys() Recibe como parámetros un iterable y un valor, 
# devolviendo un diccionario que contiene como claves los elementos del iterable con el mismo valor ingresado. 
# Si el valor no es ingresado, devolverá none para todas las claves.
dic8 = dict.fromkeys(['a','b','c','d'],1)
print(dic8)

print("===============get()==================")
# get() Recibe como parámetro una clave, devuelve el valor de la clave. Si no lo encuentra, devuelve un objeto none.
dic9 = {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
valor = dic9.get("b")
print(valor)

print("===============pop()==================")
# pop() Recibe como parámetro una clave, elimina esta y devuelve su valor. Si no lo encuentra, devuelve error.
dic10 = {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
valor = dic10.pop("b") 
print (valor)
print(dic10)

print("===============setdefault()==================")
# setdefault() Funciona de dos formas. En la primera como get
dic11 = {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
valor2 = dic11.setdefault("a")
print(valor2)
# Y en la segunda forma, nos sirve para agregar un nuevo elemento a nuestro diccionario.
valor3 = dic11.setdefault("e",5)
print(valor3)
print(dic11)

print("===============update()==================")
# update() Recibe como parámetro otro diccionario. Si se tienen claves iguales, 
# actualiza el valor de la clave repetida; si no hay claves iguales, este par clave-valor es agregado al diccionario.
dic12 = {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
dic13 = {"c" : 6, "b" : 5, "e" : 9 , "f" : 10}
print(dic12)
dic12.update(dic13)
print(dic12)
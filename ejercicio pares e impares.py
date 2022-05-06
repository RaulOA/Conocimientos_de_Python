lista=[20,65,12,2,8,65,48,1,5,8]
pares=[]
impares=[]
for i in lista:
    if (i%2) == 1:
        impares.append(i)
    else:
        pares.append(i)
print("Numeros Pares: ",pares)
print("Numeros Impares",impares)
def fibonacci(lenght):
    n1=0
    n2=1
    lista=[n1,n2]
    for a in range(lenght):
        n3=n1+n2
        lista.append(n3)
        n1=n2
        n2=n3
    return(lista)
print(fibonacci(20))
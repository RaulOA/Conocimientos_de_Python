import os
os.system("cls")

# la clase es como un molde para crear objetos
class Galleta:
    pass
galleta_1=Galleta()
type(galleta_1)    #<class '__main__.Galleta'>
galleta_1.sabor="Salado"
galleta_1.color="Marron"
print("El sabor de esta galleta es",galleta_1.sabor,"y el color es",galleta_1.color)
#------------------------------------------------
class Automovil:
    pass
    arosDeLujo=False
carro_1=Automovil()
print(carro_1.arosDeLujo)
carro_1.arosDeLujo=True
print(carro_1.arosDeLujo)ç
#------------------------------------------------

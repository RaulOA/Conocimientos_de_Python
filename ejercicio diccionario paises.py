paises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", 
"Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", 
"Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", 
"Venezuela": "Caracas", "España": "Madrid"}

while True:
    print("Digite el pais")
    a=input()
    a=a.title()
    if a in paises.keys():
        b=paises[a]
        print("La capital del pais es:",b)
    else:
        print("El Pais no esta en la lista")
jugadores = {1 : "Casillas", 15 : "Ramos",

3 : "Pique", 5 : "Puyol",

11 : "Capdevila", 14 : "Xabi Alonso",

16 : "Busquets", 8 : "Xavi Hernandez",

18 : "Pedrito", 6 : "Iniesta",

7 : "Villa"}

while True:
    print("Digite el # del Jugador")
    a=int(input())
    if a in jugadores.keys():
        b=jugadores[a]
        print("El nombre del Jugador es:",b)
    else:
        print("El Jugador no esta en la lista")
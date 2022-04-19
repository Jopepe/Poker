from difflib import restore
from gzip import READ
from itertools import count
from multiprocessing.sharedctypes import RawArray
import random as rad

Oros = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
Bastos = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
Espadas = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
Copas = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
i = 0
Ases = 0
Reyes = 0
Sota = 0
Caballo = 0
Resto = 0
intentos = 500000
Baraja = Oros + Bastos + Espadas + Copas
while True:
    print(" \n [A]As [K]K [Q]Q [J]J [10]\n [9]9  [8]8 [7]7 [6]6 [5]5\n [4]4  [3]3 [2]2 [Salir]Salir\n [Enter]Probabilides actuales\n [Reset]Reiniciar Baraja\n")
    c = input("¿Que carta ha salido?(Sin palo)\n")
    c = c.upper()

    if c in Baraja:
        Baraja.remove(c)
    if c == "RESET":
        Baraja = Oros + Bastos + Espadas + Copas
    if c == "SALIR":
        break
    else:
        i = 0
    Ases = 0
    Reyes = 0
    Sota = 0
    Caballo = 0
    Diez = 0
    Nueve = 0
    Ocho = 0
    Siete = 0
    Seis = 0
    Cinco = 0
    Cuatro = 0
    Tres = 0
    Dos = 0
    Resto = 0
    while i < intentos:
        a = Baraja[rad.randint(0, len(Baraja) - 1)]
        if a == "A":
            Ases += 1
        elif a == "K":
            Reyes += 1
        elif a == "Q":
            Caballo += 1
        elif a == "J":
            Sota += 1
        elif a == "10":
            Diez += 1
            Resto += 1
        elif a == "9":
            Nueve += 1
            Resto += 1
        elif a == "8":
            Ocho += 1
            Resto += 1
        elif a == "7":
            Siete += 1
            Resto += 1
        elif a == "6":
            Seis += 1
            Resto += 1
        elif a == "5":
            Cinco += 1
            Resto += 1
        elif a == "4":
            Cuatro += 1
            Resto += 1
        elif a == "3":
            Tres += 1
            Resto += 1
        elif a == "2":
            Dos += 1
            Resto += 1
        i += 1
        
    
    print("------------------------------------------------------")
    print("A: ", Baraja.count("A"), "(",round((Ases/intentos*100), 1), "%)")
    print("K: ", Baraja.count("K"),"(",round((Reyes/intentos*100), 1), "%)")
    print("Q: ", Baraja.count("Q"),"(",round((Caballo/intentos*100),1), "%)")
    print("J: ", Baraja.count("J"),"(",round((Sota/intentos*100),1), "%)")
    print("10:", Baraja.count("10"),"(",round((Diez/intentos*100),1), "%)")
    print("9: ", Baraja.count("9"),"(",round((Nueve/intentos*100),1), "%)")
    print("8: ", Baraja.count("8"),"(",round((Ocho/intentos*100),1), "%)")
    print("7: ", Baraja.count("7"),"(",round((Siete/intentos*100),1), "%)")
    print("6: ", Baraja.count("6"),"(",round((Seis/intentos*100),1), "%)")
    print("5: ", Baraja.count("5"),"(",round((Cinco/intentos*100),1), "%)")
    print("4: ", Baraja.count("4"),"(",round((Cuatro/intentos*100),1), "%)")
    print("3: ", Baraja.count("3"),"(",round((Tres/intentos*100),1), "%)")
    print("2: ", Baraja.count("2"),"(",round((Dos/intentos*100),1), "%)")
    print("------------------------------------------------------")

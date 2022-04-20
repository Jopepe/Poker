import random as rad

Corazones = ["AC", "KC", "QC", "JC", "10C", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C"]
Trebol = ["AT", "KT", "QT", "JT", "10T", "9T", "8T", "7T", "6T", "5T", "4T", "3T", "2T"]
Picas = ["AP", "KP", "QP", "JP", "10P", "9P", "8P", "7P", "6P", "5P", "4P", "3P", "2P"]
Rombos = ["AR", "KR", "QR", "JR", "10R", "9R", "8R", "7R", "6R", "5R", "4R", "3R", "2R"]
i = 0
Ases = 0
Reyes = 0
Sota = 0
Caballo = 0
Resto = 0
intentos = 500000
Baraja = Corazones + Trebol + Picas + Rombos
while True:
    print(" \n [A]As [K]K [Q]Q [J]J [10]\n [9]9  [8]8 [7]7 [6]6 [5]5\n [4]4  [3]3 [2]2 [Salir]Salir\n [Enter]Probabilides actuales\n [Reset]Reiniciar Baraja\n")
    c = input("¿Que carta ha salido?(Indicar palo con inicial. Ej: 10 de rombos = 10R)\n")
    c = c.upper()

    if c in Baraja:
        Baraja.remove(c)
    if c == "RESET":
        Baraja = Corazones + Trebol + Picas + Rombos
    if c == "SALIR":
        break
    if c == "SUP":
        print(Baraja)
    else:
        i = 0
    Ases, Reyes, Sota, Caballo, Diez, Nueve, Ocho, Siete, Seis, Cinco, Cuatro, Tres, Dos, Resto = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    while i < intentos:
        a = Baraja[rad.randint(0, len(Baraja) - 1)]
        
        if a[0] == "A":
            Ases += 1
        elif a[0] == "K":
            Reyes += 1
        elif a[0] == "Q":
            Caballo += 1
        elif a[0] == "J":
            Sota += 1
        elif a[0] == "1" and a[1] == "0":
            Diez += 1
            Resto += 1
        elif a[0] == "9":
            Nueve += 1
            Resto += 1
        elif a[0] == "8":
            Ocho += 1
            Resto += 1
        elif a[0] == "7":
            Siete += 1
            Resto += 1
        elif a[0] == "6":
            Seis += 1
            Resto += 1
        elif a[0] == "5":
            Cinco += 1
            Resto += 1
        elif a[0] == "4":
            Cuatro += 1
            Resto += 1
        elif a[0] == "3":
            Tres += 1
            Resto += 1
        elif a[0] == "2":
            Dos += 1
            Resto += 1
        i += 1        
    ''''
    num_10 = Baraja.count("10C") + Baraja.count("10T") + Baraja.count("10P") + Baraja.count("10R")
    num_9 = Baraja.count("9C") + Baraja.count("9T") + Baraja.count("9P") + Baraja.count("9R")
    num_8 = Baraja.count("8C") + Baraja.count("8T") + Baraja.count("8P") + Baraja.count("8R")
    num_7 = Baraja.count("7C") + Baraja.count("7T") + Baraja.count("7P") + Baraja.count("7R")
    num_6 = Baraja.count("6C") + Baraja.count("6T") + Baraja.count("6P") + Baraja.count("6R")
    num_5 = Baraja.count("5C") + Baraja.count("5T") + Baraja.count("5P") + Baraja.count("5R")
    num_4 = Baraja.count("4C") + Baraja.count("4T") + Baraja.count("4P") + Baraja.count("4R")
    num_3 = Baraja.count("3C") + Baraja.count("3T") + Baraja.count("3P") + Baraja.count("3R")
    num_2 = Baraja.count("2C") + Baraja.count("2T") + Baraja.count("2P") + Baraja.count("2R")
    num_A = Baraja.count("AC") + Baraja.count("AT") + Baraja.count("AP") + Baraja.count("AR")
    num_Q = Baraja.count("QC") + Baraja.count("QT") + Baraja.count("QP") + Baraja.count("QR")
    num_K = Baraja.count("KC") + Baraja.count("KT") + Baraja.count("KP") + Baraja.count("KR")
    num_J = Baraja.count("JC") + Baraja.count("JT") + Baraja.count("JP") + Baraja.count("JR")
    '''
    num_A, num_K, num_Q, num_J, num_10, num_9, num_8, num_7, num_6, num_5, num_4, num_3, num_2 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for i in Baraja:
        if i[0] == "A":
            num_A += 1
        elif i[0] == "K":
            num_K += 1
        elif i[0] == "Q":
            num_Q += 1
        elif i[0] == "J":
            num_J += 1
        elif i[0] == "1" and i[1] == "0":
            num_10 += 1
        elif i[0] == "9":
            num_9 += 1
        elif i[0] == "8":
            num_8 += 1
        elif i[0] == "7":
            num_7 += 1
        elif i[0] == "6":
            num_6 += 1
        elif i[0] == "5":
            num_5 += 1
        elif i[0] == "4":
            num_4 += 1
        elif i[0] == "3":
            num_3 += 1
        elif i[0] == "2":
            num_2 += 1
                
    print("------------------------------------------------------")
    print("A: ", num_A, "(",round((Ases/intentos*100), 1), "%)")
    print("K: ", num_K,"(",round((Reyes/intentos*100), 1), "%)")
    print("Q: ", num_Q,"(",round((Caballo/intentos*100),1), "%)")
    print("J: ", num_J,"(",round((Sota/intentos*100),1), "%)")
    print("10:", num_10,"(",round((Diez/intentos*100),1), "%)")
    print("9: ", num_9,"(",round((Nueve/intentos*100),1), "%)")
    print("8: ", num_8,"(",round((Ocho/intentos*100),1), "%)")
    print("7: ", num_7,"(",round((Siete/intentos*100),1), "%)")
    print("6: ", num_6,"(",round((Seis/intentos*100),1), "%)")
    print("5: ", num_5,"(",round((Cinco/intentos*100),1), "%)")
    print("4: ", num_4,"(",round((Cuatro/intentos*100),1), "%)")
    print("3: ", num_3,"(",round((Tres/intentos*100),1), "%)")
    print("2: ", num_2,"(",round((Dos/intentos*100),1), "%)")
    print("Cartas bajas: ", (len(Baraja) - num_A) -num_K - num_Q - num_J,"(",round((Resto/intentos*100),1), "%)")
    print("------------------------------------------------------")

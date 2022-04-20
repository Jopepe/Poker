import random

contador_jugadas = [0] * 11
partidas = 1000000
num_palos = 4
num_valores = 13
cartas_en_mano = 5

def CrearBaraja(num_palos, num_valores):
    baraja = []
    i, j = 0, 0
    while(i < num_palos):
        while(j < num_valores):
            baraja.append([i, j])
            j += 1
        i += 1
        j = 0
    return baraja

def RepartirMano(baraja, cartas_en_mano):
    a = []
    for i in range(cartas_en_mano):
        b = random.choice(baraja)
        a.append(b)
        baraja.remove(b)
    return a

def ObtenerContadorValores(mano, num_valores):
    j = 0
    a = []
    for i in mano:
        a.append(mano[j][1])
        j+=1
    repeticiones = {}
    for n in a:
        if n in repeticiones:
            repeticiones[n] += 1
        else:
            repeticiones[n] = 0
    a = []
    j = 0
    b = list(repeticiones.values())
    for i in b:
        a.append(b[j]+1)
        j += 1
    return a

def ObtenerMaximos(contador_valores):
    contador_valores.sort(reverse=True)
    return contador_valores[0], contador_valores[1]

def ObtenerJugadaMano(max1, max2):
    if(max1 == 4):
        return 0
    elif(max1 == 3 and max2 == 2):
        return 1
    elif(max1 == 3):
        return 2
    elif(max1 == 2 and max2 == 2):
        return 3
    elif(max1 == 2):
        return 4
    else:
        return 5

def ImprimirPobabilidades(contador_jugadas, partidas):
    print("Numero de manos: ", partidas)
    print("Póker: ", (contador_jugadas[0]/partidas*100))
    print("Full: ", (contador_jugadas[1]/partidas*100))
    print("Trío: ", (contador_jugadas[2]/partidas*100))
    print("Doble Pareja: ", (contador_jugadas[3]/partidas*100))
    print("Pareja: ", (contador_jugadas[4]/partidas*100))
    print("Carta alta: ", (contador_jugadas[5]/partidas*100))

for i in range(partidas):
    baraja = CrearBaraja(num_palos, num_valores)
    mano = RepartirMano(baraja, cartas_en_mano)
    contador_valores = ObtenerContadorValores(mano, num_valores)
    max1, max2 = ObtenerMaximos(contador_valores)
    jugada = ObtenerJugadaMano(max1, max2)
    contador_jugadas[jugada] += 1
ImprimirPobabilidades(contador_jugadas, partidas)
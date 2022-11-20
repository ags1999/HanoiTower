import musicalbeeps


pinoA = [0, 1, 2, 3, 4]
pinoB = []
pinoC = []

player = musicalbeeps.Player(0.3, False)

notas = {
    0: "C",
    1: "D",
    2: "E",
    3: "F",
    4: "G",
    5: "A",
    6: "B",
}

def ImprimePinos():
    print("Pino A = " + str(pinoA))
    print("Pino B = " + str(pinoB))
    print("Pino C = " + str(pinoC))
    print("/////////////////////////////////////////////////")



def HanoiRecursivo(n, inicial, final, aux):
    if n > 0:
        HanoiRecursivo(n-1, inicial, aux, final)
        disco = inicial.pop()
        final.append(disco)
        player.play_note(notas[disco], 0.2)
        ImprimePinos()
        HanoiRecursivo(n-1, aux, final, inicial)
    return


def mv_aux(p1, p2):
    disco = p1.pop(0)
    player.play_note(notas[disco], 0.2)
    p2.insert(0, disco)

def movimento(Pino1, Pino2):
    if(len(Pino1) == 0 and len(Pino2) == 0):
        return 0
    elif(len(Pino1) == 0):
        mv_aux(Pino2, Pino1)
    elif(len(Pino2) == 0):
        mv_aux(Pino1, Pino2)
    else:
        if(Pino1[0] > Pino2[0]):
            mv_aux(Pino2, Pino1)
        else:
            mv_aux(Pino1, Pino2)
    return 1

def HanoiIterativo(n, inicial, final, aux):
    nummv = 0
    prox = 1
    while(len(final) != n):
        if(n%2 == 0):
            match prox:
                case 1:
                    nummv += movimento(inicial, aux)
                    prox = 2
                    continue
                
                case 2:
                    nummv += movimento(inicial, final)
                    prox = 3
                    continue
                case 3:
                    nummv += movimento(aux, final)
                    prox = 1
                    continue
        else:
            match prox:
                case 1:
                    nummv += movimento(inicial, final)
                    prox = 2
                    continue
                
                case 2:
                    nummv += movimento(inicial, aux)
                    prox = 3
                    continue
                case 3:
                    nummv += movimento(aux, final)
                    prox = 1
                    continue

    return nummv


#HanoiRecursivo(len(pinoA), pinoA, pinoC, pinoB)
#print(pinoC)



nm = HanoiIterativo(len(pinoA), pinoA, pinoC, pinoB)
print("Numero de movimentos = " + str(nm))
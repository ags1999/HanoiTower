import musicalbeeps


pinoA = [0, 1, 2, 3]
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





HanoiRecursivo(len(pinoA), pinoA, pinoC, pinoB)
print(pinoC)



#nm = Hanoi2(pinoA, pinoB, pinoC)
#print("Numero de movimentos = " + str(nm))
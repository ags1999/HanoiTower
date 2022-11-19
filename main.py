import musicalbeeps


pinoA = [0, 1, 2, 3, 4, 5]
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



def Hanoi1(n, inicial, final, aux):
    if n > 0: 
        Hanoi1(n-1, inicial, final, aux)
        if inicial:
            disco = inicial.pop()
            player.play_note(notas[disco], 0.2)
            final.append(disco)
        Hanoi1(n-1, aux, inicial, final)

    return


#Não está pronta
def Hanoi2():
    while(len(pinoA) != 0):
        if(len(pinoA)%2 != 0):

            disco = pinoA.pop(0)
            player.play_note(notas[disco], 0.2)
            pinoB.insert(0, disco)

            disco = pinoA.pop(0)
            player.play_note(notas[disco], 0.2)
            pinoC.insert(0, disco)

            disco = pinoB.pop(0)
            player.play_note(notas[disco], 0.2)
            pinoC.insert(0, disco)
        else:
            disco = pinoA.pop(0)
            player.play_note(notas[disco], 0.2)
            pinoC.insert(0, disco)

            disco = pinoA.pop(0)
            player.play_note(notas[disco], 0.2)
            pinoB.insert(0, disco)

            disco = pinoB.pop(0)
            player.play_note(notas[disco], 0.2)
            pinoC.insert(0, disco)

    return

#Hanoi1(len(pinoA), pinoA, pinoB, pinoC)
Hanoi2()
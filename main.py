import musicalbeeps

pinoA = [0, 1, 2]
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


def TorreDeHanoi(inicial, final, aux):
    if len(inicial) == 0:
        return
    disco = inicial.pop(0)

    player.play_note(notas[disco], 0.2)
    TorreDeHanoi(inicial, aux, final)
    final.insert(0, disco)
    TorreDeHanoi(aux, final, inicial)

    return


TorreDeHanoi(pinoA, pinoB, pinoC)

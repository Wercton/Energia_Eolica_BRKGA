import Selecao
import random


def produzir_filho(elite, nao_elite):

    pai1 = Selecao.escolher_pai(elite)
    pai2 = Selecao.escolher_pai(nao_elite)

    filho = []

    for i in range(len(pai1)):

        if random.random() > 0.5:
            filho.append(pai1[i])
        else:
            filho.append(pai2[i])

    return filho

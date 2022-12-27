import Selecao, Funcao_fitness
import random


def produzir_filho(elite, nao_elite):

    while True:
        pai1 = Selecao.escolher_pai(elite)
        pai2 = Selecao.escolher_pai(nao_elite)
        if pai1 != pai2:
            break

    filho = []

    fit1 = Funcao_fitness.fitness(pai1)
    fit2 = Funcao_fitness.fitness(pai2)
    
    if fit2 > fit1:
        pai1, pai2 = pai2, pai1
    
    for i in range(len(pai1)):

        if random.random() < 0.7:
            filho.append(pai1[i])
        else:
            filho.append(pai2[i])

    return filho

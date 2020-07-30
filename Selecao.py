import numpy as np
import sys


def separar_elite(populacao, fitness_populacao):

    elite, nao_elite = [], []

    fitness_lista = [fitness_populacao[i][0] for i in range(len(fitness_populacao))]
    fitness_lista = list(enumerate(fitness_lista))
    fitness_lista = sorted(fitness_lista, key=lambda x: x[1], reverse=True)

    for i in range((len(populacao)//2) - 1):
        indice = fitness_lista[i][0]
        elite.append(populacao[indice])
        np.delete(populacao, indice)

    for i in range(len(populacao)):
        nao_elite.append(populacao[i])

    return elite, nao_elite


def escolher_pai(grupo):
    pass

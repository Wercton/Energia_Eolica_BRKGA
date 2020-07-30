import random
import numpy as np
import Funcao_fitness


'''PartLim=[[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],
[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],
[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],
[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],
[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],
[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],
[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],
[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],
[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]],[[0.3, -0.03],[0.2, 0.05]]]'''


'''ind1=[0.35 0.157 0.324 0.153 0.3 0.149 0.277 0.146 0.257 0.142 0.238 0.137 0.220 0.133 0.204 0.130 0.189 0.126 0.175
      0.122 0.161 0.118 0.149 0.115 0.138 0.112 0.127 0.108 0.117 0.105 0.107 0.102 0.098 0.1 0.090 0.097 0.082 0.094
      0.075 0.092 0.068 0.090 0.061 0.087 0.055 0.085 0.049 0.083 0.043 0.081 0.037 0.079 0.032 0.078 0.027 0.076 0.
      0.074 0.018 0.073 0.014 0.071 0.010 0.070 0.006 0.068 0.002 0.067 -0.002 0.066 -0.005 0.064 -0.009 0.063 -0.012
      0.062 -0.015 0.061 -0.018 0.060 -0.021 0.059 -0.024 0.058 -0.026 0.057 -0.029 0.056 -0.032 0.055 -0.034 0.054
      -0.036 0.053 -0.039 0.052 -0.041 0.051 -0.043 0.050];'''


def criar_populacao(individuos, genes, nova=False):

    limites_cromossomo = [[[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]],
               [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03],
                                                                          [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]],
               [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]],
               [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03],
                                             [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]],
               [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03],
                                                                                                       [0.2, 0.05]],
               [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]],
               [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03],
                                                                          [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]],
               [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]],
               [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03],
                                             [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]],
               [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03],
                                                                                                       [0.2, 0.05]],
               [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]],
               [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03],
                                                                          [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]],
               [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]],
               [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03],
                                             [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]], [[0.3, -0.03], [0.2, 0.05]]]

    populacao = []

    for _ in range(individuos):
        cromossomo = []
        for i in range(genes):
            x = round(random.uniform(limites_cromossomo[i][0][0], limites_cromossomo[i][0][1]), 2)
            y = round(random.uniform(limites_cromossomo[i][1][0], limites_cromossomo[i][1][1]), 2)
            cromossomo.append([x, y])
        populacao.append([cromossomo])
    if nova:
        populacao = np.squeeze(np.asanyarray(populacao))  # convertendo listas em array somente se for uma nova,

    return populacao


def geral_fitness(populacao):
    todos_fitness = []

    for i in range(len(populacao)):
        todos_fitness.append(Funcao_fitness.fitness(populacao[i]))

    return todos_fitness


def gerar_conjunto_mutante(quantidade):
    pass
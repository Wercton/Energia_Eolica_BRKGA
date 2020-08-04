import random


def separar_elite(populacao, fitness_populacao):

    elite, nao_elite = [], []

    fitness_lista = [fitness_populacao[i][0] for i in range(len(fitness_populacao))]
    fitness_lista = list(enumerate(fitness_lista))
    fitness_lista = sorted(fitness_lista, key=lambda x: x[1])

    for i in range((len(populacao)//4)):
        indice = fitness_lista.pop()
        cromossomo = populacao[indice[0]]
        fitness_cromossomo = indice[1]
        elite.append([cromossomo, fitness_cromossomo])  # (membro, fitness) otimizar escolha dos pais -- OK

    for i in range(len(fitness_lista)):
        indice = fitness_lista.pop()
        nao_elite.append((populacao[indice[0]], indice[1]))  # pensar em uma maneira de nao-elite tambem receber -- OK

    return elite, nao_elite


def escolher_pai(grupo):

    total = sum([i[1] for i in grupo])
    pick = random.uniform(0, total)
    acumulo = 0
    for cromossomo in grupo:
        acumulo += cromossomo[1]
        if acumulo > pick:
            return cromossomo[0]

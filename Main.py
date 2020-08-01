import random
import matplotlib.pyplot as plt
import sys
import numpy as np  # ???
import Populacao
import Selecao
import Reproducao


def brkga(individuos, genes, geracao, mutantes_quantidade):

    melhor_solucao_geral = [0, 0]

    for _ in range(1):

        populacao = Populacao.criar_populacao(individuos, genes, nova=True)

        for geracao_atual in range(geracao):

            populacao = np.squeeze(np.asanyarray(populacao))  # transforma população em array numpy
            fitness_populacao = Populacao.geral_fitness(populacao)
            populacao = populacao.tolist()  # torna o array lista outra vez

            elite, nao_elite = Selecao.separar_elite(populacao, fitness_populacao)  # retornando alguns arrays em listas

            nova_populacao, populacao = [], []  # reinicio populacao que não será mais usada
            [nova_populacao.append(cromossomo[0]) for cromossomo in elite]  # elite vem com enumeracao do fitness
            melhor_solucao_geracao = elite[0]

            mutante = Populacao.criar_populacao(mutantes_quantidade, genes)
            [nova_populacao.append(*cromossomo) for cromossomo in mutante]

            for _ in range(individuos - len(nova_populacao)):

                nova_populacao.append(Reproducao.produzir_filho(elite, nao_elite))

            [populacao.append(cromossomo) for cromossomo in nova_populacao]

            exibir_dados(geracao_atual, melhor_solucao_geracao)

            if melhor_solucao_geracao[1] > melhor_solucao_geral[1]:
                melhor_solucao_geral = melhor_solucao_geracao

    return melhor_solucao_geral


def exibir_dados(geracao, melhor_solucao_geracao):
    print("Geração", geracao, "-" * 100)
    print("Melhor solução:", melhor_solucao_geracao[1])


if __name__ == '__main__':

    melhor_solucao = brkga(individuos=10, genes=50, geracao=5, mutantes_quantidade=2)

    print("\n\nFitness do melhor indíviduo encontrado:", melhor_solucao[1])
    print("Indivíduo: ", *[i for i in melhor_solucao[0]], sep="\n")

import random
import sys
import numpy  # ???
import Populacao
import Selecao


def brkga(individuos, genes, geracao, mutantes_quantidade):

    melhor_solucao_geral = 0

    for _ in range(geracao):

        populacao = Populacao.criar_populacao(individuos, genes, nova=True)
        print(populacao)

        for _ in range(geracao):

            fitness_populacao = Populacao.geral_fitness(populacao)
            elite, nao_elite = Selecao.separar_elite(populacao, fitness_populacao)  # retornando alguns arrays em listas
            nova_populacao = elite
            mutante = Populacao.criar_populacao(mutantes_quantidade, genes)
            nova_populacao += mutante

            for _ in range(individuos - len(nova_populacao)):

                pai1 = escolher_pai(elite)
                pai2 = escolher_pai(nao_elite)
                filho = [[(0, 0) for _ in range(genes)]]

                for i in range(genes):

                    if random.random() > 0.5:
                        filho[i] = pai1[i]
                    else:
                        filho[i] = pai2[i]

                nova_populacao += filho

            populacao = nova_populacao()
            melhor_solucao_geracao = max(fitness_populacao)

            if melhor_solucao_geracao > melhor_solucao_geral:
                melhor_solucao_geral = melhor_solucao_geracao

    return melhor_solucao_geral


if __name__ == '__main__':
    print(brkga(individuos=10, genes=50, geracao=2, mutantes_quantidade=2))

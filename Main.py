import random
import sys
import numpy as np  # ???
import Populacao
import Selecao


def brkga(individuos, genes, geracao, mutantes_quantidade):

    melhor_solucao_geral = 0

    for _ in range(1):

        populacao = Populacao.criar_populacao(individuos, genes, nova=True)
        print(populacao)
        print(len(populacao))

        for _ in range(geracao):

            populacao = np.squeeze(np.asanyarray(populacao))
            fitness_populacao = Populacao.geral_fitness(populacao)
            print('-' * 100)
            populacao = populacao.tolist()

            nova_populacao = []
            elite, nao_elite = Selecao.separar_elite(populacao, fitness_populacao)  # retornando alguns arrays em listas
            [nova_populacao.append(cromossomo[0]) for cromossomo in elite]  # elite tem que vir com enumeracao do fitness

            mutante = Populacao.criar_populacao(mutantes_quantidade, genes)
            [nova_populacao.append(*cromossomo) for cromossomo in mutante]

            for _ in range(individuos - len(nova_populacao)):

                pai1 = Selecao.escolher_pai(elite)
                pai2 = Selecao.escolher_pai(nao_elite)

                #print("\nPai1:", pai1)
                #print("Pai2:", pai2, end="\n")

                filho = []

                for i in range(len(pai1)):

                    if random.random() > 0.5:
                        filho.append(pai1[i])
                    else:
                        filho.append(pai2[i])

                #print("Filho:", filho)

                nova_populacao.append(filho)

            populacao = []
            [populacao.append(cromossomo) for cromossomo in nova_populacao]


            melhor_solucao_geracao = max(fitness_populacao)
            print(melhor_solucao_geracao)

            if melhor_solucao_geracao > melhor_solucao_geral:
                melhor_solucao_geral = melhor_solucao_geracao

    return melhor_solucao_geral


if __name__ == '__main__':
    print(brkga(individuos=10, genes=50, geracao=20, mutantes_quantidade=2))

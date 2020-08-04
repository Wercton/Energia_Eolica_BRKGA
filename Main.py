import matplotlib.pyplot as plt
import warnings
import numpy as np
import Populacao
import Selecao
import Reproducao

plt.style.use('dark_background')
warnings.filterwarnings('ignore', 'The iteration is not making good progress')


def brkga(individuos, genes, geracao, mutantes_quantidade):

    melhor_solucao_geral = [0, 0]
    melhores_solucoes = []

    for _ in range(1):

        populacao = Populacao.criar_populacao(individuos, genes, nova=True)

        for geracao_atual in range(geracao):

            print(".")

            populacao = np.squeeze(np.asanyarray(populacao))  # transforma população em array numpy
            fitness_populacao = Populacao.geral_fitness(populacao)
            populacao = populacao.tolist()  # torna o array lista outra vez

            elite, nao_elite = Selecao.separar_elite(populacao, fitness_populacao)

            populacao = []  # reinicio populacao para reutilizar como nova populacao
            [populacao.append(cromossomo[0]) for cromossomo in elite]  # elite vem com enumeracao do fitness
            melhor_solucao_geracao = elite[0]

            mutante = Populacao.criar_populacao(mutantes_quantidade, genes)
            [populacao.append(*cromossomo) for cromossomo in mutante]

            for _ in range(individuos - len(populacao)):

                populacao.append(Reproducao.produzir_filho(elite, nao_elite))

            exibir_dados(geracao_atual, melhor_solucao_geracao)

            if melhor_solucao_geracao[1] > melhor_solucao_geral[1]:
                melhor_solucao_geral = melhor_solucao_geracao

            melhores_solucoes.append(melhor_solucao_geral[1])
            plt.plot(melhor_solucao_geral[1], geracao_atual)

    print("\n\nFitness do melhor indíviduo encontrado:", melhor_solucao_geral[1])
    print("Indivíduo: ", [i for i in melhor_solucao_geral[0]], sep="\n")

    plt.plot(melhores_solucoes)
    fig1 = plt.gcf()
    plt.show()
    plt.draw()
    fig1.savefig('demo.png', transparent=True)


def exibir_dados(geracao, melhor_solucao_geracao):
    print("Geração", geracao, "-" * 100)
    print("Melhor solução:", melhor_solucao_geracao[1])
    if melhor_solucao_geracao[1] > 800:
        print(melhor_solucao_geracao[0])


if __name__ == '__main__':

    try:
        brkga(individuos=20, genes=50, geracao=100, mutantes_quantidade=4)
    except Exception as e:
        print("Error Code:", e)

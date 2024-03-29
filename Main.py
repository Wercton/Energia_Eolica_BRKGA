import matplotlib.pyplot as plt
from warnings import filterwarnings
import numpy as np
import Populacao
import Selecao
import Reproducao
from Brkga import BRKGA
import Funcao_fitness

filterwarnings('ignore', 'The iteration is not making good progress')

code = 0


def brkga(individuos, genes, geracao, mutantes_quantidade):

    melhor_solucao_geral = [0, 0]
    melhores_solucoes = []

    for _ in range(1):

        populacao = Populacao.criar_populacao(individuos, genes)

        for geracao_atual in range(geracao):
            # print(geracao_atual)
            populacao = np.squeeze(np.asanyarray(populacao))  # transforma população em array numpy
            fitness_populacao = Populacao.geral_fitness(populacao)
            populacao = populacao.tolist()  # torna o array lista outra vez

            elite, nao_elite = Selecao.separar_elite(populacao, fitness_populacao)

            populacao = []  # reinicio populacao para reutilizar como nova populacao
            [populacao.append(cromossomo[0]) for cromossomo in elite]  # elite vem com enumeracao do fitness
            melhor_solucao_geracao = elite[0]

            mutante = Populacao.criar_populacao(mutantes_quantidade, genes)
            [populacao.append(*cromossomo) for cromossomo in mutante]
            
            populacao_completa = elite + nao_elite
            for _ in range(individuos - len(populacao)):
                # RKGA
                populacao.append(Reproducao.produzir_filho(populacao_completa, populacao_completa))
                # BRKGA
                # populacao.append(Reproducao.produzir_filho(elite, populacao_completa))

            # exibir_dados(geracao_atual, melhor_solucao_geracao)
            print(geracao_atual, end=" ")

            if melhor_solucao_geracao[1] > melhor_solucao_geral[1]:
                melhor_solucao_geral = melhor_solucao_geracao

            melhores_solucoes.append(melhor_solucao_geral[1])
            
            print(f'{geracao_atual} - {melhor_solucao_geral[1]}')

    print("\n\nFitness do melhor indíviduo encontrado:", melhor_solucao_geral[1])
    print("Indivíduo: ", [i for i in melhor_solucao_geral[0]], sep="\n\n")

    plottar_grafico(melhores_solucoes, individuos, mutantes_quantidade)


def exibir_dados(geracao, melhor_solucao_geracao):
    print("Geração", geracao, "-" * 100)
    print("Melhor solução:", melhor_solucao_geracao[1])


def plottar_grafico(melhores_solucoes, individuos, mutantes_quantidade):

    global code

    plt.plot([i for i in range(1, len(melhores_solucoes) + 1)], melhores_solucoes)
    plt.xlabel("Número de gerações")
    plt.ylabel("Potência (W)")
    plt.title("Curva de Convergência - BRKGA")

    fig1 = plt.gcf()
    # plt.show()
    plt.draw()
    nome_arquivo = "graficos/conv" + str(individuos) + "indiv" + str(mutantes_quantidade) + "mut" + "_Pcode" + str(code)
    # fig1.savefig(nome_arquivo + "tran", transparent=True)  # para salvar fig sem background
    fig1.savefig(nome_arquivo)
    plt.cla()

    code += 1


if __name__ == '__main__':
    for _ in range(1):
        brkga(individuos=50, genes=50, geracao=500, mutantes_quantidade=4)
    

    # brkga = BRKGA(generations=100, individuos=50, genes=50, qtd_mutations=4)
    # brkga.plottar_grafico()
    # brkga.gerar_relatorio()
    
    # Funcao_fitness.main()
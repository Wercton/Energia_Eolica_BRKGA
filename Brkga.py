import matplotlib.pyplot as plt
import numpy as np
from random import uniform, random
from Funcao_fitness import fitness

from os import listdir
from os.path import isfile, join

class BRKGA:

    def __init__(self, generations=10, individuos=50, genes=50, qtd_mutations=3):
        self.generations = generations
        self.individuos = individuos
        self.genes = genes
        self.qtd_mutations = qtd_mutations
        self.melhor_solucao_geral = [0, 0]
        self.melhor_solucao_geracao = []
        self.melhores_solucoes = []
        self.versao = self.get_grafico_id()
        
        self.run()

    def run(self):
        self.populacao = []
        self.inicializar_valores()
        
        # self.populacao.append([[[0.26, 0.14], [0.26, 0.05], [0.02, 0.13], [0.2, 0.09], [0.18, 0.14], [0.26, 0.14], [0.12, 0.06], [0.26, 0.11], [-0.02, 0.1], [0.24, 0.17], [0.16, 0.17], [0.01, 0.18], [0.05, 0.13], [0.27, 0.08], [0.08, 0.14], [0.25, 0.09], [0.28, 0.17], [0.01, 0.09], [0.06, 0.19], [0.22, 0.06], [0.21, 0.14], [0.22, 0.1], [-0.02, 0.13], [0.08, 0.16], [0.21, 0.11], [0.04, 0.08], [0.16, 0.1], [0.16, 0.19], [0.03, 0.16], [0.09, 0.13], [0.1, 0.11], [0.26, 0.06], [0.05, 0.13], [0.07, 0.1], [0.18, 0.1], [0.18, 0.15], [0.18, 0.2], [-0.03, 0.07], [0.11, 0.14], [-0.01, 0.1], [0.2, 0.1], [0.03, 0.19], [-0.02, 0.17], [-0.01, 0.19], [0.1, 0.08], [0.09, 0.07], [0.05, 0.13], [0.06, 0.2], [0.06, 0.12], [0.11, 0.2]]])
        # self.populacao.append([[[0.23, 0.16], [0.22, 0.17], [0.14, 0.06], [0.12, 0.06], [0.15, 0.08], [0.12, 0.08], [0.25, 0.14], [0.28, 0.08], [0.24, 0.14], [0.21, 0.15], [0.23, 0.17], [0.28, 0.1], [0.17, 0.18], [0.09, 0.16], [0.2, 0.16], [0.15, 0.19], [0.27, 0.18], [0.28, 0.07], [0.3, 0.12], [0.17, 0.17], [0.19, 0.2], [0.22, 0.19], [0.2, 0.2], [0.21, 0.16], [0.11, 0.19], [0.16, 0.18], [0.23, 0.16], [0.05, 0.15], [0.07, 0.09], [0.1, 0.14], [0.03, 0.16], [0.06, 0.12], [0.1, 0.19], [0.12, 0.15], [0.05, 0.2], [0.1, 0.19], [0.07, 0.14], [0.07, 0.16], [-0.01, 0.19], [-0.02, 0.16], [0.09, 0.19], [0.07, 0.18], [0.05, 0.18], [0.01, 0.1], [0.04, 0.18], [-0.03, 0.19], [-0.01, 0.18], [0.08, 0.19], [0.06, 0.19], [0.05, 0.07]]])
        self.populacao.append([[[0.26, 0.14], [0.26, 0.05], [0.02, 0.13], [0.2, 0.09], [0.18, 0.14], [0.26, 0.14], [0.12, 0.06], [0.26, 0.11], [-0.02, 0.1], [0.24, 0.17], [0.16, 0.17], [0.01, 0.18], [0.05, 0.13], [0.27, 0.08], [0.08, 0.14], [0.25, 0.09], [0.28, 0.17], [0.01, 0.09], [0.06, 0.19], [0.22, 0.06], [0.21, 0.14], [0.22, 0.1], [-0.02, 0.13], [0.08, 0.16], [0.21, 0.11], [0.04, 0.08], [0.16, 0.1], [0.16, 0.19], [0.03, 0.16], [0.09, 0.13], [0.1, 0.11], [0.26, 0.06], [0.05, 0.13], [0.07, 0.1], [0.18, 0.1], [0.18, 0.15], [0.18, 0.2], [-0.03, 0.07], [0.11, 0.14], [-0.01, 0.1], [0.2, 0.1], [0.03, 0.19], [-0.02, 0.17], [-0.01, 0.19], [0.1, 0.08], [0.09, 0.07], [0.05, 0.13], [0.06, 0.2], [0.06, 0.12], [0.11, 0.2]]])

        self.populacionar(self.populacao, self.individuos-1)
        for generation in range(self.generations):
            self.inicializar_valores()
            self.get_fitness()
            self.segregar_populacao()
            self.inserir_novos_membros(self.elite)
            self.populacionar(self.nova_populacao, self.qtd_mutations)
            self.produzir_filhos()
            self.encerrar_geracao(generation)

    def inicializar_valores(self):
        self.nova_populacao, self.fitness = [], []
        self.elite, self.non_elite = [], []
    
    def populacionar(self, populacao, individuos):
        for _ in range(individuos):
            cromossomo = []
            for i in range(self.genes):
                x = round(uniform(limites_cromossomo[i][0][1], limites_cromossomo[i][0][0]), 2)
                y = round(uniform(limites_cromossomo[i][1][1], limites_cromossomo[i][1][0]), 2)
                cromossomo.append([x, y])
            populacao.append([cromossomo])

    def get_fitness(self):
        np_populacao = np.squeeze(np.asanyarray(self.populacao))  # transforma população em array numpy
        
        for i in range(len(np_populacao)):
            self.fitness.append(fitness(np_populacao[i]))

    def segregar_populacao(self):
        fitness_lista = [self.fitness[i][0] for i in range(len(self.fitness))]
        fitness_lista = list(enumerate(fitness_lista))
        fitness_lista = sorted(fitness_lista, key=lambda x: x[1])

        for _ in range(len(self.populacao)//4):
            indice = fitness_lista.pop()
            cromossomo = self.populacao[indice[0]]
            fitness_cromossomo = indice[1]
            self.elite.append([cromossomo, fitness_cromossomo])
        
        self.melhor_solucao_geracao = self.elite[0]
        
        for _ in range(len(fitness_lista)):
            indice = fitness_lista.pop()
            self.non_elite.append((self.populacao[indice[0]], indice[1]))

    def inserir_novos_membros(self, grupo):
        for cromossomo in grupo:
            self.nova_populacao.append(cromossomo[0])

    def produzir_filhos(self):
        for _ in range(self.individuos - len(self.nova_populacao)):
            
            pop_total = self.elite + self.non_elite
            
            pai1 = self.escolher_pai(self.elite)
            pai2 = self.escolher_pai(pop_total)
            filho = []
            
            # print(pai1)
            
            # fit1 = self.elite.index(pai1)
            # fit2 = pop_total.index(pai2)
            
            # print(fit2)
            
            # if fit2 < fit1:
            #     aux = pai2
            #     pai2 = pai1
            #     pai1 = aux
            
            for i in range(len(pai1)):
                if random() < 0.7:
                    filho.append(pai1[i])
                else:
                    filho.append(pai2[i])
                    
            self.nova_populacao.append(filho)
    
    def escolher_pai(self, grupo):
        total = sum([i[1] for i in grupo])
        pick = uniform(0, total)
        acumulo = 0
        for cromossomo in grupo:
            acumulo += cromossomo[1]
            if acumulo > pick:
                return cromossomo[0]

    def encerrar_geracao(self, generation):
        self.classificar_solucao()
        self.exibir_dados(generation)
        self.populacao = self.nova_populacao    
 
    def classificar_solucao(self):
        if self.melhor_solucao_geracao[1] > self.melhor_solucao_geral[1]:
            self.melhor_solucao_geral = self.melhor_solucao_geracao

        self.melhores_solucoes.append(self.melhor_solucao_geral[1])
    
    def exibir_dados(self, generation):
        print(f'Geração: {generation}')
        print(f'Melhor fitness: {self.melhor_solucao_geral[1]}')
    
    def plottar_grafico(self):
        plt.style.use('bmh')
        plt.plot([i for i in range(1, len(self.melhores_solucoes) + 1)], self.melhores_solucoes)
        plt.xlabel("Número de gerações")
        plt.ylabel("Potência (W)")
        plt.title("Curva de Convergência - BRKGA")
        
        fig1 = plt.gcf()
        #plt.show()
        #plt.draw()
        
        nome_arquivo = "graficos/" + self.versao + "_grafico"
        #"_conv" + str(self.individuos) + "indiv" + str(self.qtd_mutations) + "mut" + "_Pcode"
        # fig1.savefig(nome_arquivo + "tran", transparent=True)  # para salvar fig sem background
        fig1.savefig(nome_arquivo)
        plt.cla()
        
    def get_grafico_id(self):
        mypath = 'graficos/'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        onlyfiles = [i for i in onlyfiles if '.png' in i]
        return "{0:03}".format(len(onlyfiles) + 1)
    
    def gerar_relatorio(self):
        filename = 'graficos/' + self.versao + "_relatorio.txt"
        text = "Número de gerações: {n_gen}\nIndivíduos: {n_indi}\nGenes: {n_genes}\nMutantes: {n_mut}\n".format(n_gen = self.generations, n_indi = self.individuos, n_genes = self.genes, n_mut = self.qtd_mutations)
        text += f'Melhor fitness: {self.melhor_solucao_geral[1]}\n\n'
        
        n = 1
        for gene in self.melhor_solucao_geral[0][0]:
            text += f'{n} | {gene[0]} | {gene[1]}\n'
            n += 1
        
        text += f'\n{self.melhor_solucao_geracao[0][0]}'
        
        with open(filename, 'w') as f:
            f.write(text)


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
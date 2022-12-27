from Funcao_fitness import fitness

class Key:
    def __init__(self, individual):
        self.individual = individual
        self.fitness = self.get_fitness()
        
    def get_fitness(self):
        self.fitness = fitness(self.individual)
        
    def __str__(self):
        return f'Key {self.fitness}'

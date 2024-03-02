from initializePopulation import initializePopulation
from evaluate import evaluate

class NQueens:
    def __init__(self,size):
        self.size = size
        self.solution = None

    def solve(self,populationSize):
        if self.size < 4:
            return
        population = initializePopulation(populationSize,self.size)
        while (True):
            # evaluate population
            evaluate(population)
            for chromosome in population:
                if chromosome.fitness == 0:
                    self.solution = chromosome
                    return


        
from initializePopulation import initializePopulation
from evaluate import evaluate
from selection import selection
from variation import variation

class NQueens:
    def __init__(self,size):
        self.size = size
        self.solution = None

    def solve(self,populationSize,maxTries):
        if self.size < 4:
            return
        if populationSize%2 != 0:
            return
        
        population = initializePopulation(populationSize,self.size)
        for i in range(maxTries):
            # evaluate population
            evaluate(population)
            for chromosome in population:
                if chromosome.fitness == 0:
                    self.solution = chromosome
                    return
            matingPool = selection(population)
            population = variation(matingPool)
        
        return

            

        
from initializePopulation import initializePopulation

class NQueens:
    def __init__(self,size):
        self.size = size

    def solveGA(self,populationSize):
        population = initializePopulation(populationSize,self.size)
    def solveMinConflicts(self):
        return
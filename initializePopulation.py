from Chromosome import Chromosome
import random
import copy

def initializePopulation(populationSize,chromosomeSize,cycle):
    population = []
    allowedGenes = []
    for i in range(chromosomeSize):
        allowedGenes.append(i+1)

    for i in range(populationSize):
        chromosome = Chromosome()
        random.shuffle(allowedGenes)
        chromosome.queens = copy.deepcopy(allowedGenes)
        chromosome.type.append(cycle)
        population.append(chromosome)
    return population
    
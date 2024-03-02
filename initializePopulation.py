from Chromosome import Chromosome
import random

def initializePopulation(populationSize,chromosomeSize):
    population = []
    for i in range(populationSize):
        chromosome = Chromosome()
        for i in range(chromosomeSize):
            gene = random.randint(1,chromosomeSize)
            chromosome.queens.append(gene)
        population.append(chromosome)
    return population
    
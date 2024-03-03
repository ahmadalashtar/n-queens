import math
import random

def getFitness(chromosome):
    return chromosome.fitness

def selection(population):
    pool = []

    if len(population)<6:
        fightersCount = 2
    else:
        fightersCount = math.ceil(len(population)/5)
    
    for i in range(len(population)):
        cage = []

        random.shuffle(population)
        cage = population[0:fightersCount]
    
        cage.sort(key=getFitness)

        winner = cage[0]

        winner.cycles.append("won the cage fight in selection to mate")
        pool.append(winner)
    
    return pool
        





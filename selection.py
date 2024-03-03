import math
import random

def getFitness(chromosome):
    return chromosome.fitness

def selection(population):
    pool = []

    if len(population)<6:
        k = 2
    else:
        k = math.ceil(len(population)/5)
    
    for i in range(len(population)):
        cage = []

        for i in range(k):
            index = random.randint(0,len(population)-1)
            chromosome = population[index]
            cage.append(chromosome)
        
        cage.sort(key=getFitness)

        winner = cage[0]

        pool.append(winner)
    
    return pool
        





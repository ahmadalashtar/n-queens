def getFitness(chromosome):
    return chromosome.fitness

def survive(offsprings,population):
    generation = offsprings + population
    generation.sort(key=getFitness)
    newPopulation = []
    for i in range(len(population)):
        newPopulation.append(generation[i])
    
    return newPopulation

from initializePopulation import initializePopulation 

def getFitness(chromosome):
    return chromosome.fitness

def survive(offsprings,population, extraPopulation):
    generation = offsprings + population + extraPopulation
    generation.sort(key=getFitness)
    newPopulation = []
    for i in range(len(population)):
        generation[i].cycle.append("selected")
        newPopulation.append(generation[i])
    
    return newPopulation

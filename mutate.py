import random

def mutate(offsprings):
    probability = 0.15

    for i in range(len(offsprings)):
        for j in range(len(offsprings[0].queens)):
            mutationProbability = random.random()
            if mutationProbability <= probability:
                offsprings[i].cycles.append("mutated")
                randomIndex = random.randint(0,len(offsprings[0].queens)-1)
                offsprings[i].queens[j], offsprings[i].queens[randomIndex]  = offsprings[i].queens[randomIndex],  offsprings[i].queens[j]
    
    return offsprings

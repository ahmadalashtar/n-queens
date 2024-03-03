import random

def mutate(offsprings):
    probability = 0.1

    for i in range(len(offsprings)):
        for j in range(len(offsprings[0].queens)):
            mutationProp = random.random()
            if mutationProp<= probability:
                offsprings[i].queens[j] = random.randint(1,len(offsprings[0].queens))
    
    return offsprings

from Chromosome import Chromosome
import random

def crossover(pool):
    offsprings = []

    random.shuffle(pool)
    chromosome = pool[0]
    crossoverSite = random.randint(1,len(chromosome.queens)-1)
    for i in range(len(pool)//2):
        father = pool[i]
        mother = pool[i+1]
        firstChild = Chromosome()
        secondChild = Chromosome()

        for j in range(len(chromosome.queens)):
            if j < crossoverSite:
                firstChild.queens.append(father.queens[j])
                secondChild.queens.append(mother.queens[j])

            else:
                firstChild.queens.append(mother.queens[j])
                secondChild.queens.append(father.queens[j])
    
        offsprings.append(firstChild)
        offsprings.append(secondChild)
    
    return offsprings
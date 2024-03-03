from Chromosome import Chromosome
import random
import copy
def crossover(pool):
    offsprings = []

    random.shuffle(pool)
    chromosome = pool[0]
    crossoverSite = random.randint(1,len(chromosome.queens)-1)
    while (i < len(pool)-1):
        father = pool[i]
        mother = pool[i+1]
        firstChild = Chromosome()
        secondChild = Chromosome()
        fatherQueens = father.queens
        motherQueens = mother.queens
        firstChild.queens = copy.deepcopy(fatherQueens)
        secondChild.queens = copy.deepcopy(motherQueens)
        firstPart = fatherQueens[0:crossoverSite]
        secondPart = motherQueens[0:crossoverSite]
        for j in range(len(firstPart)):
            secondIndex = secondChild.queens.index(firstPart[j])
            secondChild.queens[j], secondChild.queens[secondIndex] = secondChild.queens[secondIndex], secondChild.queens[j]
        for k in range(len(secondPart)):
            firstIndex = firstChild.queens.index(secondPart[k])
            firstChild.queens[k], firstChild.queens[firstIndex] = firstChild.queens[firstIndex], firstChild.queens[k]
        
        firstChild.cycles.append("offspring")
        secondChild.cycles.append("offspring")
        offsprings.append(firstChild)
        offsprings.append(secondChild)
        i += 2

    return offsprings
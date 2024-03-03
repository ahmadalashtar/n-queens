from crossover import crossover
from mutate import mutate

def variation(pool):
    offsprings = crossover(pool)
    offsprings = mutate(offsprings)
    return offsprings
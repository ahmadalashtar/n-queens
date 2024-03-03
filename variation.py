from crossover import crossover
from mutate import mutate
import random

def variation(pool):
    random.shuffle(pool)
    offsprings = crossover(pool)
    population = mutate(offsprings)
    return population



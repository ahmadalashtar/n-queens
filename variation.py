from crossover import crossover
from mutate import mutate
import random

def variation(pool):
    offsprings = crossover(pool)
    population = mutate(offsprings)
    return population



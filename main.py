from NQueens import NQueens

queens = 4
populationSize = 100
maxTries = 100

nqueens = NQueens(queens)

nqueens.solve(populationSize, maxTries)

print(nqueens.solution.queens)
print(nqueens.solution.fitness)
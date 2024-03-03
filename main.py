from NQueens import NQueens

nqueens = NQueens(10)
nqueens.solve(15)
print(nqueens.solution.queens)
print(nqueens.solution.fitness)
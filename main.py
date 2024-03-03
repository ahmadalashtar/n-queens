from NQueens import NQueens

def main():
    queens = 10
    populationSize = 100
    maxTries = 100

    if populationSize%2 != 0:
        print("Population size must be an even number!")
        return
    
    nqueens = NQueens(queens)

    nqueens.solve(populationSize, maxTries)

    if  nqueens.solution is None:
        print("No solution found!")
        return
    
    print(nqueens.solution.queens)
        

if __name__ == "__main__":
    main()
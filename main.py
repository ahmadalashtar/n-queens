import argparse
from NQueens import NQueens

def main(queens, populationSize, maxTries):
    if populationSize % 2 != 0:
        print("Population size must be an even number!")
        return
    nqueens = NQueens(queens)
    nqueens.solve(populationSize, maxTries)
    if nqueens.solution is None:
        print("No solution found!")
        return
    print(nqueens.solution.queens)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Solve N-Queens problem using Genetic Algorithm')
    parser.add_argument('--queens', type=int, default=10, help='Number of Queens')
    parser.add_argument('--populationSize', type=int, default=100, help='Population Size')
    parser.add_argument('--maxTries', type=int, default=100, help='Maximum Number of Tries')

    args = parser.parse_args()

    main(args.queens, args.populationSize, args.maxTries)
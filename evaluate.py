def checkAdjacentCells(queens):
    violations = 0
    for i in range(len(queens)):
        for j in range(i+1,len(queens)):
            if queens[i]==queens[j]:
                violations += 1

    return violations

def checkDiagonally(queens):
    violations = 0
    for i in range(len(queens)):
        for j in range(i+1,len(queens)):
            if queens[i]==queens[j]+j-i or queens[j]==queens[i]+j-i:
                violations += 1
    return violations
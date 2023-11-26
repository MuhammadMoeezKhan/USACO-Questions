#Question Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=687
#Run Command: python3 notLast.py < notlast.in > notlast.out

from collections import defaultdict

def findSecondMinMilkAmount(numCows):
    #edge case: checking if cannot have a second minimum milk amount
    if numCows < 2:
        return "Tie"

    #adding up all milk amounts for all cows
    cowLog, secondMinMilk, winnerCow = defaultdict(int), float('inf'), ""
    for _ in range(numCows):
        cowName, milkAmount = input().split(' ')
        cowLog[cowName] += int(milkAmount)
    
    #finding the second min milk amount value
    minMilk = min(cowLog.values())
    for cowName, milkAmount in cowLog.items():
        if milkAmount > minMilk and milkAmount < secondMinMilk:
            secondMinMilk = milkAmount
            winnerCow = cowName

    #checking if any Ties exist for the second minimum milk amount
    checkTie = sum(1 for milk in cowLog.values() if milk == secondMinMilk)

    #if tie exists return "Tie"
    if checkTie > 1 or secondMinMilk == float('inf'):
        return "Tie"
    
    #else return the name of the winning cow!
    else:
        return winnerCow
    

def writeToOutputFile():
    numCows = int(input())
    with open("notlast.out", "w") as outputFile:
        print(findSecondMinMilkAmount(numCows), file = outputFile)

writeToOutputFile()
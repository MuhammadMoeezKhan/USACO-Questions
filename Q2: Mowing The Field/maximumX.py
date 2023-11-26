#Question Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=593
#Run Command: python3 maximumX.py < mowing.in > mowing.out

from collections import defaultdict

def findMaximumX(currentPosition, numMovements):
    #track the most recent time for the last visited cell, and move in the direction mentioned in the dict below
    cellLastVisitTimes, directions, currentTime = defaultdict(int), {'N': [0,-1], 'E': [1,0], 'S': [0,1], 'W':[-1,0]}, 0
    cellLastVisitTimes[currentPosition], maximumX = currentTime, -1

    #for each direction movemenet
    for _ in range(numMovements):
        direction, steps = input().split(' ')
        steps = int(steps)

        #for each step in that cetain direction
        for _ in range(steps):
            currentTime += 1

            #update currentPosition by moving in that direction from currentPosition
            currentPosition = (currentPosition[0] + directions[direction][0], currentPosition[1] + directions[direction][1])

            #if already visited, update map , track maximumX, and move back to starting position
            if currentPosition in cellLastVisitTimes:
                lastVisitTime = cellLastVisitTimes[currentPosition]
                cellLastVisitTimes[currentPosition] = currentTime
                maximumX = max(maximumX, currentTime - lastVisitTime)
                currentPosition = (0,0)
            
            #mark cell as visited
            cellLastVisitTimes[currentPosition] = currentTime
        
    #if not cell was visited twice, returns initialized value => -1
    return maximumX


def writeToOutputFile():
    numberMovements = input()
    with open("mowing.out", "w") as outputFile:
        print(findMaximumX((0, 0), int(numberMovements)), file = outputFile)

writeToOutputFile()
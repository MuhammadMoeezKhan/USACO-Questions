#Question Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=713
#Run Command: python3 timeForAllCowsToPass.py < cowqueue.in > cowqueue.out

from collections import deque
import heapq as hq

def findMinTimeToPass(numCows):
    minTimeToPass, cowTimeMinHeap = 0, []

    #sort cows according to their arrival times
    for _ in range(numCows):
        arrivalTime, questionTime = input().split(' ')
        arrivalTime, questionTime = int(arrivalTime), int(questionTime)
        hq.heappush(cowTimeMinHeap, (arrivalTime, questionTime))

    #traverse over all cows 
    while cowTimeMinHeap:
        arrivalTime, questionTime = hq.heappop(cowTimeMinHeap)

        #if arrive later than currentTime - update to arrivalTime and questioningTime
        if arrivalTime >= minTimeToPass:
            minTimeToPass = arrivalTime + questionTime

        #else just add the current questioningTime
        else:
            minTimeToPass += questionTime
            
    return minTimeToPass


#write result to output file 
def writeOutputToFile():
    n = int(input())
    with open("cowqueue.out", "w") as outputFile:
        print(findMinTimeToPass(n), file = outputFile)

writeOutputToFile()
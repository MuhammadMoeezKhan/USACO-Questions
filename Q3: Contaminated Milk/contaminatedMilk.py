#Question Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=569
#Run Command: python3 contaminatedMilk.py < badmilk.in > badmilk.out

from collections import defaultdict
import heapq as hq

def numberOfMedicineDoses(numPeople, numMilks, numDrinkLogs, numSickLogs):
    #data structures to map person to milk, perosn to milkTime, and store all possible bad milks
    personMilks, personMilkTime, possibleBadMilks, numSickPeople = defaultdict(list), defaultdict(list), defaultdict(set), 0

    #trcak every person's milk consumption in dict and minHeap
    for _ in range(numDrinkLogs):
        person, milk, drinkTime = input().split(' ')
        personMilks[person].append(milk)
        hq.heappush(personMilkTime[person], (drinkTime, milk))

    #track every sick person's milk consumption
    for _ in range(numSickLogs):
        person, sickTime = input().split(' ')
        while personMilkTime[person] and personMilkTime[person][0][0] <= sickTime:
            possibleBadMilks[person].add(hq.heappop(personMilkTime[person])[1])

    #find the mutual milks that possibily consumed by all sick and could be bad
    mutualMilks = None
    for milkSet in possibleBadMilks.values():
        if not mutualMilks:
            mutualMilks = milkSet
        mutualMilks &= milkSet
    
    #find the number of people that consumed any of the possible bad milks
    for person in range(1, numPeople + 1):
        if str(person) in personMilks:
            for milk in personMilks[str(person)]:
                if milk in mutualMilks:
                    numSickPeople += 1
                    break
    
    #gets updated throughout last check, else return initalized value => 0
    return numSickPeople

#output to file
def writeOutputToFile():
    n, m, d, s = input().split(' ')
    n, m, d, s = int(n), int(m), int(d), int(s)

    with open("badmilk.out", "w") as outputFile:
        print(numberOfMedicineDoses(n, m, d, s), file = outputFile)

writeOutputToFile()
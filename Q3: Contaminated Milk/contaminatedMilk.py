#Question: http://www.usaco.org/index.php?page=viewproblem2&cpid=569
#Run Command: python3 contaminatedMilk.py < badmilk.in > badmilk.out

from collections import defaultdict
import heapq as hq

def numberOfMedicineDoses(numPeople, numMilks, numDrinkLogs, numSickLogs):
    personMilks ,personMilkTime, possibleBadMilks, numSickPeople = defaultdict(list), defaultdict(list), defaultdict(set), 0

    for _ in range(numDrinkLogs):
        person, milk, drinkTime = input().split(' ')
        personMilks[person].append((drinkTime, milk))
        hq.heappush(personMilkTime[person], (drinkTime, milk))

    for _ in range(numSickLogs):
        person, sickTime = input().split(' ')
        while personMilkTime[person] and personMilkTime[person][0][0] <= sickTime:
            possibleBadMilks[person].add(hq.heappop(personMilkTime[person])[1])

    mutualMilks = None
    for milkSet in possibleBadMilks.values():
        if not mutualMilks:
            mutualMilks = milkSet
        mutualMilks &= milkSet
    
    for person in range(1, numPeople + 1):
        if str(person) in personMilks:
            for _, milk in personMilks[str(person)]:
                if milk in mutualMilks:
                    numSickPeople += 1
                    break

    return numSickPeople

def writeOutputToFile():
    n, m, d, s = input().split(' ')
    n, m, d, s = int(n), int(m), int(d), int(s)

    with open("badmilk.out", "w") as outputFile:
        print(numberOfMedicineDoses(n, m, d, s), file = outputFile)

writeOutputToFile()
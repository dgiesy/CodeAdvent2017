'''
Created on Dec 7, 2017

@author: Zog
'''


def oneCycle(startingList):
    endingList = startingList[:]
    listSize = len(startingList)
    maxValue = max(startingList)
    runningIndex = startingList.index(maxValue)
    endingList[runningIndex] = 0
    while maxValue > 0:
        runningIndex += 1
        workingIndex = runningIndex % listSize
        endingList[workingIndex] += 1
        maxValue -= 1    
    return endingList

def findStateInStates(currentState, allPastStates):
    matchIndex = -1    
    for aState in allPastStates:
        if aState == currentState:
            matchIndex = allPastStates.index(aState)
            break    
    return matchIndex

    
if __name__ == '__main__':
    startingMemoryList = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]
    previousStateList = []
    currentMemoryList = startingMemoryList[:]
    cycleCounter = 0
    foundStateIndex = -1
    while foundStateIndex < 0:
        foundStateIndex = findStateInStates(currentMemoryList, previousStateList)
        previousStateList.append(currentMemoryList)
        currentMemoryList = oneCycle(currentMemoryList)
        cycleCounter = cycleCounter + 1
        print("Intermediate cycle counter: " + str(cycleCounter))

    print("Number of loops to find cycle: " + str(cycleCounter))
    print("Length of cycle: " + str((cycleCounter - 1) - foundStateIndex))
    
    pass
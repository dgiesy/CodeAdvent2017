'''
Created on Dec 5, 2017

@author: dgiesy

Author's Note:
Yes, there is a ton of repeated code in here. This is what happens when I get a late
start and I'm tired and don't feel like refactoring after I get everything working.
'''

def readData():
    with open("../../../../jumpsteps.txt", "r") as f:
        dataList = f.read().splitlines()
    return dataList

def part1Nav(numList):
    print("Starting List Part 1: " + str(numList))
    listLength = len(numList)
    listPosition = 0
    startingPositionValue = 0
    endingPositionValue = 0
    jumpDistance = 0
    numJumps = 0
    
    while listPosition < listLength:
        startingPositionValue = numList[listPosition]
        jumpDistance = startingPositionValue
        endingPositionValue = startingPositionValue + 1
        numList[listPosition] = endingPositionValue
        listPosition = listPosition + jumpDistance
        numJumps = numJumps + 1
    
    print("Part1 exited List after: " + str(numJumps) + " jumps.")
    return numJumps

def part2Nav(numList):
    print("Starting List Part 2: " + str(numList))
    listLength = len(numList)
    listPosition = 0
    startingPositionValue = 0
    endingPositionValue = 0
    jumpDistance = 0
    numJumps = 0
    
    while listPosition < listLength:
        startingPositionValue = numList[listPosition]
        jumpDistance = startingPositionValue
        if jumpDistance < 3:
            endingPositionValue = startingPositionValue + 1
        else:
            endingPositionValue = startingPositionValue - 1
        numList[listPosition] = endingPositionValue
        listPosition = listPosition + jumpDistance
        numJumps = numJumps + 1
    
    print("Part 2 exited List after: " + str(numJumps) + " jumps.")
    return numJumps

if __name__ == '__main__':

    jumpList = readData()
    numberListPart1 = list(map(int, jumpList))
    numberListPart2 = list(map(int, jumpList))
    
    part1Nav(numberListPart1)
    part2Nav(numberListPart2)
    pass
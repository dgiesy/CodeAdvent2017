'''
Created on Dec 13, 2017

@author: dgiesy
'''

def read_data(fileName):
    with open(fileName) as junk:
        walls = {}
        content = junk.readlines()
        for line in content:
            cleanContent = line.split(": ")
            walls[cleanContent[0]]=cleanContent[1].strip()
    return walls

def populate_data(fw2):
    expandedFireWalls = {}
    count = 0
    while len(fw2) > 0:
        keyList = list(fw2.keys())
#         print(str(keyList))
        if str(count) in keyList:
            expandedFireWalls[count] = fw2[str(count)]
            del(fw2[str(count)])
            count += 1
        else:
            expandedFireWalls[count] = None
            count += 1

    return expandedFireWalls

def find_location_cost(maxDepth, moves):
    cost = 0
    bottomTier = maxDepth - 1
    if moves % bottomTier == 0:
        if (moves / bottomTier) % 2 == 0:
            cost = moves * maxDepth
    return cost

if __name__ == '__main__':
    fileName = "../firewalls.txt"
    
    compressedFirewalls = read_data(fileName)
#     Create a disposable copy
    disposableWalls = dict(compressedFirewalls)
    fullWalls = populate_data(disposableWalls)
    
    picos = len(fullWalls)
    step = 0
    totalCost = 0
    caughtAt = []
    while step < picos:
        if not fullWalls[step] == None:
            currentDepth = int(fullWalls[step])
            totalCost += find_location_cost(currentDepth,step)
        step += 1
    
    print("Total cost for Part 1: " + str(totalCost))
    pass

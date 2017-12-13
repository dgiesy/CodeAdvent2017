'''
Created on Dec 12, 2017

@author: Zog
'''

def read_data(fileName):
    allPipes = {}
    lineCount = 0
    with open(fileName) as junk:
        lines = junk.readlines()
        for line in lines:
            lineCount += 1
            parts = line.split("<->")
            targets = parts[1].split(",")
            cleanTargets = []
            for target in targets:
                cleanTargets.append(target.strip())
            allPipes[parts[0].strip()] = cleanTargets
    return allPipes, lineCount

def scan_connections(pipeDict, connectArr):
    changes = 0
    changeArr = []
    for key in pipeDict:
        if key in connectArr:
            connections = pipeDict[key]
            for connection in connections:
                if not connection in connectArr:
                    connectArr.append(connection)
                    changeArr.append(connection)
                    changes += 1
#     print(str(changeArr))
#     print("Number of changes this scan: " + str(len(changeArr)))
    return connectArr, changes

def remove_used_keys(oldDict, usedKeys):
    newDict =  dict(oldDict)
    
    for key in usedKeys:
        del newDict[key]
    
    return newDict

if __name__ == '__main__':
    fileName = "../pipes.txt"
    
    pipes, count = read_data(fileName)
    connectedToZero = ['0']
    updatedConnect, changeCount = scan_connections(pipes, connectedToZero)
    scans = 1
    while not changeCount == 0:
        updatedConnect, changeCount = scan_connections(pipes,updatedConnect)
        scans += 1
    
    numConnected = len(updatedConnect)
    numUnconnected = count - numConnected
#     print("Ran " + str(scans) + " scans")
    print(str(numConnected) + " nodes ARE connected to Zero")
#     print("Final connected array: " + str(updatedConnect))
    groups = 1
    remainingPipes = remove_used_keys(pipes, updatedConnect)
    
    while len(remainingPipes) > 0:
        groups += 1
        pipeKeys = list(remainingPipes.keys())
        baseKey = pipeKeys[0]
        connectedToBase = [baseKey]
        cCount = 1
        scans = 0
        while not cCount == 0:
            connectedToBase, cCount = scan_connections(remainingPipes, connectedToBase)
            scans += 1
#         print("Ran this many scans: " + str(scans))
#         print("Found these connections: " + str(connectedToBase))
        remainingPipes = remove_used_keys(remainingPipes, connectedToBase)
    
    print("Groups found: " + str(groups))
    pass
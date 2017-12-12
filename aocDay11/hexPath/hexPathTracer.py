'''
Created on Dec 11, 2017

@author: Zog
'''

from collections import Counter
from itertools import count

def read_data(fileName):
    with open(fileName) as junk:
        content = junk.readline()
    cleanContent = content.split(",")
    return cleanContent

def eliminate_offseting_pairs(countDict):
    afterDict = {}
    north = countDict['n']
    south = countDict['s']
    if north > south:
        afterDict['n'] = north - south
    else:
        afterDict['s'] = south - north
    
    norEast = countDict['ne']
    souWest = countDict['sw']    
    if  norEast > souWest:
        afterDict['ne'] = norEast - souWest
    else:
        afterDict['sw'] = souWest - norEast
    
    norWest= countDict['nw']
    souEast = countDict['se']    
    if  norWest > souEast:
        afterDict['nw'] = norWest - souEast
    else:
        afterDict['se'] = souEast - norWest

    return afterDict

'''
#     Three cases total
#     Case 1
        All three N|S directions are the same.
        e.g. n, ne, nw or s, se, sw
#     Case 2
        The Cardinal direction is opposite the two angles
        e.g. n, se, sw or s, ne, nw
#     Case 3
        The angles have opposite N|S component
        e.g. n, nw, sw || n, ne, se || s, nw, sw || s, ne, se  
#    
'''
def add_remaining_steps(stepDict, headings):
    upDown = ""
    angles = []
    for point in headings:
        if len(point) == 1:
            upDown = stepDict[point]
        else:
            angles.append(stepDict[point])
    
    
    totalSteps = 0
    if ('n' in headings and 'ne' in headings and 'nw' in headings) or ('s' in headings and 'se' in headings and 'sw' in headings):
        totalSteps = upDown + max(angles[0], angles[1])
    elif ('n' in headings and 'se' in headings and 'sw' in headings) or ('s' in headings and 'ne' in headings and 'nw' in headings):
        totalSteps = angles[0] + angles[1] - upDown
    elif ('n' in headings and 'nw' in headings and 'sw' in headings) or ('n' in headings and 'ne' in headings and 'se' in headings) or ('s' in headings and 'ne' in headings and 'se' in headings) or ('s' in headings and 'nw' in headings and 'sw' in headings):
        if upDown > min(angles[0], angles[1]):
            totalSteps = upDown + max(angles[0], angles[1])
        else:
            totalSteps = angles[0] + angles[1]

    
    return totalSteps

if __name__ == '__main__':
    
    pathFileName = "../hexSteps.txt"
    pathArr = read_data(pathFileName)
    print("Number of Steps: " + str(len(pathArr)))
    
#     PART 1
    directionCount = Counter(pathArr)
    for key in directionCount:
        print("Key: " + key + ", Count: " + str(directionCount[key]))
    
    dirCount2 = eliminate_offseting_pairs(directionCount)
    remainingHeadings = []
    for key in dirCount2:
        remainingHeadings.append(key)
        print("Key: " + key + ", Count: " + str(dirCount2[key]))
        
    print("Remaining Headings: " + str(remainingHeadings))
    print("Total Distance after all steps: " + str(add_remaining_steps(dirCount2, remainingHeadings)))
    
#     Part 2
    p2Dict = {"n":0, "s":0, "ne":0, "nw":0, "se":0, "sw":0}
    maxDistance = 0
    for step in pathArr:
        p2Dict[step] = p2Dict[step] + 1
        p2short = eliminate_offseting_pairs(p2Dict)
        currentHeadings = []
        for key in p2short:
            currentHeadings.append(key)
        currentSteps = add_remaining_steps(p2short, currentHeadings)
        if currentSteps > maxDistance:
            maxDistance = currentSteps
        print("Current max reached: " + str(maxDistance))    
    print(maxDistance)
    pass
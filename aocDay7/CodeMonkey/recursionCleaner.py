'''
Created on Dec 7, 2017

@author: Zog
'''
import re

class Node(object):
    name = ""
    parent = ""
    weight = 0
    children = []
    totalWeight = 0
    
    def __init__(self, name, parent, weight, children, totalWeight):
        self.name = name
        self.parent = parent
        self.weight = weight
        self.children = children
        self.totalWeight = totalWeight

def make_node(name, parent, weight, children, totalWeight=None):
    node = Node(name, parent, weight, children, totalWeight)
    return node

def print_node(aNode):
    print(str(aNode.name) + ", " + str(aNode.weight) + ", " + str(aNode.parent) + ", " + str(aNode.children) + ", " + str(aNode.totalWeight))

def read_data(fileName):
    with open(fileName) as junk:
        content = junk.readlines()
    cleanContent = [x.strip() for x in content]
    return cleanContent

def munch_data(rawArr):
    returnDict = {}
    for aString in rawArr:
        firstSplitArr = aString.split("->")
        frontHalfArr = firstSplitArr[0].split(" ")
        if len(firstSplitArr) > 1:
            tempArr = firstSplitArr[1].split(",")
            childrenArr = []
            for i in tempArr:
                childrenArr.append(i.strip())
        else:
            childrenArr = None
        name = frontHalfArr[0]
        weight = re.sub(r"[\(\)]", "",frontHalfArr[1])
        aNode = make_node(name, None, weight, childrenArr, None)
        returnDict[name] = aNode
    return returnDict

def find_kids(nodeDict):
    for entry in nodeDict:
        thisNode = nodeDict[entry]
        if not thisNode.children == None:
            kids = thisNode.children
            for kid in kids:
                nodeDict[kid].parent = thisNode.name
    return nodeDict

def find_bottom_node(nodeDict):
    for i in nodeDict:
        if nodeDict[i].parent == None:
            return nodeDict[i].name
    return None

def populate_total_weight(fullDict):
    for entry in fullDict:
        thisNode = fullDict[entry]
        fullDict[entry].totalWeight = find_total_weight(thisNode, fullDict)
    return fullDict


def find_total_weight(base, fullDict):
    totalWeight = int(base.weight)
    if not base.children == None:
        for kid in base.children:
            totalWeight = totalWeight + find_total_weight(fullDict[kid], fullDict)
    return totalWeight

def is_node_balanced(current, fullDict):
    if current.children == None:
        return True
    else:
        kidWeights = []
        for kid in current.children:
            kidWeights.append(fullDict[kid].totalWeight)
        if kidWeights.count(kidWeights[0]) == len(kidWeights):
            return True
    return False

def find_odd_child(parentNode, fullDict):
    oddKidName = ""
    childNodes = []
    for child in parentNode.children:
        childNodes.append(fullDict[child])
    nameWeight = {}
    totalWeights = []
    oddweight = 0
    matchedweight = 0
    for node in childNodes:
        nameWeight[node.totalWeight] = node.name
        totalWeights.append(node.totalWeight)
    for i in range(0, len(totalWeights)):
        if totalWeights.count(totalWeights[i]) == 1:
            oddweight = totalWeights[i]
            oddKidName = nameWeight[oddweight]
        else:
            matchedweight = totalWeights[i]
    return oddKidName, matchedweight

def find_fix_weight(baseNode, fullDict, siblingWeight = 0):
    adjustedWeight = 0
    if not is_node_balanced(baseNode, fullDict):
        badChildName, matchedWeight = find_odd_child(baseNode,fullDict)
        badChild = fullDict[badChildName]
        adjustedWeight = find_fix_weight(badChild, fullDict, matchedWeight)
    else:
        if siblingWeight:
            adjustWeight = abs(baseNode.totalWeight - siblingWeight)
            adjustedWeight = int(baseNode.weight) - adjustWeight
    return adjustedWeight


if __name__ == '__main__':
    
    dataFile = "../tower.txt"

    rawStrings = read_data(dataFile)
    nodeDict = munch_data(rawStrings)
    nodeDict = find_kids(nodeDict)
    nodeDict = populate_total_weight(nodeDict)
    ultimateParent = find_bottom_node(nodeDict)
    print("The node with no Parent and therefore the base is: " + ultimateParent)
    
    newNodeWeight = find_fix_weight(nodeDict[ultimateParent], nodeDict)
    print("The new Node weight is: " + str(newNodeWeight))
    
    pass



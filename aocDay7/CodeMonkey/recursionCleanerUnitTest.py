'''
Created on Dec 8, 2017

@author: Zog
'''
import unittest
from CodeMonkey.recursionCleaner import read_data, munch_data, print_node,\
    find_kids, find_total_weight, populate_total_weight, is_node_balanced,\
    find_bottom_node, find_odd_child, find_fix_weight

class Test(unittest.TestCase):


    def testReadData(self):
        testFile = "../testTower.txt"
        testData = read_data(testFile)
        print(testData)
        pass
    
    def testMunchData(self):
        testFile = "../testTower.txt"
        rawData = read_data(testFile)
        dictionaryOfNodes = munch_data(rawData)
        for entry in dictionaryOfNodes:
            print_node(dictionaryOfNodes[entry])
        
        pass

    def testFindKids(self):
        testFile = "../testTower.txt"
        rawData = read_data(testFile)
        dictionaryOfNodes = munch_data(rawData)
        dictionaryOfNodes = find_kids(dictionaryOfNodes)
        for entry in dictionaryOfNodes:
            print_node(dictionaryOfNodes[entry])
        pass

    def testFindTotaldWeight(self):
        print("Nodes weights as reported by find_total_wieght")
        testFile = "../testTower.txt"
        rawData = read_data(testFile)
        dictionaryOfNodes = munch_data(rawData)
        dictionaryOfNodes = find_kids(dictionaryOfNodes)
        for entry in dictionaryOfNodes:
            thisNode = dictionaryOfNodes[entry]
            print("Total weight of: " + thisNode.name + " is: " + str(find_total_weight(thisNode, dictionaryOfNodes)))
        
        pass
    
    def testPopulateTotalWeight(self):
        print("Nodes weights as reported by populate_total_wieght")
        testFile = "../testTower.txt"
        rawData = read_data(testFile)
        dictionaryOfNodes = munch_data(rawData)
        dictionaryOfNodes = find_kids(dictionaryOfNodes)
        dictionaryOfNodes = populate_total_weight(dictionaryOfNodes)
        for entry in dictionaryOfNodes:
            thisNode = dictionaryOfNodes[entry]
            print("Total weight of: " + thisNode.name + " is: " + str(thisNode.totalWeight))
            
        pass
    
    def testIsNodeBalanced(self):
        testFile = "../testTower.txt"
        rawData = read_data(testFile)
        dictionaryOfNodes = munch_data(rawData)
        dictionaryOfNodes = find_kids(dictionaryOfNodes)
        dictionaryOfNodes = populate_total_weight(dictionaryOfNodes)
        for entry in dictionaryOfNodes:
            thisNode = dictionaryOfNodes[entry]
            print(thisNode.name + " is Balanced?? " + str(is_node_balanced(thisNode, dictionaryOfNodes)))
        pass
    
    def testFindBottomNode(self):
        testFile = "../testTower.txt"
        rawData = read_data(testFile)
        dictionaryOfNodes = munch_data(rawData)
        dictionaryOfNodes = find_kids(dictionaryOfNodes)
        dictionaryOfNodes = populate_total_weight(dictionaryOfNodes)
        baseNodeName = find_bottom_node(dictionaryOfNodes)
        assert(baseNodeName == "tknk")
        pass
    
    def testFindOddChild(self):
        testFile = "../testTower.txt"
        rawData = read_data(testFile)
        dictionaryOfNodes = munch_data(rawData)
        dictionaryOfNodes = find_kids(dictionaryOfNodes)
        dictionaryOfNodes = populate_total_weight(dictionaryOfNodes)
        baseNodeName = find_bottom_node(dictionaryOfNodes)
        baseNode = dictionaryOfNodes[baseNodeName]
        answerList = find_odd_child(baseNode, dictionaryOfNodes)
        print(answerList)
        pass
    
    def testFindFixWeight(self):
        testFile = "../testTower.txt"
        rawData = read_data(testFile)
        dictionaryOfNodes = munch_data(rawData)
        dictionaryOfNodes = find_kids(dictionaryOfNodes)
        dictionaryOfNodes = populate_total_weight(dictionaryOfNodes)
        baseNodeName = find_bottom_node(dictionaryOfNodes)
        baseNode = dictionaryOfNodes[baseNodeName]
        adjustmentNeeded = find_fix_weight(baseNode, dictionaryOfNodes)
        print(adjustmentNeeded)
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRead_data']
    unittest.main()
'''
Created on Dec 12, 2017

@author: Zog
'''
import unittest
from Plumbing.plumbersHelper import read_data, scan_connections,\
    remove_used_keys


class Test(unittest.TestCase):


    def testReadData(self):
        fileName = "../testPipes.txt"
        pipes, lineCount = read_data(fileName)
        assert(lineCount == 7)
        assert(len(pipes) == 7)
        set1 = set(pipes['0'])
        set2 = set(['2'])
        assert(set1 == set2)
        pass
    
    def testScanConnections(self):
        fileName = "../testPipes.txt"
        pipes, lineCount = read_data(fileName)
        connect = ['0']
        outConnect, changes = scan_connections(pipes, connect)
        assert(lineCount == 7)
        pass

    def testRemoveUsedKeys(self):
        fileName = "../testPipes.txt"
        pipes, lineCount = read_data(fileName)
        connect = ['0']
        outConnect, changes = scan_connections(pipes, connect)
        newDict = remove_used_keys(pipes, outConnect)
        assert(len(newDict) == 1)   
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testReadData']
    unittest.main()
'''
Created on Dec 7, 2017

@author: Zog
'''
import unittest
from com.whatever.memoryReallocation import oneCycle, findStateInStates


class Test(unittest.TestCase):


    def testOneCycle(self):
        testStates = [[0, 2, 7, 0], [2, 4, 1, 2], [3, 1, 2, 3], [0, 2, 3, 4,], [1, 3, 4, 1,]]
        for index in range(0, len(testStates)):
            newArr = oneCycle(testStates[index])
            if index < len(testStates) - 1:
                assert(newArr == testStates[index + 1])            
        pass
    
    def testFindStateInStates(self):
        states = [[0, 2, 7, 0], [2, 4, 1, 2], [3, 1, 2, 3], [0, 2, 3, 4], [1, 3, 4, 1]]
        for state in states:
            assert(findStateInStates(state, states) in range(0, len(states)))
        assert(findStateInStates([1,2,3,4], states) < 0)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testOneCycle']
    unittest.main()
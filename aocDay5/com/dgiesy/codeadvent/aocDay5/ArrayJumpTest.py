'''
Created on Dec 5, 2017

@author: dgiesy
'''
import unittest
from com.dgiesy.codeadvent.day5.ArrayJump import part1Nav, part2Nav


class Test(unittest.TestCase):


    def testPart1Nav(self):
        testList1 = [0, 3, 0, 1, -3]
        jumps = part1Nav(testList1)
        print("Ending List: " + str(testList1))
        assert jumps == 5
        pass

    def testPart2Nav(self):
        testList2 = [0, 3, 0, 1, -3]
        jumps = part2Nav(testList2)
        print("Ending List: " + str(testList2))
        assert jumps == 10
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
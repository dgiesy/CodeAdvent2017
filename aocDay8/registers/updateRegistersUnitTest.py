'''
Created on Dec 9, 2017

@author: Zog
'''
import unittest
from registers.updateRegisters import read_data, format_instructions


class Test(unittest.TestCase):


    def testFormatInstructions(self):
        testFile = "../testInstructionSet.txt"
        raw = read_data(testFile)
        prettyInstructions = format_instructions(raw)
        assert(prettyInstructions[0].regName == "b")
        assert(prettyInstructions[0].direction == "inc")
        assert(prettyInstructions[0].amount == 5)
        assert(prettyInstructions[0].condReg == "a")
        assert(prettyInstructions[0].condOp == ">")
        assert(prettyInstructions[0].condValue == 1)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
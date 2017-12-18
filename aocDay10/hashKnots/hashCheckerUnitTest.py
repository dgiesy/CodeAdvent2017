'''
Created on Dec 10, 2017

@author: Zog
'''
import unittest
from hashKnots.hashChecker import hash_checker


class Test(unittest.TestCase):


    def testHashChecker(self):
        testStrings = ["", "AoC 2017", "1,2,3", "1,2,4", "flqrgnkx-0"]
        testExpectedAnswers = ["a2582a3a0e66e6e86e3812dcb672a272", "33efeb34ea91902bb2f59c9920caa6cd", "3efbe78a8d82f29979031a4aa0b16a9d", "63960835bcdc130f0b66d7ff4f6a5a8e", ""]
        
        for i in range(len(testStrings)):
            assert(testExpectedAnswers[i] == hash_checker(testStrings[i]))
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testHashChecker']
    unittest.main()
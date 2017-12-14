'''
Created on Dec 13, 2017

@author: dgiesy
'''
import unittest
from damageCounter import find_location_cost


class Test(unittest.TestCase):


    def testFindLocationCost(self):
        assert(find_location_cost(3, 0) == 0)
        assert(find_location_cost(4, 4) == 0)
        assert(find_location_cost(4, 6) == 24)
        assert(find_location_cost(12, 44) == 528)
        assert(find_location_cost(8, 52) == 0)
        pass

    def testFindTotalCost(self):
        
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
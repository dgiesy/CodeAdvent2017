'''
Created on Dec 1, 2017

@author: dgiesy
'''
import unittest
from ms1.captcha import simpleCaptcha
from ms1.captcha import oppositeCaptcha

class Test(unittest.TestCase):

    def testSimpleCaptcha(self):
        print('Simple Captcha Test')
        self.assertEqual(simpleCaptcha('1122'), 3, 'Total was not 3, Dumbass')
        self.assertEqual(simpleCaptcha('1111'), 4, 'Total was not 4, Dumbass')
        self.assertEqual(simpleCaptcha('1234'), 0, 'Total was not 0, Dumbass')
        self.assertEqual(simpleCaptcha('91212129'), 9, 'Total was not 9, Dumbass')
        
    def testOppositCaptcha(self):
        print('Opposite Captcha Test')
        self.assertEqual(oppositeCaptcha('1212'), 6, 'Total was not 6, Dumbass')
        self.assertEqual(oppositeCaptcha('1221'), 0, 'Total was not 0, Dumbass')
        self.assertEqual(oppositeCaptcha('123425'), 4, 'Total was not 4, Dumbass')
        self.assertEqual(oppositeCaptcha('123123'), 12, 'Total was not 12, Dumbass')
        self.assertEqual(oppositeCaptcha('12131415'), 4, 'Total was not 4, Dumbass')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSimpleCaptcha']
    unittest.main()
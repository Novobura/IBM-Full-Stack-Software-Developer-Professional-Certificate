
'''
#unit test for add function in newmodule.py

#Write test cases for these scenarios.
#When 2 and 4 are given as input the output must be 6.

#When 0 and 0 are given as input the output must be 0.

#When 2.3 and 3.6 are given as input the output must be 5.9.

#When the strings ‘hello’ and ‘world’ are given as input the output must be ‘helloworld’.

#When 2.3000 and 4.300 are given as input the output must be 6.6.

#When -2 and -2 are given as input the output must not be 0. (Hint : Use assertNotEqual)
'''

import unittest

from new_module import add

class TestSquare(unittest.TestCase): 
    def test1(self):
        self.assertEqual(add(2,4), 6) 
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(2.3,3.6),5.9)
        self.assertEqual(add('hello','world'), 'helloworld')
        self.assertEqual(add(2.3000,4.300), 6.6)
        self.assertNotEqual(add(-2,-2), 0)

unittest.main()

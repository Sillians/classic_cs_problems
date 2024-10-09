import unittest
from fib3 import fib3
from fib4 import fib4


class FibonacciTest(unittest.TestCase):
    msg = "Input to fibonacci sequence must be a non-negative integer"

    def testCase1(self):
        self.assertEqual(12586269025, fib3(50), "Case1 unit test")

    def testCase2(self):
        self.assertEqual(12586269025, fib4(50), "Case2 unit test")

    def testCase3(self):
        self.assertEqual(6765, fib3(20), "Case3 unit test")

if __name__ == '__main__':
    unittest.main()
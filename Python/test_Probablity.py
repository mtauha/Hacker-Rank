#!/usr/bin/env python3
import unittest as test
from Probablity import Probability

class ProbabilityTest(test.TestCase):
    def test_case1(self):
        #* Write your code:
        expected = 0.8809523809523809
        List = ['a','a','a','a','d','e','f','g','h']

        self.assertEqual(Probability(3,List),expected)


if __name__ == "__main__":
    test.main()
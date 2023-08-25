#! /usr/bin/env python3
import unittest as test
from Combinations_with_replacement import Combinations_With_Replacement

class Test_Combination_with_replacement(test.TestCase):
    def test_Combination_with_replacement(self):
        expected = [
            "AA",
            "AC",
            "AH",
            "AK",
            "CC",
            "CH",
            "CK",
            "HH",
            "HK",
            "KK",
        ]

        self.assertEqual(Combinations_With_Replacement("HACK","2"),expected)


test.main()
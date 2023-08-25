#!/usr/bin/env python3
import unittest as test
from Combinations import Combinations


class Combination_Test(test.TestCase):
    def test_simple(self):
        expected_list = [
            "A",
            "C",
            "H",
            "K",
            "AC",
            "AH",
            "AK",
            "CH",
            "CK",
            "HK",
        ]
        self.assertEqual(first=Combinations("HACK", "2"), second=expected_list)


test.main()

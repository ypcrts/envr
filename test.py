from __future__ import print_function
import sys
import unittest
from envr import Envr

# class


def load():
    suite = unittest.TestSuite()
    cases = []

    for c in cases:
        suite.addtest(unittest.makeSuite(c))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner().run(load())

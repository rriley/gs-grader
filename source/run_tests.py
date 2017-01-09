#!/usr/bin/python

"""
This code automatically finds all the testcases in the tests/ directory
and runs them.  In the end, it outputs the results in gradescope's json format.
"""

import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

if __name__ == '__main__':
    # Automatically detect and load the tests.
    suite = unittest.defaultTestLoader.discover('tests')

    # This code is a dirty hack to run the tests in alphabetical order
    test_list = []
    for s in suite:
	for t in s:
		for u in t:
			test_list.append(u)
    test_list = sorted(test_list, key=str)
    suite = unittest.TestSuite()
    for t in test_list:
        suite.addTest(t)

    # Run the tests
    JSONTestRunner().run(suite)

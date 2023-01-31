import unittest
import os
import sys
import re
import glob
import file_differ
from gradescope_utils.autograder_utils.decorators import weight
import subprocess32 as subprocess

# The file containing stdin for the program.  This means that this file
# should contain whatever you want to type into the program as input.
INPUT_FILE = "/autograder/source/tests/test01.input"

# A file containing the correct output.
SOLUTION = "/autograder/source/tests/test01.output"

# How to run the program, basically.
EXEC_NAME = "./prog"

# Where to temporary store a program's output.
# You probably don't need to change this.
OUTPUT_FILE = "/tmp/out.tmp"

# How long to wait before assuming their program is stuck in an infinite loop.
TIMEOUT = 10

class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    @weight(10)
    def test01(self):
        """Test 4: Addition with Negative Numbers"""

        # Change to the submission dir
        os.chdir("../workspace")

        # Open the input file
        input_file = open(INPUT_FILE, "rb")
        inp = input_file.read()
        input_file.close()

        # Open a temporary output file
        output_file = open(OUTPUT_FILE,"w")

        # Run the process
        proc = subprocess.Popen(EXEC_NAME.split(), stdin=subprocess.PIPE, stdout=output_file, stderr=subprocess.PIPE)
        try:
            proc.communicate(input=inp, timeout=TIMEOUT)
        except:
            proc.terminate()
            # Program didn't terminate in time, this is almost always a bad submission
            self.assertTrue(False,'Program did not finish within %d seconds'%TIMEOUT)

        # Compare the output and the expected solution.
        if file_differ.diff(OUTPUT_FILE, SOLUTION):
            self.assertTrue(False,'I did some addition involving negative numbers. One of the input numbers is negative, and so is the sum.')

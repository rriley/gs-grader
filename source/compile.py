"""
This script compiles the student submission in /autograder/workspace

It assumes there is already a Makefile present.

If the call to make is not successful, then it returns a results json
file that reports the compile error.
"""

import json
import subprocess32 as subprocess
import os

os.chdir("../workspace/")
proc = subprocess.Popen('make'.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
std_output = proc.stdout.read()
std_err = proc.stderr.read()
returncode = None
try:
    returncode = proc.wait(20)
except:
    pass

if returncode is None or returncode != 0:
    proc.terminate()
    output = "Your program could not compile.\n" + std_err
    test = {"score":0,"output":output,"name":"Compiling"}
    tests = []
    tests.append(test)
    outp = {"tests":tests, "score":0}
    print json.dumps(outp)

This serves as a simple example for a Gradescope compatible autograder.
I assume you have read the Gradescope documentation about Autograder
Specifications that can be found [here](http://gradescope-autograders.readthedocs.io/en/latest/specs/).

This sample autograder uses diff to compare the output of a student
submission with some expected output.  See source/tests/test01.py for
an example.  You can create your own testcases by copying that file to
a new testcase and configuring it appropriately.

The autograder in this repo is meant to grade a simple calculator in C.
Check assignment.pdf for details.

To generate a .zip package suitable for uploading to Gradescope, run:
```make gs```

You can also run and test in a local docker image.  Try...
```make docker-run```

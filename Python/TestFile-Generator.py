#!/usr/bin/env python3
import os

cwd = os.getcwd()
filename = input("Enter file name with extension: ")
test_file = input("Enter exact name of Python module for testing: ")
function = input("Enter name of function you want to test: ")

filename = os.path.join(cwd,filename)

with open(file=filename,mode="w") as file:
    file.write(f"""#!/usr/bin/env python3
import unittest as test
from {test_file} import {function}

class {function}Test(test.TestCase):
    def test_simple(self):
        #* Write your code:
        """)
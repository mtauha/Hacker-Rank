#!/usr/bin/env python3
import os

cwd = os.getcwd()
filename = input("Enter file name with extension: ")
filename = os.path.join(cwd,filename)

with open(file=filename,mode="w") as file:
    file.write("""#!/usr/bin/env python3
               """)
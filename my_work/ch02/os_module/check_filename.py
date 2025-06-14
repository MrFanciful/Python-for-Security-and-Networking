import os
import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(f"[-] {filename} does not exist")
    if not os.access(filename, os.R_OK):
        print(f"[-] {filename} access denied")
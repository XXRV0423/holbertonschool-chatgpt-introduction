#!/usr/bin/python3
import sys

# This script prints the command-line arguments passed to it, excluding the script name itself.
for i in range(1, len(sys.argv)): 
    print(sys.argv[i])
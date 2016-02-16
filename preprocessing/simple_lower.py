#!/usr/local/bin/python3

import sys

# This script takes as input as text file.
# As output, the same text is returned as in the 
# input file, but with all chars lowercased.

with open(sys.argv[1],'r') as fn:
  text = fn.read()

with open(sys.argv[2],'w') as fn:
  fn.write(text.lower())

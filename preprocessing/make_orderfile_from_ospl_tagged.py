#!/usr/local/bin/python3
import sys

# This code takes as input a file, one sentence per line, 
# with each token tagged like so: token/tag
# The output is a file, one token per line, with POS tag
# formatted like so: token tag
# The sentences within the output file are separated by 
# a row of '=' chars.


with open(sys.argv[1],'r') as ospl:
  lines = ospl.read().strip().split('\n')

with open(sys.argv[2],'w') as outfile:
  for line in lines:
    outline = ''
    for token in line.split():
      entry = token.split('/')
      outline+='\n{} {}'.format(entry[0], entry[1])
    outline+='\n====================\n'
    outfile.write(outline.lstrip())


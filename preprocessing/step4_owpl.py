#!/usr/local/bin/python3

import sys, codecs

# Takes as inpu a test with one sentence per line.
# As output, it produces the same text, but now 
# with one word per line.


with open(sys.argv[1], 'r', encoding='utf8') as fn:
  lines = fn.read().strip().split('\n')

for i, line in enumerate(lines):
  outline = ''
  for token in line.split():
    outline+='{}\n'.format(token)
  print(outline.rstrip())



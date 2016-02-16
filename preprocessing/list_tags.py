#!/usr/local/bin/python3

import sys, codecs, re

# This script takes as input a tagged text with 
# tokens and tags formatted like so: token/tag
#
# As output, this script returns a list of unique 
# found in the input text.


with codecs.open(sys.argv[1], 'r', encoding='utf8') as f:
  text = f.read()

tags = re.findall('/(\S+)', text)
for tag in tags:
  print(tag)

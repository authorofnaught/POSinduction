#!/usr/local/bin/python3

import sys, re, codecs

# Takes as input a text with tokens tagged like so:
# token/tag and produces as output the exact same 
# text but with tokens no longer tagged.


with codecs.open(sys.argv[1], 'r', encoding='utf8') as f:
  text = f.read()

print(re.sub('/\S+', '', text).strip())

#!/usr/local/bin/python3

import re, codecs, sys

# Takes as input the concatenated, annotated text of 
# a portion of the Penn Treebank 3.
# The text and POS tags are preserved in token/tag format and  
# output to a file with one sentence per line.


with codecs.open(sys.argv[1], 'r', encoding='utf8') as f:
  text = f.read()

text = re.sub("\n", "", text)
text = re.sub("\( \(S", "\n( (S", text)
text = re.sub(" +", " ", text)
lines = text.split('\n')
outtext = ''
for line in lines:
  matches = re.findall("\(([^()]+ [^()]+)\)", line)
  outline = ''
  for match in matches:
    if 'NONE' not in match:
      outline += re.sub('/', '-', match.split()[1].lower())+'/'+match.split()[0]+' '
  outtext += outline.strip()+'\n'
print(outtext.strip())

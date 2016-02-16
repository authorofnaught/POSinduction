#!/usr/local/bin/python3

import sys, codecs

# input: tagged text with one sentence per line and 'token/tag' format
# output: only the tags of the tagged text separated by whitespace and with one sentence per line

outfilename = '{}.tagsonly'.format(sys.argv[1])

with codecs.open(outfilename, 'w', encoding='utf-8') as outfile:
  with codecs.open(sys.argv[1], encoding='utf-8') as fn:
    for line in fn:
      outputline = ''
      for word in line.split():
        token, tag = word.split('/')
        outputline += '{} '.format(tag)
      outfile.write('{}\n'.format(outputline.rstrip()))

#!/usr/local/bin/python3

import sys

# Script for producing key used for 
# separating corpus into the training, 
# context, and testing datasets required by 
# Haghighi and Klein's code.


def get_split_text_key(textfile):

  with open(textfile) as f:
    sents = f.readlines()

  trainingCount = 0
  testingCount = 0

  with open('split_text.key','w') as key:
    for i, sent in enumerate(sents):

      if trainingCount < 5000 and i % 8 == 0 and len(sent) <= 200:
        trainingCount+=1
        key.write('{} {}\n'.format(i,'training'))
      elif testingCount < 2000 and i % 8 == 1 and len(sent) <= 200:
        testingCount+=1
        key.write('{} {}\n'.format(i,'testing'))
      else:
        key.write('{} {}\n'.format(i,'context'))



if __name__ == '__main__':

  get_split_text_key(sys.argv[1])

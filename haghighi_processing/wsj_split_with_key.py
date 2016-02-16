#!/usr/local/bin/python3

import sys

# Using the key produced by make_split_key.ps, 
# This scripts splits a corpus into the training, 
# context, snd testing datasets required by the 
# Haghighi and Klein code. 

def split_text(keyfile, textfile):

  key = {}
  with open(keyfile) as f:
    keys = f.readlines()

  with open(textfile) as f:
    sents = f.readlines()

  for k in keys:
    key[int(k.split()[0])] = k.split()[1]

  context = open('context_data.txt','w')
  training = open('train_data.txt','w')
  testing = open('test_data.txt','w')

  for i, sent in enumerate(sents):

    if key[i] == 'training':
      training.write(sent)
    elif key[i] == 'testing':
      testing.write(sent)
    elif key[i] == 'context':
      context.write(sent)
    else:
      print("something went wrong with the keys...")
      exit(1)

  context.close()
  training.close()
  testing.close()  


if __name__ == '__main__':

  split_text(sys.argv[1], sys.argv[2])

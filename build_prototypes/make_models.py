#!/usr/local/bin/python3

import sys, gensim, logging
from gensim.models import Word2Vec

# input = ospl untagged text; basename for output files
# output = two pickled word2vec models: cbow and skipgram
def makeModels(textfile, outputstring):

  logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

  f = open(textfile) 
  lines = f.readlines()
  f.close()

  sentences = []
  for line in lines:
    sentences.append(list(line.split()))

  model = Word2Vec(sentences, min_count=0, sg=0)
  model.save('{}.cbow.model'.format(outputstring))

  model = Word2Vec(sentences, min_count=0, sg=1)
  model.save('{}.skipgram.model'.format(outputstring))



if __name__ == '__main__':
  makeModels(sys.argv[1], sys.argv[2])

  

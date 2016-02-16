#!/usr/local/bin/python3

import sys, gensim, logging, os
from gensim.models import Word2Vec
from collections import Counter, defaultdict
import Clustering

# Script for producing prototypes from a corpus based on 
# certain criteria. As input, the script requires the raw text,
# a CBOW Word2Vec model, a SkipGram Word2Vec model, the 
# clustered output from brown92 or clark03, and a name for 
# the dataset, in that order.



class CosSim:

  def __init__(self, word, cossim):
    self.word = word
    self.cossim = cossim




def findPrototypes(raw_text, cbow_model, skipgram_model, clusters, dataset_name):

  cbow = Word2Vec.load(cbow_model)
  skipgram = Word2Vec.load(skipgram_model)
  cl = Clustering.Clustering(clusters)
  clusteredCounts = defaultdict(Counter)
  with open(raw_text) as f:
    text = f.read()
    for word in text.split():
      clusteredCounts[cl.word2cluster[word]][word]+=1

  dirname = '{}/prototypes/{}'.format(dataset_name, os.path.basename(clusters))
  if not os.path.exists(dirname):
    os.mkdir(dirname)

  C3 = open('{}/C_3'.format(dirname), 'w')
  C5 = open('{}/C_5'.format(dirname), 'w') 
  C7 = open('{}/C_7'.format(dirname), 'w') 
  Ccb3 = open('{}/C_cosCBOW_3'.format(dirname), 'w') 
  Ccb5 = open('{}/C_cosCBOW_5'.format(dirname), 'w') 
  Ccb7 = open('{}/C_cosCBOW_7'.format(dirname), 'w') 
  Csg3 = open('{}/C_cosSG_3'.format(dirname), 'w') 
  Csg5 = open('{}/C_cosSG_5'.format(dirname), 'w') 
  Csg7 = open('{}/C_cosSG_7'.format(dirname), 'w') 
  cb3 = open('{}/cosCBOW_3'.format(dirname), 'w') 
  cb5 = open('{}/cosCBOW_5'.format(dirname), 'w') 
  cb7 = open('{}/cosCBOW_7'.format(dirname), 'w') 
  sg3 = open('{}/cosSG_3'.format(dirname), 'w') 
  sg5 = open('{}/cosSG_5'.format(dirname), 'w') 
  sg7 = open('{}/cosSG_7'.format(dirname), 'w') 


  ####### Write prototypes based on counts
  for c in cl.cluster2word:
    clist = clusteredCounts[c].most_common(7)
    C3.write('{}\t{}\t{}\t{}\n'.format(c, clist[0][0], clist[1][0], clist[2][0]))
    C5.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(c, clist[0][0], clist[1][0], clist[2][0], clist[3][0], clist[4][0]))
    C7.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(c, clist[0][0], clist[1][0], clist[2][0], clist[3][0], clist[4][0], clist[5][0], clist[6][0]))
  print('\tCount prototype files written...')

  ####### Write prototypes based on counts and cosine similarities
  for c in cl.cluster2word:
    seed = clusteredCounts[c].most_common(1)[0][0]
    cossims = []
    for word in cl.cluster2word[c]:
      try:
        sim = cbow.similarity(seed, word)
      except:
        sim = 0.0
      cossim = CosSim(word, sim)
      cossims.append(cossim)
    cossims.sort(key=lambda x: x.cossim, reverse=True)
    clist = cossims[:7]
    Ccb3.write('{}\t{}\t{}\t{}\n'.format(c, clist[0].word, clist[1].word, clist[2].word))
    Ccb5.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(c, clist[0].word, clist[1].word, clist[2].word, clist[3].word, clist[4].word))
    Ccb7.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(c, clist[0].word, clist[1].word, clist[2].word, clist[3].word, clist[4].word, clist[5].word, clist[6].word))
    
    seed = clusteredCounts[c].most_common(1)[0][0]
    cossims = []
    for word in cl.cluster2word[c]:
      try:
        sim = skipgram.similarity(seed, word)
      except:
        sim = 0.0
      cossim = CosSim(word, sim)
      cossims.append(cossim)
    cossims.sort(key=lambda x: x.cossim, reverse=True)
    clist = cossims[:7]
    Csg3.write('{}\t{}\t{}\t{}\n'.format(c, clist[0].word, clist[1].word, clist[2].word))
    Csg5.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(c, clist[0].word, clist[1].word, clist[2].word, clist[3].word, clist[4].word))
    Csg7.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(c, clist[0].word, clist[1].word, clist[2].word, clist[3].word, clist[4].word, clist[5].word, clist[6].word))
  print('\tCount-cosine prototype files written...')

  ####### Write prototypes based on cosine similarities
  for i, c in enumerate(cl.cluster2word):
    print('\t\tcluster#{} numWords={}'.format(i, len(cl.cluster2word[c])))
    maxSim = 0.0
    seed = ''
    for w1 in cl.cluster2word[c]:
      sim = 0.0
      for w2 in cl.cluster2word[c]:
        try:
          sim += cbow.similarity(w1,w2)
        except:
          sim += 0.0
      if sim > maxSim:
        maxSim = sim
        seed = w1
    print('\t\t\tcbow seed = {}'.format(seed))

    cossims = []
    for word in cl.cluster2word[c]:
      try:
        sim = cbow.similarity(seed, word)
      except:
        sim = 0.0
      cossim = CosSim(word, sim)
      cossims.append(cossim)
    cossims.sort(key=lambda x: x.cossim, reverse=True)
    clist = cossims[:7]
    cb3.write('{}\t{}\t{}\t{}\n'.format(c, clist[0].word, clist[1].word, clist[2].word))
    cb5.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(c, clist[0].word, clist[1].word, clist[2].word, clist[3].word, clist[4].word))
    cb7.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(c, clist[0].word, clist[1].word, clist[2].word, clist[3].word, clist[4].word, clist[5].word, clist[6].word))
    
    maxSim = 0.0
    seed = ''
    for w1 in cl.cluster2word[c]:
      sim = 0.0
      for w2 in cl.cluster2word[c]:
        try:
          sim += skipgram.similarity(w1,w2)
        except:
          sim += 0.0
      if sim > maxSim:
        maxSim = sim
        seed = w1
    print('\t\t\tskipgram seed = {}'.format(seed))

    cossims = []
    for word in cl.cluster2word[c]:
      try:
        sim = skipgram.similarity(seed, word)
      except:
        sim = 0.0
      cossim = CosSim(word, sim)
      cossims.append(cossim)
    cossims.sort(key=lambda x: x.cossim, reverse=True)
    clist = cossims[:7]
    sg3.write('{}\t{}\t{}\t{}\n'.format(c, clist[0].word, clist[1].word, clist[2].word))
    sg5.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(c, clist[0].word, clist[1].word, clist[2].word, clist[3].word, clist[4].word))
    sg7.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(c, clist[0].word, clist[1].word, clist[2].word, clist[3].word, clist[4].word, clist[5].word, clist[6].word))
  print('\tCosine similarity prototype files written...')

  ####### Close all files and finish
  C3.close()
  C5.close()
  C7.close()
  Ccb3.close()
  Ccb5.close()
  Ccb7.close()
  Csg3.close()
  Csg5.close()
  Csg7.close()
  cb3.close()
  cb5.close()
  cb7.close()
  sg3.close()
  sg5.close()
  sg7.close()



if __name__ == '__main__':
  findPrototypes(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

  

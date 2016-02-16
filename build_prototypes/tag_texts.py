#!/usr/local/bin/python3

import os, sys, pickle, codecs
from collections import defaultdict
from os.path import splitext
import Clustering

# This script produces tagged texts for all experiments.
# Gold standard tagged texts are produced as well texts 
# tagged with 45 tags and texts tagged with 13 tags.


tagmap = {
          'CD':'NUM'
          ,'JJ':'ADJ','JJR':'ADJ','JJS':'ADJ','PRP$':'ADJ','$':'ADJ','#':'ADJ','POS':'ADJ'
          ,'CC':'CONJ'
#          ,'POS':'POS'
          ,'RP':'PRT'
          ,'TO':'TO'
          ,'MD':'V','VBD':'V','VBP':'V','VB':'V','VBZ':'V','VBG':'V','VBN':'V'
          ,'RB':'ADV','RBR':'ADV','RBS':'ADV'
          ,'DT':'DET','PDT':'DET'
          ,'EX':'N','FW':'N','NN':'N','NNP':'N','NNPS':'N','NNS':'N','PRP':'N'
          ,'IN':'PREP'
          ,'WDT':'W','WP':'W','WP$':'W','WRB':'W'
          ,'.':'PUNCT','``':'PUNCT',"''":'PUNCT','(':'PUNCT',')':'PUNCT'
          ,',':'PUNCT',':':'PUNCT','LS':'PUNCT','SYM':'PUNCT','UH':'PUNCT'
          ,'-LRB-':'PUNCT','-RRB-':'PUNCT'
          }



def make_tagged_texts(orderfile, b45clusterfile, b13clusterfile, c45clusterfile, c13clusterfile, outputfilename):

  b45cl = Clustering.Clustering(b45clusterfile)
  b13cl = Clustering.Clustering(b13clusterfile)
  c45cl = Clustering.Clustering(c45clusterfile)
  c13cl = Clustering.Clustering(c13clusterfile)

  tokenlist = []
  with codecs.open(orderfile,'r',encoding='utf8') as f:
    tokenlist = f.readlines()

  gold45out = open(outputfilename+'.45.gold','w')
  b45out = open(outputfilename+'.45.brown92','w')
  c45out = open(outputfilename+'.45.clark03','w')
  gold13out = open(outputfilename+'.13.gold','w')
  b13out = open(outputfilename+'.13.brown92','w')
  c13out = open(outputfilename+'.13.clark03','w')
  justtokenout = open(outputfilename+'.justtokens','w')
  
  gold45line = ''
  b45line = ''
  c45line = ''
  gold13line = ''
  b13line = ''
  c13line = ''
  justtokenline = ''
  for i, tokenline in enumerate(tokenlist):
    if '=====' in tokenline.split()[0] or i == len(tokenlist):
      gold45out.write(gold45line.strip()+'\n')
      b45out.write(b45line.strip()+'\n')
      c45out.write(c45line.strip()+'\n')
      gold13out.write(gold13line.strip()+'\n')
      b13out.write(b13line.strip()+'\n')
      c13out.write(c13line.strip()+'\n')
      justtokenout.write(justtokenline.strip()+'\n')
      gold45line = ''
      b45line = ''
      c45line = ''
      gold13line = ''
      b13line = ''
      c13line = ''
      justtokenline = ''
    else:
      token = tokenline.split()[0]
      try:
        tagmap[tokenline.split()[1]]
        gold45tag = tokenline.split()[1]
      except:
        gold45tag = 'UNK'
      try:
        gold13tag = tagmap[gold45tag]
      except:
        gold13tag = 'UNK'
      b45cluster = b45cl.word2cluster[token]
      c45cluster = c45cl.word2cluster[token]
      b13cluster = b13cl.word2cluster[token]
      c13cluster = c13cl.word2cluster[token]

      gold45line += '{}/{} '.format(token, gold45tag)
      b45line += '{}/{} '.format(token, b45cluster)
      c45line += '{}/{} '.format(token, c45cluster)
      gold13line += '{}/{} '.format(token, gold13tag)
      b13line += '{}/{} '.format(token, b13cluster)
      c13line += '{}/{} '.format(token, c13cluster)
      justtokenline += '{} '.format(token)

  gold45out.close()
  b45out.close()
  c45out.close()
  gold13out.close()
  b13out.close()
  c13out.close()
  justtokenout.close()



if __name__ == '__main__':

  make_tagged_texts(sys.argv[1],sys.argv[2],sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])


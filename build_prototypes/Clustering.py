#!/usr/local/bin/python3

from collections import defaultdict
from os.path import splitext
import codecs

class Clustering:

  def __init__(self, clusterfile):

    self.word2cluster = {}
    self.cluster2word = defaultdict(list)

    if clusterfile.endswith('brown92'):
      clusterNum = 0
      clusterNums = {}
      with codecs.open(clusterfile, 'r', encoding='utf8') as fn:
        for line in fn.readlines():
          word = line.split()[1]
          clusterID = line.split()[0]
          if clusterID not in clusterNums:
            clusterNums[clusterID] = clusterNum
            clusterNum+=1
          self.word2cluster[word] = clusterNums[clusterID]
          self.cluster2word[clusterNums[clusterID]].append(word)

    elif clusterfile.endswith('clark03'):
      with codecs.open(clusterfile, 'r', encoding='utf8') as fn:
        for line in fn.readlines():
          word = line.split()[0]
          clusterID = line.split()[1]
          if 'e' not in clusterID:
            self.word2cluster[word] = clusterID
            self.cluster2word[clusterID].append(word)

    else:
      print('Neither brown nor clark clustering have we here.')

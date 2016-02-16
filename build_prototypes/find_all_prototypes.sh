#!/bin/bash

# Runs the find_prototypes.py script for all systems and 
# over all numbers of clusters.

clusters="13.brown92 13.clark03 45.brown92 45.clark03"

for cl in ${clusters}; do
  ./find_prototypes.py wsj/text/owpl.notags wsj/models/cbow.model wsj/models/skipgram.model wsj/clusters/${cl} wsj 
done

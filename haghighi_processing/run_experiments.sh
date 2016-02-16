#!/bin/bash

# Script for running all experiments using 
# Haghighi and Klein's code.

confdir="conf/wsj"
outputdir="output/wsj"
clusternames="45.brown92 13.brown92 45.clark03 13.clark03"
prototypes="C_3 C_5 C_7 C_cosCBOW_3 C_cosCBOW_5 C_cosCBOW_7 C_cosSG_3 C_cosSG_5 C_cosSG_7 cosCBOW_3 cosCBOW_5 cosCBOW_7 cosSG_3 cosSG_5 cosSG_7"

for cl in ${clusternames}; do
  for pr in ${prototypes}; do
    echo
    echo
    echo
    echo
    echo "TRAINING cluster=${cl} prototypes=${pr}"
    echo
    echo
    ./scripts/train_seq_model.rb ${confdir}/${cl}/train/${pr}.conf 
    sleep 5

  done
done


for cl in ${clusternames}; do
  for pr in ${prototypes}; do

    echo
    echo
    echo
    echo
    echo "TESTING/TAGGING cluster=${cl} prototypes=${pr}"
    echo
    echo
    ./scripts/test_seq_model.rb ${confdir}/${cl}/test/${pr}.conf 
    sleep 5

  done
done


for cl in ${clusternames}; do
  for pr in ${prototypes}; do

    ./trade_delimiters.sh < ${outputdir}/${cl}/${pr}/test_data.txt.tagged > ${outputdir}/${cl}/${pr}/data_slashdelim.tagged

  done
done

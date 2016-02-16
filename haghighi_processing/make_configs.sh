#!/bin/bash

# A script for creating all necessary config files 
# for experiments using Haghighi and Klein's script.

workingdir="/Users/authorofnaught/Projects/POSinduction/haghighi_prototypes/psmt"
datadir="data/wsj"
confdir="conf/wsj"
modeldir="models/wsj"
outputdir="output/wsj"
protodir="protoFiles/wsj"
clusternames="45.brown92 13.brown92 45.clark03 13.clark03"
prototypes="C_3 C_5 C_7 C_cosCBOW_3 C_cosCBOW_5 C_cosCBOW_7 C_cosSG_3 C_cosSG_5 C_cosSG_7 cosCBOW_3 cosCBOW_5 cosCBOW_7 cosSG_3 cosSG_5 cosSG_7"

for cl in ${clusternames}; do
  rm -fr ${workingdir}/${confdir}/${cl}/
  mkdir -p ${workingdir}/${confdir}/${cl}/train
  mkdir -p ${workingdir}/${confdir}/${cl}/test
done

for cl in ${clusternames}; do
  for pr in ${prototypes}; do

    train="${workingdir}/${confdir}/${cl}/train/${pr}.conf"
    test="${workingdir}/${confdir}/${cl}/test/${pr}.conf"

    echo "dataRoot	${datadir}" > $train
    echo "prefix	train" >> $train
    echo "protoFile	${protodir}/${cl}/${pr}" >> $train
    echo "extension	txt" >> $train
    echo "simModelPath	models/wsj/sim.model" >> $train
    echo "order	1" >> $train
    echo "numCPUs	2" >> $train
    echo "numIters	50" >> $train
    echo "minIters	10" >> $train
    echo "sigmaSquared	0.5" >> $train
    echo "useSuffixFeatures" >> $train
    echo "useInitialCapital" >> $train
    echo "useHasDigit" >> $train
    echo "useHasHyphen" >> $train
    echo "outfile	${modeldir}/${cl}/${pr}_seq.model" >> $train

    echo "modelPath	${modeldir}/${cl}/${pr}_seq.model" > $test
    echo "inPrefix	test" >> $test
    echo "inDirRoot	${datadir}/" >> $test
    echo "inExtension	.txt" >> $test
    echo "outDir	${outputdir}/${cl}/${pr}/" >> $test
    echo "outExtension	.tagged" >> $test

  done
done





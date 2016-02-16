#!/bin/bash

#
# Concatenates all files from the tagged wsj portion of PTB3 
# into a single file for further processing.
#

datadir="/Users/authorofnaught/Data/TREEBANK_3/parsed/mrg/wsj/"
dirnames="00/ 01/ 02/ 03/ 04/ 05/ 06/ 07/ 08/ 09/ 10/ 11/ 12/ 13/ 14/ 15/ 16/ 17/ 18/ 19/ 20/ 21/ 22/ 23/ 24/"


outfile="wsj.parsed"

for dirname in ${dirnames}; do

  filenames=$(ls ${datadir}${dirname})

  for filename in ${filenames}; do

    cat ${datadir}${dirname}${filename}  >> $outfile

  done
done 

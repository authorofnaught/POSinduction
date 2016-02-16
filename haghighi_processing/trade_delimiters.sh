#!/bin/bash

# Script for trading the ## used to delimit tokens from 
# tags in Haghighi and Klein's output with / so that 
# the output can be tested using the Christodoulopoulos 
# evaluation code.

sed 's:\([^[:space:]]\)##\([^[:space:]]\):\1/\2:g'

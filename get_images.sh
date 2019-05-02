#!/bin/bash

# This script is created to check the algorithm on multimple examples

for i in $(ls input/); 
do 
	echo $i;

	python main.py "input/$i" "output/$i" > /dev/null; 
done;

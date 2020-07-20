#!/bin/bash
my_file='last_gold.gold_conll'
#for TW
separetor='\t'
#for ONTO
#separetor=' '
if [[ `tail -1 "$my_file"` =~ "#begin" ]];  then echo " "; else  echo "#begin document">>$my_file; fi
python stats.py $my_file $separetor
exit
#!/bin/bash

#criar vetor com a condição inicial do log_map.

#gcc -o3 -Wall VisibilityGraphQM.c -lm -o VisibilityGraphQM
r=(3.5 3.56995 3.857 3.87 3.89 4.00)
gcc -o3 -Wall VisibilityGraphQM.c -lm -o VisibilityGraphQM


for ((i=2;i<=5;i++)) 

do
 

for ((j=0; j<=2000; j++))
do
	echo $j $j ${r[i]} 0.1 
	./VisibilityGraphQM $j $j ${r[i]} 0.1 


done

done



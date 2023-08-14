#!/bin/bash


r=(3.5 3.56995 3.857 3.87 3.89 4.00)

gcc VisibilityGraphQM.c -lm -o VisibilityGraphQM


for ((i=0;i<=5;i++))

do

for ((j=2;j<=4000;j++))

do


	./VisibilityGraphQM $j $j  ${r[i]} 0.1

done

done


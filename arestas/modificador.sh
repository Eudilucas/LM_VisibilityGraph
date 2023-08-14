#!/bin/bash

cd

cd ~/Desktop/IC/caos/arestas/LM_p1/
for ((i=0;i<4000;i++))

do

cut -c 1,3,4 $i.txt > /home/eude/Desktop/IC/caos/arestas/LM_p1/p1_$i.txt
done



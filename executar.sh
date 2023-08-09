#!/bin/bash


r=(3.5 3.56995 3.857 3.87 3.89 4.00)

gcc VisibilityGraphQM.c -lm -o VisibilityGraphQM


for ((i=0;i<=5;i++))

do



#for ((j=62500;j<=65000;j++))

#do

if [ $i -eq 0 ]; then
	./VisibilityGraphQM 60000 60000  ${r[i]} 0.1 > ~/Desktop/IC/caos/histograma/LM_p1/hist/$j.dat

fi

if [ $i -eq 1 ]; then
	./VisibilityGraphQM 60000 60000 ${r[i]} 0.1 > ~/Desktop/IC/caos/histograma/LM_fbp/hist/$j.dat
fi

if [ $i -eq 2 ]; then
	./VisibilityGraphQM 60000 60000 ${r[i]} 0.1 > ~/Desktop/IC/caos/histograma/LM_int/hist/$j.dat
fi


if [ $i -eq 3 ]; then
	./VisibilityGraphQM 60000 60000 ${r[i]} 0.1 > ~/Desktop/IC/caos/histograma/LM_c1/hist/$j.dat
fi

if [ $i -eq 4 ]; then
	./VisibilityGraphQM 60000 60000 ${r[i]} 0.1 > ~/Desktop/IC/caos/histograma/LM_c2/hist/$j.dat
fi

if [ $i -eq 5 ]; then
	./VisibilityGraphQM 60000 60000 ${r[i]} 0.1 > ~/Desktop/IC/caos/histograma/LM_fc/hist/$j.dat
fi


#done

done


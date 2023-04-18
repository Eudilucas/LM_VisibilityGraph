#!/bin/bash

#cd Área\ de\ Trabalho/projeto
gcc -o3 -Wall VisibilityGraphQM.c -lm -o VisibilityGraphQM

#periodico
for (( i=0; i<=2001; i++ )) #MUDAR PARA DEFINIR O LIMITE DO NUMERO DE VERTICES
do
#aqui deve começar o loop
	./VisibilityGraphQM $i $i 3.5 0.1 
	python3 part_2.py >> dados/log_map/periodico_2000.txt #Nome do novo arquivo txt  
done
#aqui deve acabar o loop

'''
#feigenbaum
for (( i=0; i<=2001; i++ )) #MUDAR PARA DEFINIR O LIMITE DO NUMERO DE VERTICES
do

	./VisibilityGraphQM $i $i 3.56995 0.1 
	python3 part_2.py >> dados/log_map/intermitente_i_2000.txt #Nome do novo arquivo txt  
done


#intermitencia
for (( i=0; i<=2001; i++ )) #MUDAR PARA DEFINIR O LIMITE DO NUMERO DE VERTICES
do

	./VisibilityGraphQM $i $i 3.82484 0.1 
	python3 part_2.py >> dados/log_map/intermitente_i_2000.txt #Nome do novo arquivo txt  
done


#fullcaotico
for (( i=0; i<=2001; i++ )) #MUDAR PARA DEFINIR O LIMITE DO NUMERO DE VERTICES
do

	./VisibilityGraphQM $i $i 3.82484 0.1 
	python3 part_2.py >> dados/log_map/fullcaotico_i_2000.txt #Nome do novo arquivo txt  
done
'''
#parametros:


#r = 3.5 - periodico ok
#r = 3.56995 - feigenbaum ok
#r = 3.82484 - intermitente_i ok
#r = 4.00 - Fullchaos ok

#parametros não testados
#r = 3.87 - chaos_1 
#r = 3.89 - chaos_2

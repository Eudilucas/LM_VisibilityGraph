#!/bin/bash

# Gerar nome do arquivo para programa em C
c_filename="c-$(date +'%Y-%m-%d_%H-%M-%S').c"
echo "Nome do arquivo para programa em C: $c_filename"

# Gerar nome do arquivo para programa em Python
py_filename="py-$(date +'%Y-%m-%d_%H-%M-%S').py"
echo "Nome do arquivo para programa em Python: $py_filename"

# Compilar programa em C
gcc -o3 -Wall VisibilityGraphQM.c -lm -o VisibilityGraphQM

#periodico
for (( i=0; i<=2001; i++ )) #MUDAR PARA DEFINIR O LIMITE DO NUMERO DE VERTICES
do
#aqui deve começar o loop
	./VisibilityGraphQM $i $i 3.5 0.1 

	python3 part_2.py >> "dados/log_map/periodico_${py_filename%.*}.txt" #Nome do novo arquivo txt  

done
#aqui deve acabar o loop
#/home/eude/Desktop/IC/caos/espectral

#OBJETIVO: Fazer o script colocar os dados dos autovalores em cada diretorio.

#feigenbaum
for (( i=0; i<=2001; i++ )) #MUDAR PARA DEFINIR O LIMITE DO NUMERO DE VERTICES
do
	./VisibilityGraphQM $i $i 3.56995 0.1 
	python3 part_2.py >> "dados/log_map/feigenbaum_${py_filename%.*}.txt" #Nome do novo arquivo txt  
done

#intermitencia
for (( i=0; i<=2001; i++ )) #MUDAR PARA DEFINIR O LIMITE DO NUMERO DE VERTICES
do
	./VisibilityGraphQM $i $i 3.82484 0.1 
	python3 part_2.py >> "dados/log_map/intermitente_${py_filename%.*}.txt" #Nome do novo arquivo txt  
done

#fullcaotico
for (( i=0; i<=2001; i++ )) #MUDAR PARA DEFINIR O LIMITE DO NUMERO DE VERTICES
do
	./VisibilityGraphQM $i $i 4.0 0.1 
	python3 part_2.py >> "dados/log_map/fullcaotico_${py_filename%.*}.txt" #Nome do novo arquivo txt  
done


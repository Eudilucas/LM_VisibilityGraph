import networkx as nx
import numpy as np


def diretorio(caso, nome):
	matriz = '/home/pc/Desktop/IC/caos/arestas'
	casos = ['/LM_p1','LM_int','LM_fbp','LM_c1','LM_c2','LM_fc']
	barra = '/'
	tipo = '.txt'
	
	
	nome = str(nome)
	caso = float(caso)
	
	string=''
	
	if (caso == 3.5):
		string = str(matriz+casos[0]+barra+nome+tipo)
	elif (caso == 3.56995):
		string = str(matriz+casos[1]+barra+nome+tipo)
	elif (caso == 3.857):
		string = str(matriz+casos[2]+barra+nome+tipo)
	elif (caso == 3.87):
		string = str(matriz+casos[3]+barra+nome+tipo)
	elif (caso == 3.89):
		string = str(matriz+casos[4]+barra+nome+tipo)
	elif (caso == 4):
		string = str(matriz+casos[5]+barra+nome+tipo)
	else:
		print("Caso invalido")

	return string

pasta = diretorio(3.5,100)
arq =open(pasta, 'r')

vec=arq.readlines()

for i in range(len(vec)):
	vec[i]=vec[i].split(",")


for i in range(len(vec)):
	for j in range(2):
		vec[i][j]=float(vec[i][j])
		#print(vec[i][j])	

G=nx.Graph()


G.add_edges_from(vec)

A=nx.adjacency_spectrum(G)
B=np.real(max(A))
print(B)

arq.seek(0)
arq.close()

#lendo todo o arquivo e deixando apenas a parte real



import matplotlib.pyplot as plt
import numpy as np
import networkx as nx


def mostrar_matriz(A):
	
	for i in range(len(A)):
		for j in range(len(A[0])):
			print(A[i][j], end = " ")
		print("\n")

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
arq =open(pasta, "r")


vec=arq.readlines() #Transformando cada linha em entradas da lista

for i in range(len(vec)):
	vec[i]=vec[i].split(",") #quebrando cada todas as linhas até onde tem virgula
arq.seek(0)

for i in range(len(vec)):
	for j in range(2):
		vec[i][j]=float(vec[i][j])#convertendo os valores em float e adicionando ao array vec



G=nx.Graph(vec)

#tam = len(nx.cliques_containing_node(G))


a=float(nx.average_shortest_path_length(G))

tam = len(nx.cliques_containing_node(G))

arq.seek(0)
arq.close()


#anexar os pontos a um novo arquivo 
arq = open("caminho/pontos.txt","a")

arq.write(str(tam) + ", " + str(a)+"\n")
arq.seek(0)
arq.close()

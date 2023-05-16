import matplotlib.pyplot as plt
import numpy as np
import networkx as nx


def mostrar_matriz(A):
	
	for i in range(len(A)):
		for j in range(len(A[0])):
			print(A[i][j], end = " ")
		print("\n")


arq =open("arestas/LM_periodico_10000.txt", "r") #Abrindo arquivo no modo leitura

#arestas/LM_periodic.txt
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

import networkx as nx
import numpy as np

arq =open("LM_fullcaos.txt", 'r')

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



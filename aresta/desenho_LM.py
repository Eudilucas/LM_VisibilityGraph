import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv



arq =open("LM_fullcaos.txt", 'r') #Abrindo arquivo no modo leitura

vec=arq.readlines() #Transformando cada linha em entradas da lista

for i in range(len(vec)):
	vec[i]=vec[i].split(",") #quebrando cada todas as linhas até onde tem virgula
arq.seek(0)

for i in range(len(vec)):
	for j in range(2):
		vec[i][j]=float(vec[i][j])#convertendo os valores em float e adicionando ao array vec


G=nx.Graph(vec)
#pos = nx.kamada_kawai_layout(G)
#pos = nx.spectral_layout(G)
#pos = nx.nx_agraph.graphviz_layout(G, prog="twopi", args="")

options = {
#    "font_size": 0.2,
    "node_size": 25,
    "node_color": "black",
    "edgecolors": "white",
    "linewidths": 0.25,
    "width": 0.25,}

nx.draw(G, **options)
plt.axis("equal")

plt.draw()  # pyplot draw()
plt.show()





arq.seek(0)
arq.close()


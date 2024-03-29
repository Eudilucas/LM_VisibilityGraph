import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv
'''
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
	
a = float(input('Digite o caso'))
b = int(input('Digite o tamanho do arquivo txt'))
	
pasta = diretorio(a, b)
'''
arq =open('/home/pc/Desktop/IC/caos/exemplos/exem_matriz.txt', 'r') #Abrindo arquivo no modo leitura

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
    "font_size": 10,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
    "with_labels": True,
    "font_weight":'bold'}

nx.draw(G, **options, )
plt.axis("equal")

plt.draw()  # pyplot draw()
plt.show()


arq.seek(0)
arq.close()


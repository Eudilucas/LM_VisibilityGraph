#plot de todos os autovalores em função de v(vertices)
#um para cada rede.

import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

def diretorio(matriz,caso, nome):
	matriz1 = '/home/pc/Desktop/IC/caos/arestas'
	matriz2 = '/home/pc/Desktop/IC/caos/m_complex/espectral'
	casos = ['/LM_p1','LM_int','LM_fbp','LM_c1','LM_c2','LM_fc']
	
	barra = '/'
	autovalor = 'autovalor'
	tipo = '.txt'
	
	

	nome = str(nome)
	caso = float(caso)
	matriz = int(matriz)

	string=''

	if (matriz == 0):
		
		if (caso == 3.5):
			string = str(matriz1+casos[0]+barra+nome+tipo)
		elif ((caso - 3.56995)<0.000001):
			string = str(matriz1+casos[1]+barra+nome+tipo)
		elif ((caso - 3.857)<0.0001):
			string = str(matriz1+casos[2]+barra+nome+tipo)
		elif ((caso - 3.87)<0.001):
			string = str(matriz1+casos[3]+barra+nome+tipo)
		elif ((caso - 3.89)<0.001):
			string = str(matriz1+casos[4]+barra+nome+tipo)
		elif (caso == 4):
			string = str(matriz1+casos[5]+barra+nome+tipo)
		else:
			print("Caso invalido")

	if (matriz == 1):
			
		if (caso == 3.5):
			string = str(matriz2+casos[0]+barra+nome+tipo)
		elif ((caso - 3.56995)<0.000001):
			string = str(matriz2+casos[1]+barra+nome+tipo)
		elif ((caso - 3.857)<0.0001):
			string = str(matriz2+casos[2]+barra+nome+tipo)
		elif ((caso - 3.87)<0.001):
			string = str(matriz2+casos[3]+barra+nome+tipo)
		elif ((caso - 3.89)<0.001):
			string = str(matriz2+casos[4]+barra+nome+tipo)
		elif (caso == 4):
			string = str(matriz2+casos[5]+barra+nome+tipo)
		else:
			print("Caso invalido")


	return string

a = float(input('Digite o caso '))
b = int(input('Digite o tamanho do arquivo txt '))


pasta = diretorio(0, a, b)

arq = open(pasta, "r")

vec=arq.readlines()

for i in range(len(vec)):
	vec[i]=vec[i].split(",")


for i in range(len(vec)):
	for j in range(2):
		vec[i][j]=float(vec[i][j])
	

G=nx.Graph()


G.add_edges_from(vec)

A=nx.adjacency_spectrum(G)
B=np.real(A)



arq.seek(0)
arq.close()



pasta = diretorio(1, a, b)
print(pasta)
arquivo = open(pasta,'w')

for i in range(len(vec)):
	arquivo.write(str(B[i]))
	arquivo.write("\n")

arquivo.seek(0)
arquivo.close()


ptr = open(pasta,'r')

vec=ptr.readlines()

print(vec)

for i in range(len(vec)):
	
	vec[i]=float(vec[i]) 

n = np.arange(0,len(vec),1) 

plt.grid(True)
#plt.title("Autovalores em função dos vertices")
plt.xlabel("n° vertices")
lamb = "\u03BB"
plt.ylabel(lamb)
plt.plot(n,vec, color = 'k') 

plt.show()

arq.close()

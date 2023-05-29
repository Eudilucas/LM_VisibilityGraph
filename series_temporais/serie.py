import matplotlib.pyplot as plt
import numpy as np
import networkx as nx


def mostrar_matriz(A):
	
	for i in range(len(A)):
		for j in range(len(A[0])):
			print(A[i][j], end = " ")
		print("\n")

def diretorio(caso, nome):
	matriz = '/home/pc/Desktop/IC/caos/series_temporais'
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

pasta = diretorio(a,b)


arq =open(pasta, "r") #Abrindo arquivo no modo leitura


vec=arq.readlines() #Transformando cada linha em entradas da lista


for i in range(len(vec)):
	vec[i]=float(vec[i])


v=[]
for i in range(len(vec)):
	a=100*i
	v.append(a)

plt.grid(True)
#plt.title("Autovalores em função dos vertices")
plt.xlabel("t")

plt.ylabel("A(t)")
plt.plot(v,vec, "k-") #plotando um grafico de v por vec

plt.show()

arq.close()



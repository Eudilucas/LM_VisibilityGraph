import matplotlib.pyplot as plt
import numpy as np
import networkx as nx


def mostrar_matriz(A):
	
	for i in range(len(A)):
		for j in range(len(A[0])):
			print(A[i][j], end = " ")
		print("\n")


arq =open("series_temporais/aleatoria.txt", "r") #Abrindo arquivo no modo leitura


vec=arq.readlines() #Transformando cada linha em entradas da lista


for i in range(len(vec)):
	vec[i]=float(vec[i])

#print(vec)

'''
v=[]
for i in range(len(vec)):

	v.append(i) #criando um vetor do tamanho do arquivo 	
#print(v)
'''
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



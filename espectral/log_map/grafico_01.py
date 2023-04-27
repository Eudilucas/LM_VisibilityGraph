#plote

import matplotlib.pyplot as plt
import numpy as np

pont = open("dado_2000_2.txt","r")#abrindo arquivo para ler


vec = pont.readlines()#lendo todo o arquivo linha a linha e adicionando ao vetor vec

for i in range(len(vec)):
	
	vec[i]=float(vec[i])-1 #transformando a string em float

v =np.arange(0,len(vec),1) #criando um vetor do tamanho do arquivo 	

plt.grid(True)
#plt.title("Autovalores em função dos vertices")
plt.xlabel("n° vertices")
lamb = "\u03BB"
plt.ylabel(lamb)
plt.plot(v,vec, color = 'k') #plotando um grafico de v por vec

plt.show()
pont.close()



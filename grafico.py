#plote

import matplotlib.pyplot as plt
import numpy as np

pont = open("serie_temporal.txt","r")#abrindo arquivo para ler


vec = pont.readlines()#lendo todo o arquivo linha a linha e adicionando ao vetor vec


for i in range(len(vec)):
	vec[i]=float(vec[i])#transformando a string em float

pont.seek(0)

v=np.arange(0,len(vec),1) #criando um vetor do tamanho do arquivo 	

plt.grid(True)
#plt.title("Autovalores em função dos vertices")
plt.xlabel("tempo")

plt.ylabel("Serie temporal")
plt.plot(v,vec, "ko") #plotando um grafico de v por vec

plt.show()

pont.close()



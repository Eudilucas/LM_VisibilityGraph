import matplotlib.pyplot as plt


arq =open("distribuicao/deg_dist.dat", 'r') #Abrindo arquivo no modo leitura

vec=arq.readlines() #Transformando cada linha em entradas da lista

for i in range(len(vec)):
	vec[i]=vec[i].split(",") #quebrando cada todas as linhas até onde tem virgula
arq.seek(0)

for i in range(len(vec)):
	for j in range(2):
		vec[i][j]=float(vec[i][j])#convertendo os valores em float e adicionando ao array vec

arq.seek(0)

n=[[0]for i in range(len(vec))]
hist=[[0]for i in range(len(vec))]

for i in range(len(vec)):
	for j in range(2):
		if (j == 0):
			n[i]= vec[i][j]
		if (j==1):
			hist[i] = vec[i][j] 

print(n)
print(hist)
plt.xlabel("n")
plt.stem(n,hist)


plt.show()
arq.close()

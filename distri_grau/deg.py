import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def linear(x, a):
    return a*x

def lei_de_potencia(x,a,b):

	return a*x**b

arq = open("distribuicao/aleatorio.dat", 'r') # Abrindo arquivo no modo leitura

vec = arq.readlines() # Transformando cada linha em entradas da lista
for i in range(len(vec)):
	vec[i] = vec[i].split(",") # Quebrando cada todas as linhas até onde tem vírgula
arq.seek(0)
for i in range(len(vec)):
	for j in range(2):
		vec[i][j] = float(vec[i][j]) # Convertendo os valores em float e adicionando ao array vec

arq.seek(0)

k = []
p = []
#p_= []
print(p)
for i in range(len(vec)):
	for j in range(2):
		if j == 0:
			k.append(vec[i][j])
		if j == 1:
			p.append((vec[i][j]))
#			p_.append(vec[i][j])

x = np.array(k)
y = np.array(p)
#y_ = np.array(p_)

#popt, pcov = curve_fit(linear, x, y)

popt, pcov = curve_fit(linear, x, y)


fig, ax = plt.subplots()

x_plot = np.linspace(x.min(), x.max(), 1000)
y_plot = linear(x_plot, *popt)


plt.xlabel("k")
plt.ylabel("p(k)")
#ax.set_yscale("log")
#ax.set_xscale("log")
ax.plot(x, y, 'ro')

#ax.plot(x_plot, y_plot) # Usando a função semilogy para deixar apenas o eixo das ordenadas com o log
print(popt)


#plt.legend()
plt.show()


arq.close()
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def linear(x, a,b):
    return a*x+b

def lei_de_potencia(x,a,b):

	return a*x**b

def diretorio(caso, nome):
	matriz = '/home/eude/Desktop/IC/caos/distri_grau'
	casos = ['/LM_p1','/LM_int','/LM_fbp','/LM_c1','/LM_c2','/LM_fc']
	barra = '/'
	tipo = '.txt'
	
	
	nome = str(nome)
	caso = float(caso)
	
	string=''
	
	if (caso == 3.5):
		string = str(matriz+casos[0]+barra+nome+tipo)
	elif ((caso - 3.56995)<0.000001):
		string = str(matriz+casos[1]+barra+nome+tipo)
	elif ((caso - 3.857)<0.0001):
		string = str(matriz+casos[2]+barra+nome+tipo)
	elif ((caso - 3.87)<0.001):
		string = str(matriz+casos[3]+barra+nome+tipo)
	elif ((caso - 3.89)<0.001):
		string = str(matriz+casos[4]+barra+nome+tipo)
	elif (caso == 4):
		string = str(matriz+casos[5]+barra+nome+tipo)
	else:
		print("Caso invalido")

	return string

u = float(input('Digite um dos casos abaixo:\n 3.5 \n 3.56995 \n 3.857 \n 3.87 \n 3.89 \n 4.00 \n '))
v = int(input('Digite o tamanho do arquivo txt: '))

pasta = diretorio(u,v)

arq = open(pasta, 'r') 

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

x = np.log(np.array(k))
y = np.log(np.array(p))
#y_ = np.array(p_)

#popt, pcov = curve_fit(linear, x, y)

popt, pcov = curve_fit(linear, x, y)


fig, ax = plt.subplots()

x_plot = np.linspace(x.min(), x.max(), 2000)
y_plot = linear(x_plot, *popt)



plt.xlabel(r"$ln k$")
plt.ylabel(r"$ln p(k)$")
ax.plot(x, y, 'ro')
ax.plot(x_plot, y_plot, label=r'$\alpha$ = -1.41')

print(popt)


plt.legend()
plt.show()


arq.close()

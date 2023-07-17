import matplotlib.pyplot as plt
import numpy as np



def vetor(diretorio):
    data = np.loadtxt(diretorio, delimiter=',')
    x = data[:, 0]
    y = data[:, 1]
    return x, y

n=input('Digite o tamanho do arquivo: ')


n = str(n)


diretorio1 = '/home/eude/Desktop/IC/caos/distri_grau/LM_p1/' + n + '.txt'


x1, p1 = vetor(diretorio1)


x2 = []
fbp = []
diretorio2 = '/home/eude/Desktop/IC/caos/distri_grau/LM_fbp/' + n + '.txt'

x2, fbp =vetor(diretorio2)

x3 = []
intr = []
diretorio3 = '/home/eude/Desktop/IC/caos/distri_grau/LM_int/' + n + '.txt'
x3, intr =vetor(diretorio3)

x4 = []
c1 = []
diretorio4 = '/home/eude/Desktop/IC/caos/distri_grau/LM_c1/' + n + '.txt'
x4, c1=vetor(diretorio4)


x5 = []
c2 = []
diretorio5 = '/home/eude/Desktop/IC/caos/distri_grau/LM_c2/' + n + '.txt'
x5, c2=vetor(diretorio5)

x6 = []
fc = []
diretorio6 = '/home/eude/Desktop/IC/caos/distri_grau/LM_fc/' + n + '.txt'
x6, fc =vetor(diretorio6)


#Criar um array do tamanho do arquivo

		


#fazer o plote de todos os arquivos

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x1,p1,'-o',label = r"Periodic $\mu= 3.5$", markersize = 0.1)
ax.plot(x2,fbp,'-*',label= r'Feigenbaum point $\mu= 3.56995$',markersize = 0.1)
ax.plot(x3,intr,'-x',label= r'Intermittent $\mu= 3.857$',markersize = 0.1)
ax.plot(x4,c1,'-d',label= r'Chaos 1 $\mu=3.87$',markersize = 0.1)
ax.plot(x5,c2,'-v',label = r'Chaos 2 $\mu=3.89$',markersize = 0.1)
ax.plot(x6,fc,'-s',label = r'Full caos $\mu= 4.0$',markersize = 0.1)



#criar a legenda
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Distribuição de grau')
ax.grid(True)

ax.legend(title = n+' dados')

#Mostrar o grafico 
plt.show()

ax.figure.savefig('/home/eude/Desktop/IC/caos/distri_grau/grafico/'+n+'.png')

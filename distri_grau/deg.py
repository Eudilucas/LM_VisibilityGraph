import matplotlib.pyplot as plt
import numpy as np



def vetor(diretorio):
    data = np.loadtxt(diretorio, delimiter=',')
    x = data[:, 0]
    y = data[:, 1]
    return x, y

n=input('Qual o tamanho dos arquivos?\n')
    
n = str(n)


diretorio1 = '/home/pc/Desktop/IC/caos/distri_grau/LM_p1/' + n + '.txt'

x1, p1 = vetor(diretorio1)


x2 = []
fbp = []
diretorio2 = '/home/pc/Desktop/IC/caos/distri_grau/LM_fbp/' + n + '.txt'

x2, fbp =vetor(diretorio2)

x3 = []
intr = []
diretorio3 = '/home/pc/Desktop/IC/caos/distri_grau/LM_int/' + n + '.txt'
x3, intr =vetor(diretorio3)

x4 = []
c1 = []
diretorio4 = '/home/pc/Desktop/IC/caos/distri_grau/LM_c1/' + n + '.txt'
x4, c1=vetor(diretorio4)


x5 = []
c2 = []
diretorio5 = '/home/pc/Desktop/IC/caos/distri_grau/LM_c2/' + n + '.txt'
x5, c2=vetor(diretorio5)

x6 = []
fc = []
diretorio6 = '/home/pc/Desktop/IC/caos/distri_grau/LM_fc/' + n + '.txt'
x6, fc =vetor(diretorio6)


#Criar um array do tamanho do arquivo

		


#fazer o plote de todos os arquivos
plt.figure(figsize=(5,4),layout='constrained')
plt.plot(x1,p1,'-o',label ='periodic')
plt.plot(x2,fbp,'-*',label='feigenbaun point')
plt.plot(x3,intr,'-x', label='intermitente')
plt.plot(x4,c1,'-d', label='caos 1')
plt.plot(x5,c2,'-v', label = 'caos 2')
plt.plot(x6,fc,'-s',label = 'full caos')



#criar a legenda
plt.xlabel('x')
plt.ylabel('y')
plt.title('Distribuição de grau')
plt.grid(True)

plt.legend(title = n+' dados')

#Mostrar o grafico 
plt.show()

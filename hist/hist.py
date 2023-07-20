import matplotlib.pyplot as plt
import numpy as np

def vetor(diretorio):
    data = np.loadtxt(diretorio, delimiter=',')
    x = data[:, 0]
    y = data[:, 1]
    return x, y

n = input('Qual o tamanho dos arquivos?\n')
n = str(n)

diretorio1 = '/home/eude/Desktop/IC/caos/hist/LM_p1/' + n + '.txt'
x1, p1 = vetor(diretorio1)

x2 = []
fbp = []
diretorio2 = '/home/eude/Desktop/IC/caos/hist/LM_fbp/' + n + '.txt'
x2, fbp = vetor(diretorio2)

x3 = []
intr = []
diretorio3 = '/home/eude/Desktop/IC/caos/hist/LM_int/' + n + '.txt'
x3, intr = vetor(diretorio3)

x4 = []
c1 = []
diretorio4 = '/home/eude/Desktop/IC/caos/hist/LM_c1/' + n + '.txt'
x4, c1 = vetor(diretorio4)

x5 = []
c2 = []
diretorio5 = '/home/eude/Desktop/IC/caos/hist/LM_c2/' + n + '.txt'
x5, c2 = vetor(diretorio5)

x6 = []
fc = []
diretorio6 = '/home/eude/Desktop/IC/caos/hist/LM_fc/' + n + '.txt'
x6, fc = vetor(diretorio6)

#fig, axs = plt.subplots(3, 2)

fig, axs = plt.subplots(1, 2)

largura_barras = 2

axs[0].bar(x1, p1, width = largura_barras)
axs[0].set_title('Periodic')

'''
axs[1, 0].bar(x2, fbp)
axs[1, 0].set_title('Feigenbaun Point')

axs[2, 0].bar(x3, intr)
axs[2, 0].set_title('Intermmitent')

axs[0, 1].bar(x4, c1)
axs[0, 1].set_title('Chaos 1')
'''
axs[1].bar(x5, c2, width = largura_barras)
axs[1].set_title('Chaos 2')

'''
axs[2, 1].bar(x6, fc)
axs[2, 1].set_title('Full chaos')
'''

# Adicionar legenda em cada subplot
#axs[0, 0].legend([n + ' dados'])
#axs[0, 1].legend([n + ' dados'])
#axs[1, 0].legend([n + ' dados'])
#axs[2, 0].legend([n + ' dados'])
#axs[1, 1].legend([n + ' dados'])
#axs[2, 1].legend([n + ' dados'])

plt.suptitle('Histograma')
plt.tight_layout()

nome_arquivo = "/home/eude/Desktop/IC/caos/hist/hist_"+ n +".png"
plt.savefig(nome_arquivo)
# Mostrar o gráfico
plt.show()

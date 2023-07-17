import matplotlib.pyplot as plt
import numpy as np

def vetor(diretorio):
    data = np.loadtxt(diretorio, delimiter=',')
    x = data[:, 0]
    y = data[:, 1]
    return x, y

n = input('Qual o tamanho dos arquivos?\n')
n = str(n)

diretorio1 = '/home/pc/Desktop/IC/caos/hist/LM_p1/' + n + '.txt'
x1, p1 = vetor(diretorio1)

x2 = []
fbp = []
diretorio2 = '/home/pc/Desktop/IC/caos/hist/LM_fbp/' + n + '.txt'
x2, fbp = vetor(diretorio2)

x3 = []
intr = []
diretorio3 = '/home/pc/Desktop/IC/caos/hist/LM_int/' + n + '.txt'
x3, intr = vetor(diretorio3)

x4 = []
c1 = []
diretorio4 = '/home/pc/Desktop/IC/caos/hist/LM_c1/' + n + '.txt'
x4, c1 = vetor(diretorio4)

x5 = []
c2 = []
diretorio5 = '/home/pc/Desktop/IC/caos/hist/LM_c2/' + n + '.txt'
x5, c2 = vetor(diretorio5)

x6 = []
fc = []
diretorio6 = '/home/pc/Desktop/IC/caos/hist/LM_fc/' + n + '.txt'
x6, fc = vetor(diretorio6)

fig, axs = plt.subplots(3, 2)

axs[0, 0].plot(x1, p1)
axs[0, 0].set_title('-o')

axs[0, 1].plot(x2, fbp)
axs[0, 1].set_title('-*')

axs[1, 0].plot(x3, intr)
axs[1, 0].set_title('-x')

axs[2, 0].plot(x4, c1)
axs[2, 0].set_title('-d')

axs[1, 1].plot(x5, c2)
axs[1, 1].set_title('-v')

axs[2, 1].plot(x6, fc)
axs[2, 1].set_title('-s')

# Adicionar legenda em cada subplot
axs[0, 0].legend([n + ' dados'])
axs[0, 1].legend([n + ' dados'])
axs[1, 0].legend([n + ' dados'])
axs[2, 0].legend([n + ' dados'])
axs[1, 1].legend([n + ' dados'])
axs[2, 1].legend([n + ' dados'])

plt.suptitle('histograma')
plt.tight_layout()
plt.grid(True)

# Mostrar o gráfico
plt.show()


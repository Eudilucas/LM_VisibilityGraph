import networkx as nx
import numpy as np


'''
Abrir arquivos com as arestas e criar o grafo --> Devo criar um metodo que faz isso.
Contar os caminhos.
Adicionar em um vetor.
Contar o numero de Nós.
Criar um vetor com o numero de N.
'''



arq =open("/home/eude/Desktop/IC/caos/arestas/LM_p1/3.txt", 'rb') #Abrindo arquivo no modo leitura
G=nx.read_adjlist(arq)

arq.close()

print("Caminho medio")
print(nx.average_shortest_path_length(G))




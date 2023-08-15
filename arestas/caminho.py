import networkx as nx
import numpy as np
import os
'''
Abrir arquivos com as arestas e criar o grafo --> { 


1) Loop{
2) Passo o diretorio onde se encontram os arquivos.
3) Ler o arquivo1.txt e gravo o caminho medio dele em algum vetor.
4) Volta o ponteiro para o comeco do novo arquivo. 
5) plot do caminho medio em funcao do numero de nos do ultimo arquivo.
6) Fechar arquivo.}



}

Contar os caminhos.
Adicionar em um vetor.
Contar o numero de Nos.
Criar um vetor com o numero de N.
'''
n=str(input())

diretorio = "/home/eude/Desktop/IC/caos/arestas/LM_fbp/"+n+".txt"




arq=open(diretorio, 'rb') #Abrindo arquivo no modo leitura

G=nx.read_adjlist(arq)
print(n, nx.average_shortest_path_length(G))
arq.close()	




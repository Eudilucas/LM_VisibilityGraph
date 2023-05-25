import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv


def mostrar_matriz(A):
	
	for i in range(len(A)):
		for j in range(len(A[0])):
			print(A[i][j])
			

def diretorio(#int caso, int nome e a str string de volta):
	str matriz = ["/home/pc/Desktop/IC/caos/arestas"]
	str casos = ["/LM_p1","LM_int","LM_fbp","LM_c1","LM_c2","LM_fc"]
	str barra = "/"
	str tipo = ".txt"
	int i
	
	if (i == 3.5):
			string_de_volta = str(matriz+casos[0]+barra+nome+tipo)
			else if (i == 3.):
						string_de_volta = str(matriz+casos[1]+barra+nome+tipo)
			else if (i == 3.):
			string_de_volta = str(matriz+casos[2]+barra+nome+tipo)
			else if (i == 3.):
			string_de_volta = str(matriz+casos[3]+barra+nome+tipo)
			else if (i == 3.):
			string_de_volta = str(matriz+casos[4]+barra+nome+tipo)
			else if (i == 3.):
						string_de_volta = str(matriz+casos[5]+barra+nome+tipo)
			else if (i == 4.):


	str (nome)
	
	string_de_volta = str(matriz+casos+barra+nome+tipo)
	
	
valor1 = int(input(""))
valor2 = float(input(""))
valor3 = (input(""))
valor4 = (input(""))
arq =open("exemplo2.txt", 'r') #Abrindo arquivo no modo leitura

vec=arq.readlines() #Transformando cada linha em entradas da lista



for i in range(len(vec)):
	vec[i]=vec[i].split(",") #quebrando cada todas as linhas até onde tem virgula

arq.seek(0) #função para o ponteiro voltar para o começo do arquivo





for i in range(len(vec)):
	for j in range(2):
		vec[i][j]=float(vec[i][j])#convertendo os valores em float e adicionando ao array vec

G=nx.Graph(vec)




complexo_simplicial = []
complexo_simplicial = list(nx.find_cliques(G)) 



tam_q = nx.graph_clique_number(G) #tamanho do paremetro q.




q=[[]for i in range(tam_q)]





#print(complexo_simplicial)

#print(tam_simplex_max)


#Primeiro vetor da estrutura Q(q)

tam = len(nx.cliques_containing_node(G)) # Note que isso é o mesmo que o numero de nós.

print(nx.cliques_containing_node(G))


aux = [[]for i in range(tam)]

for i in range(tam):
	aux[i] = nx.cliques_containing_node(G)[i]
	print(aux[i])

#ideia

n_simplex = []

for i in range(len(aux)):
	n_simplex.append(len(aux[i]))
print(max(n_simplex))


'''
for i in range(tam_q):
	for j in range(2):
		aux[i] = nx.cliques_containing_node(G)[i]
		if (len(aux[i])==1):
		
		print(i ,len(aux[i]))
'''

#vetor f(q) --> PARA O QUARTO VETOR JÁ EXISTE UM MÉTODO PRONTO(o SEGUNDO VETOR É O QUARTO VETOR ACUMULADO)
'''
for i in range(complexo_simplicial):
	if x in complexo_simplicial 
		print(nx.number_of_cliques(G))
'''


#vetor max(dim)Qî

'''
contar a dimensão de cada nó

'''



arq.seek(0)
arq.close()

'''

Proximo passo é definir os 6 caracterizadores.
Mas antes precisamos definir a variável q. Para isso basta saber o tamanho da maior linha no complexo simplicial. OK

função count 



Agora devo contar o numero de arestas entre os cliques.
vetor Q(q)
vetor N_s(q)
vetor Q^(q)
vetor f(q)
vetor max(dim(Qî))(q)
vetor S(q)


'''

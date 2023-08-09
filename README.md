# LM_VisibilityGraph
IC
@dilucas

Quanto a utilização do programa.

O VisibilityGraphQM.c é a núcleo do programa, a partir dele são gerados os dados advindos da serie temporal e convertidos em arestas (relacionados ao grafo associado), histograma (do também grafo associado) e distribuição de grau (naturalmente, do grafo que a originou). Para uma necessaria visualisação é necessário usar os programas postos dentro da pasta (~/arestas/graficos, ~/distri_grau/graficos, ~/hist/graficos, ~/histograma/graficos). Nestes mesmos diretorios estarão nossos resultados.

O programa Visibility é feito em C e portanto necessita de ser compilado e rodado.
Quanto as medidas de complexidade

Algumas são feitas em python e já não necessitam ser compiladas pasta ir no diretorio através do terminal e rodar o programa desejado, assim:

$~./programa_python.py


Para rodar o Visibility entre no terminal e vá até o diretório do programa e use:

$ gcc VisibilityGraphQM.c -lm -o VisibilityGraphQM
$./VisibilityGraphQM <numero de dados> <distancia entre vizinhos> <caso> <condição inicial>


ou dê a permissão para o arquivo "executar.sh", faça modificações caso queira e rode ele no terminal assim,

~./executar.sh


OBS1: Todos os programas possuem metodos ou funções que só funcionam máquina em específico, pois esses tais métodos ou funções manipulam os diretórios, por este motivo você deve modificar ou construir uma nova forma de organizar os diretorios.

Feito isto seus arquivos estarão prontos nas pastas arestas, distri_grau, hist, series_temporais.

OBS2: A entrada 'caso' foi limitada para ter apenas 6 opções, se o usuario tentar usar uma entrada não cadastrada receberá o seguinte retorno:

$'Caso invalido'

Os casos validos são: 

LM_p1 = 3.5
LM_fbp = 3.56995
LM_int = 3.857
LM_c1 = 3.87
LM_c2 = 3.89
LM_fc = 4.00


A condição inicial não pode ser zero, caso seja não terá resultado algum.

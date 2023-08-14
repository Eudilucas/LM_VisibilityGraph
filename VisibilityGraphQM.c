//Autor: Adauto J. Ferreira de Souza
//Co-autor: Eude Lucas S. da Silva
//Universidade Federal Rural de Pernambuco - UFRPE
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>



int main( int argc, char** argv )
{
    FILE *ptr;
    int i, j, k, Ndata, Delta, visible, d;
    float t, x0, r;
    char endereco1[200]="", endereco2[200]="", endereco3[200]="", endereco4[200]="";
	void diretorio_arquivo(int i, float j, int k, char* endereco);
	int f_links = Ndata*(Ndata - 1);// N° maximo de arestas	    	
	
	sscanf (argv[1],"%d",&Ndata); 
	sscanf (argv[2],"%d",&Delta);
	sscanf (argv[3],"%f",&r);
	sscanf (argv[4],"%f",&x0);


    int *deg = (int *) calloc(Ndata,sizeof(int)); 
    float *data = (float *) calloc(Ndata,sizeof(float));
    data[0] = x0;

	diretorio_arquivo(0,r,Ndata, endereco1);
	diretorio_arquivo(1,r,Ndata, endereco2);
	diretorio_arquivo(2,r,Ndata, endereco3);
	diretorio_arquivo(3,r,Ndata, endereco4);
			
	
	

    for (i=1; i<Ndata; ++i) data[i] = r*data[i-1]*(1-data[i-1]);// logistic map
	

	ptr = fopen(endereco1,"w"); //endereco
	for (i=0;i<Ndata;++i)fprintf(ptr,"%f\n",data[i]);
	fclose(ptr);
	
	
    ptr = fopen(endereco2,"w"); //endereco
    for (i=0; i<Ndata; ++i) deg[i] = 0;
    for (d=1; d<=Delta; ++d) {
	for (i=0; i<Ndata-d; ++i) {
	    j = i+d;
	    visible = 1;
	    t = (data[i]-data[j])/ (float) d;
	    for (k=i+1; k<j; ++k)
		visible = visible && ( data[k] < (data[j] + t*(j-k)) );
	    if ( visible ) {
		++deg[i];
		++deg[j];
		fprintf(ptr,"%d %d\n",i,j);
	    }
	}
    }
    fclose(ptr);
    
/*   
    ptr = fopen(endereco3,"w");//endereco
    for (i=0; i<Ndata; ++i) fprintf(ptr,"%d, %d\n",i,deg[i]);// Aqui não é um histograma. Mas sim o grau de cada nó.
    fclose(ptr);

    ptr = fopen(endereco4,"w");//endereco	
    int *hist = (int *) calloc(100,sizeof(int));
    for (i=0; i<100; ++i) hist[i] = 0;
    for (i=0; i<Ndata; ++i) ++hist[deg[i]];
    

    double n = 0.0;


    for (i=0; i<100; ++i) n += hist[i];
    for (i=0; i<100; ++i){

	if ( hist[i] ){ fprintf(ptr,"%d, %f \n",i , hist[i]/n);
	printf("%d, %d \n",i , hist[i]);
}}

    fclose(ptr);


*/
    return 0;
}

void diretorio_arquivo(int i, float j, int k, char* endereco) {
	char diretorio[30] = "/home/eude/Desktop/IC/caos";
	char pasta[4][18] = { "/series_temporais", "/arestas", "/hist", "/distri_grau" };
	char caso[6][8] = { "/LM_p1","/LM_fbp","/LM_int","/LM_c1","/LM_c2","/LM_fc" };
	char nome[13] = "", copia[5] = "", barra[6]="/";

	strcat(endereco, diretorio);
	if (i == 0) {
		strcat(endereco, pasta[0]);
	} else if (i == 1) {
		strcat(endereco, pasta[1]);
	} else if (i == 2) {
		strcat(endereco, pasta[2]);
	} else if (i == 3) {
		strcat(endereco, pasta[3]);
	} else {
		printf("Valor inválido de i\n");
		return;
	}

	if (j == 3.5) {
		strcat(endereco, caso[0]);
	}
	else if ((j - 3.56995)<0.000001) {
		strcat(endereco, caso[1]);
	} 
	else if ((j - 3.857)<0.0001 ) {
		strcat(endereco, caso[2]);
	} 
	else if ((j - 3.87 )<0.001) {
		strcat(endereco, caso[3]);
	}
	else if ((j - 3.89)<0.001) {
		strcat(endereco, caso[4]);
	}
	else if (j == 4.00) {
		strcat(endereco, caso[5]);
	} 
	else {
		printf("Caso nao existente de r= %f\n", j);
		return;
	}

	sprintf(copia, "%i", k);
	strcat(barra, copia);
	strcat(nome, barra);
	strcat(nome, ".txt");
	strcat(endereco, nome);
}

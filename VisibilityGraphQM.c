// includes, system
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
#define __STDC_FORMAT_MACROS //pre-processamento
#include <inttypes.h>

static inline uint64_t rotl(const uint64_t x, int k) {
	return (x << k) | (x >> (64 - k));
}

uint64_t next(uint64_t *s) {
	const uint64_t result_starstar = rotl(s[1] * 5, 7) * 9;

	const uint64_t t = s[1] << 17;

	s[2] ^= s[0];
	s[3] ^= s[1];
	s[1] ^= s[2];
	s[0] ^= s[3];

	s[2] ^= t;

	s[3] = rotl(s[3], 45);

	return result_starstar;
}

uint64_t seed(uint64_t x) {
	uint64_t z = (x += 0x9e3779b97f4a7c15);
	z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9;
	z = (z ^ (z >> 27)) * 0x94d049bb133111eb;
	return z ^ (z >> 31);
}

double rnd(uint64_t x) {
	return (x >> 11) * (1. / (UINT64_C(1) << 53)); //retorna um double em [0,1)
}
//================================== ASSUMO MINHA IGNORANCIA DAQUI PRA CIMA ======================================
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


    srand( time(0) );
    uint64_t x, st[4]; //Isso me parece ser da aleatóriedade dos números
    for (j=0; j<4; ++j) {
	for (i=0; i<100; ++i) x = rand();
	st[j] = seed(x);
    }
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
		fprintf(ptr,"%d, %d\n",i,j);
	    }
	}
    }
    fclose(ptr);
    
    
    ptr = fopen(endereco3,"w");//endereco
    for (i=0; i<Ndata; ++i) fprintf(ptr,"%d, %d\n",i,deg[i]);
    fclose(ptr);

    int *hist = (int *) calloc(f_links,sizeof(int));
    for (i=0; i<f_links; ++i) hist[i] = 0;
    for (i=0; i<Ndata; ++i) ++hist[deg[i]];
    
    ptr = fopen(endereco4,"w");//endereco

    double n = 0.0;

    for (i=0; i<f_links; ++i) n += hist[i];
    for (i=0; i<f_links; ++i)
	if ( hist[i] ) fprintf(ptr,"%d, %f \n",i , hist[i]/n);
    fclose(ptr);



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

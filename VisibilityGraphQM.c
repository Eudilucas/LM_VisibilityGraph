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
    char endereco[100];
	char diretorio_arquivo(int i, int j, int k);
	    	
	
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

    for (i=1; i<Ndata; ++i) data[i] = r*data[i-1]*(1-data[i-1]);// logistic map

	diretorio_arquivo(0,0,Ndata)
	ptr = fopen(endereco,"w"); //endereco



	

	for (i=0;i<Ndata;++i)fprintf(ptr,"%f\n",data[i]);

    ptr = fopen(endereco,"w"); //endereco
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
    
	

    ptr = fopen(endereco,"w");//endereco
    for (i=0; i<Ndata; ++i) fprintf(ptr,"%d, %d\n",i,deg[i]);
    fclose(ptr);
    int *hist = (int *) calloc(100,sizeof(int));
    for (i=0; i<100; ++i) hist[i] = 0;
    for (i=0; i<Ndata; ++i) ++hist[deg[i]];
    
    
	

    ptr = fopen(endereco,"w");//endereco
    double n = 0.0;
    for (i=0; i<100; ++i) n += hist[i];
    for (i=0; i<100; ++i)
	if ( hist[i] ) fprintf(ptr,"%d, %f \n",i , hist[i]/n);
    fclose(ptr);



    return 0;
}

char diretorio_arquivo(int i, int j, int k){
	
	
	char diretorio[30] = {"/home/pc/Desktop/IC/caos"};
	char pasta[5][18]={"/series_temporais", "/arestas", "/hist", "/distribuicao"};
	char caso[6][8] = {"/LM_p1","/LM_fbp","/LM_int","/LM_c1","/LM_c2","/LM_fc"};
	char nome[6], copia[5];
		
	
	
	
	
	strcat(endereco, diretorio);
	if (i == 0){
	strcat(endereco, pasta[0])};
	if (i == 1){
	strcat(endereco, pasta[1])};
	if (i == 2){
	strcat(endereco, pasta[2])};
	if (i == 3){
	strcat(endereco, pasta[3])};
	
	if(j == 0){
	strcat(endereco, caso[0])};
	if(j == 1){
	strcat(endereco, caso[1])};
	if(j == 2){
	strcat(endereco, caso[2])};
	if(j == 3){
	strcat(endereco, caso[3])};
	if(j == 4){
	strcat(endereco, caso[4])};
	if(j == 5){
	strcat(endereco, caso[5])};
	
	
	sprintf(copia,"%i",k);
	strcat(nome, copia);
	strcat(endereco, nome);






return endereco;
}


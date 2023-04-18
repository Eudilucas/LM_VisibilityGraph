// includes, system
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
#define __STDC_FORMAT_MACROS
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
//============================================= ASSUMO MINHA IGNORANCIA DAQUI PRA CIMA =================================
int main( int argc, char** argv )
{
    FILE *ptr;
    int i, j, k, Ndata, Delta, visible, d;
    float t, x0, r;
    
    i = sscanf (argv[1],"%d",&Ndata); 
    i = sscanf (argv[2],"%d",&Delta);
    i = sscanf (argv[3],"%f",&r);
    i = sscanf (argv[4],"%f",&x0); //Como i recebe 4 entradas?

    srand( time(0) );
    uint64_t x, st[4]; // Isso me parece ser da aleatóriedade dos números
    for (j=0; j<4; ++j) {
	for (i=0; i<100; ++i) x = rand();
	st[j] = seed(x);
    }
    int *deg = (int *) calloc(Ndata,sizeof(int)); 
    float *data = (float *) calloc(Ndata,sizeof(float));
    data[0] = x0;
    for (i=1; i<Ndata; ++i) data[i] = r*data[i-1]*(1-data[i-1]);// logistic map
	ptr = fopen("/home/eude/Desktop/IC/caos/series_temporais/periodico.txt","w");
	for (i=0;i<Ndata;++i)fprintf(ptr,"%f\n",data[i]);

    ptr = fopen("/home/eude/Desktop/IC/caos/arestas/LM_periodico_2000.txt","w");
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
    ptr = fopen("/home/eude/Desktop/IC/caos/hist/hist.dat","w");
    for (i=0; i<Ndata; ++i) fprintf(ptr,"%d, %d\n",i,deg[i]);
    fclose(ptr);
    int *hist = (int *) calloc(100,sizeof(int));
    for (i=0; i<100; ++i) hist[i] = 0;
    for (i=0; i<Ndata; ++i) ++hist[deg[i]];
    ptr = fopen("/home/eude/Desktop/IC/caos/distribuicao/deg_dist.dat","w");
    double n = 0.0;
    for (i=0; i<100; ++i) n += hist[i];
    for (i=0; i<100; ++i)
	if ( hist[i] ) fprintf(ptr,"%d, %f\n",i, hist[i]/n);
    fclose(ptr);

    return 0;
}


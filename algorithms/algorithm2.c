#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char *argv[]) {     
    int n;
    sscanf (argv[1],"%d",&n);
    double pi = 0;
    int sign = 1;
    int i;
    for(i=0; i<=n; i++){
        pi = pi + (double)((double)pow(-1,i)/(double)pow(2,10*i)) * (double)((double)(-1*pow(2,5)/(double)((4*i)+1)) + (double)(-1/(double)((4*i)+3)) + (double)(pow(2,8)/(double)((10*i)+1)) + (double)(-1*pow(2,6)/(double)((10*i)+3)) + (double)(-1*pow(2,2)/(double)((10*i)+5))  + (double)(-1*pow(2,2)/(double)((10*i)+7)) + (double)(1/(double)((10*i)+9)) );                       
    }
    pi = (double)pi/pow(2,6);
    printf("%.30f",pi);
    return 0;
}
    
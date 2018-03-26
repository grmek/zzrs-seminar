#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char *argv[]) {     
    int n;
    sscanf (argv[1],"%d",&n);
    double pi = 0;
    int sign = 1;
    int i;
    for(i = 1; i<=n; i=i+2){
        pi = pi + (double)sign*1/i;
        sign = sign * -1;
    }
    pi = pi*4;
    printf("%.30f",pi);
    return 0;
}
    

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main() //main function begins
{

double k_1,k_2 ,F;	
double **p;
F=-51;
p=loadtxt("V.dat",2,2);
  //k_1 and k_2 are eigen values obtained from the characteristic equation
k_1 =(p[0][0]+p[1][1]+(p[0][0]-p[1][1]))/(2*-F);
k_2 =(p[0][0]+p[1][1]-(p[0][0]-p[1][1]))/(2*-F);
printf("%f\n",k_1);
printf("%f\n",k_2);
}





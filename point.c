#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int  main() //main function begins
{
double a,b,cos,sin,m_1;
double p,q,sec,p_1,p_2,m_2;
a=sqrtf(34.0);
b=sqrtf(34.0)/3;
p=sqrtf(17);
q=sqrtf(17)/3;
sec=a/p;
cos=1/sec;
sin=sqrtf(1-(cos*cos));
printf("%f\n",sin);
p_1=p*cos;
p_2=q*sin;
printf("%f\n",p_1);
printf("%f\n",p_2);
m_1=a;
m_2=-b;
printf("%f\n",m_1);
printf("%f\n",m_2);
}



import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math



len=100
O=np.array([0,0])

theta = np.loadtxt('theta.dat',dtype='double')
k=np.loadtxt('pres2.dat',dtype='double')
y = np.zeros((2,len))
a=1/(k[0]**0.5)
b=1/(k[1]**0.5)
y[0,:] = a*np.cos(theta)

y[1,:] = b*np.sin(theta)
P1=np.loadtxt('p1.dat',dtype='double')
m1=np.loadtxt('m1.dat',dtype='double')
len =50

x_P1 = np.zeros((2,len))
lam_1 = np.linspace(-1,1,len)

for i in range(len):

    temp1 = P1 + lam_1[i]*m1

    x_P1[:,i]= temp1.T
plt.plot(x_P1[0,:],x_P1[1,:],label='Required Tangent 1')   
plt.plot(P1[0], P1[1], 'o')

plt.text(P1[0] * (1 - 0.1), P1[1] * (1 + 0.1) , 'P1')
 
P2=np.loadtxt('p2.dat',dtype='double')
m2=np.loadtxt('m2.dat',dtype='double')
len =50

x_P2 = np.zeros((2,len))
lam_2 = np.linspace(-1,1,len)

for i in range(len):

    temp2 = P2 + lam_2[i]*m2

    x_P2[:,i]= temp2.T
plt.plot(x_P2[0,:],x_P2[1,:],label='Required Tangent 2') 
plt.plot(P2[0], P2[1], 'o')

plt.text(P2[0] * (1 - 0.1), P2[1] * (1 + 0.1) , 'P2')

P3=np.loadtxt('p3.dat',dtype='double')
m3=np.loadtxt('m1.dat',dtype='double')
len =50

x_P3 = np.zeros((2,len))
lam_3= np.linspace(-1,1,len)

for i in range(len):

    temp3 = P3 + lam_1[i]*m3

    x_P3[:,i]= temp3.T
plt.plot(x_P3[0,:],x_P3[1,:],label='Required Tangent 3') 
plt.plot(P3[0], P3[1], 'o')

plt.text(P3[0] * (1 - 0.1), P3[1] * (1 + 0.1) , 'P3')

P4=np.loadtxt('p4.dat',dtype='double')
m4=np.loadtxt('m2.dat',dtype='double')
len =50

x_P4= np.zeros((2,len))
lam_4= np.linspace(-1,1,len)

for i in range(len):

    temp4 = P4 + lam_4[i]*m4

    x_P4[:,i]= temp4.T
plt.plot(x_P4[0,:],x_P4[1,:],label='Required Tangent 4') 
plt.plot(P4[0], P4[1], 'o')

plt.text(P4[0] * (1 - 0.1), P4[1] * (1 + 0.1) , 'P4')

plt.plot(y[0,:],y[1,:],label='Ellipse at origin')
plt.plot(O[0], O[1], 'o')

plt.text(O[0] * (1 - 0.1), O[1] * (1 + 0.1) , 'O')


plt.axis('equal')

plt.xlabel('$x$');plt.ylabel('$y$')

plt.legend(loc='best')

plt.grid()
plt.show()

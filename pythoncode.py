import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math


len=100
theta=np.linspace(0,2*np.pi,len)
V=np.array(([3,0],[0,27]))
u=np.array([0,0])
F=-51
O=np.array([0,0])
l,m=LA.eig(V/-F)
y = np.zeros((2,len))
a=1/l[0]**0.5
b=1/l[1]**0.5
print(a)
print(b)

y[0,:] = a*np.cos(theta)

y[1,:] = b*np.sin(theta)
P=np.array([(17/2)**0.5,(17/18)**0.5])
m=np.array([34.0**0.5,-(34.0**0.5)/3])
len =10
x_P = np.zeros((2,len))
lam_1 = np.linspace(0,1,len)

for i in range(len):

    temp1 = P + lam_1[i]*m

    x_P[:,i]= temp1.T
plt.plot(y[0,:],y[1,:],label='Ellipse at origin')
plt.plot(x_P[0,:],x_P[1,:],label='Required Tangent')
plt.plot(O[0], O[1], 'o')

plt.text(O[0] * (1 - 0.1), O[1] * (1 + 0.1) , 'O')
plt.plot(P[0], P[1], 'o')

plt.text(P[0] * (1 - 0.1), P[1] * (1 + 0.1) , 'P')

plt.axis('equal')

plt.xlabel('$x$');plt.ylabel('$y$')

plt.legend(loc='best')

plt.grid()
plt.show()

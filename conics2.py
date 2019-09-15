import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111,aspect='equal')
len=100
theta=np.linspace(0,2*np.pi,len)

V=np.array([1/9,0],[0,1/25])
u=np.array([0,0])
F=-1
P=np.array([3/2,5*(3**0.5)/2])
Y=P@V
F_1=np.array([0,4])
F_2=nparray([0,-4])



from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt 
from matplotlib import cm
import numpy as np 

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
r=np.linspace(0.3,1.12,70)
p=np.linspace(0,2*3.14,70)
R,P=np.meshgrid(r,p)
F,Y=R*np.cos(P),R*np.sin(P)
G=(R**2-1)**2
ax.plot_surface(F,Y,G)
plt.show()
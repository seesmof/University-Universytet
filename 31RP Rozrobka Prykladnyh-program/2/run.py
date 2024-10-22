import numpy as np 
import scipy as sp 
from matplotlib import pyplot as plt

def one():
    ''' 
    Обчислити визначений інтеграл
    '''
    PI=np.pi
    bounds={
        'lower':PI/4,
        'upper':PI/7
    }
    target_function=lambda x:(np.cos(2*x)+np.sin(x)**2)/np.sin(3*x)
    solution=sp.integrate.quad(target_function,bounds['lower'],bounds['upper'])
    print(solution)
def two():
    ''' 
    Побудувати графік функції
    Знайти її мінімум методом Нелдера-Міда: точність 10
    '''
    target_function=lambda x,y:x**2+y**2-4*x-y-x*y
    b=np.arange(-3,3,0.1)
    d=np.arange(-3,3,0.1)
    nu=np.zeros((b.size,d.size))
    counter_y=0
    for deta in d:
        counter_x=0
        for beta in b:
            nu[counter_x,counter_y]=np.sqrt(1+(2*deta*beta)**2)/np.sqrt((1-beta**2)**2)+(2*deta*beta)**2
            counter_x+=1
        counter_y+=1
    B,D=np.meshgrid(d,b)
    fig=plt.figure()
    ax=fig.add_subplot(333,projection='3d')
    ax.plot_surface(B,D,nu)
one()
two()
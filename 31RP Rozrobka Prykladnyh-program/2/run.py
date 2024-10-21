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
    x=np.array([1,2,6,8])
    y=np.array([3,8,1,10])
    plt.plot(x,y,'o-g')
    plt.xlabel('Вертикаль')
    plt.ylabel('Горизонталь')
    plt.title('Графік функції')
    plt.show()
one()
two()
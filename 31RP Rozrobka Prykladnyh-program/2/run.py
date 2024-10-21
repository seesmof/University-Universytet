import numpy as np 
import scipy as sp 
from matplotlib import pyplot as plt

def one():
    """ 
    Обчислити визначений інтеграл
    """
    PI=np.pi
    bounds={
        "lower":PI/4,
        "upper":PI/7
    }
    print(bounds)
def two():
    """ 
    Побудувати графік функції
    Знайти її мінімум методом Нелдера-Міда: точність 10
    """
one()
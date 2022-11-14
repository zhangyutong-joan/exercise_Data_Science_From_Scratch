import math
from collections import Counter
import central_tendencies as ct # 导入上一个模块。有些方法要在这里用
from C4 import Vectors as vec # 导入C4里面的Vectors.py。有些方法要在这里用

def data_range(x):
    return max(x)-min(x)

def de_mean(x):
    '''x-mean(x)'''
    x_bar=ct.mean(x)
    return [x_i-x_bar for x_i in x]

def variance(x):
    '''方差'''
    n=len(x)
    deviations=de_mean(x)
    return vec.sum_of_squares(deviations)/(n-1)

def standard_deviation(x):
    '''标准差'''
    return math.sqrt(variance(x))

def interquartile_range(x):
    '''计算75百分位值和25百分位值之间的差'''
    return ct.quantile(x,0.75)-ct.quantile(x,0.25)

if __name__ == '__main__':
    x=[3,2,6,48,31]
    print(data_range(x))
    print(variance(x))
    print(standard_deviation(x))
    print(interquartile_range(x))

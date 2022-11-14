import dispersion as dp

def covariance(x,y):
    '''协方差：协方差测量了两个变量如何从它们的平均值中串联起来变化'''
    n=len(x)
    return dp.vec.dot(dp.de_mean(x),dp.de_mean(y))/(n-1)

def correlation(x,y):
    '''相关系数，范围[-1,1]，绝对值越大相关性越大（0.25表示弱的正相关），1表示完全正相关，-1表示完全反相关'''
    stdev_x=dp.standard_deviation(x)
    stdev_y = dp.standard_deviation(y)
    if stdev_x>0 and stdev_y>0:
        return covariance(x,y)/stdev_x/stdev_y
    else:
        return 0

if __name__ == '__main__':
    x=[24,32,1,64,88,3]
    y=[10,15,0,50,70,2]
    "注意在进行相关性分析前需删除异常值"

    print(covariance(x,y))

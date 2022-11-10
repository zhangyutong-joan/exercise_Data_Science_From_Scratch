from matplotlib import pyplot as plt


if __name__ == '__main__':
    variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    total_error=[x + y for x, y in zip(variance, bias_squared)]
    xs=[i for i,_ in enumerate(variance)]
    # plt.plot() 画多个用plot
    plt.plot(xs,variance,'g-',label='variance') #绿的实线
    plt.plot(xs, bias_squared, 'r-.', label='bias^2') #红的虚线+点
    plt.plot(xs, total_error, 'b:', label='bias^2') #蓝的点
    # 加图例
    plt.legend(loc=9) # loc=9 means "top center"
    plt.xlabel("model complexity")
    plt.title("The Bias-Variance Tradeoff")
    plt.show()
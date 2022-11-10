from matplotlib import pyplot as plt
from collections import Counter

if __name__ == '__main__':
    #创建条形图
    # 比较一些电影获得奥斯卡奖的数量
    # movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    # num_oscars = [5, 11, 3, 8, 10]
    # xs=[i+0.1 for i,_ in enumerate(movies)] #设置条形位置，这里往左偏移0.1
    # plt.bar(xs,num_oscars) #条形位置为[xs],高为num_oscars，（条形宽度默认为0.8）
    # plt.ylabel("# of Academy Awards")
    # plt.title("My favorite Movies")
    # plt.xticks([i+0.5 for i,_ in enumerate(movies)],movies) #改x轴
    # plt.show()
    # 绘制直方图，观察分布
    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
    decile=lambda grade:grade//10*10
    histogram=Counter(decile(grade) for grade in grades) # 计算各分数段的人数
    plt.bar([x for x in histogram.keys()], # 将每个条位置
            histogram.values(), #每个条高度
            8) #每个条宽度为8,因为下面设置x刻度为10（plt.xticks()）
    plt.axis([-5,105,0,5]) # 设置x轴范围[-5,105],y轴范围[0,5]
    plt.xticks([10*i for i in range(11)]) # 设置x刻度 0,10,...,100
    plt.xlabel("Decile")
    plt.ylabel("# of Students")
    plt.title("Distribution od Exam 1 Grades")
    plt.show()
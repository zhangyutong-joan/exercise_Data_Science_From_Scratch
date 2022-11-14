import math
# 向量运算
def vector_add(v,w):
    """向量加法"""
    return [v_i+w_i for v_i,w_i in zip(v,w)]

def vector_subtract(v,w):
    """向量减法"""
    return [v_i-w_i for v_i,w_i in zip(v,w)]

def vector_sum(vectors):
    """向量求和"""
    result=vectors[0]
    for vector in vectors[1:]:
        result=vector_add(result,vector)
    return result
    # 或者：
    # return reudce(vector_add,vectors)
    # 或者可以这样定义(我理解不了...)：
    # vector_sum=partial(reduce,vector_add)

def scalar_multiply(c,v):
    """向量v乘一个常数c"""
    return [c*v_i for v_i in v]

def scalar_mean(vectors):
    """计算向量的平均值"""
    n=len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))

def dot(v,w):
    """向量点乘"""
    return sum(v_i*v_i for v_i,w_i in zip(v,w))

def sum_of_squares(v):
    """向量平方和（v_1 * v_1 + ... + v_n * v_n）"""
    return dot(v,v)

def magnitude(v):
    """计算向量的模"""
    return math.sqrt(sum_of_squares(v))

def squared_distance(v,w):
    """计算向量v,w之间的距离平方和"""
    return sum_of_squares(vector_subtract(v, w))

def distance(v,w):
    return math.sqrt(squared_distance(v,w))


# if __name__ == '__main__':
#     v=[70,170,40]
#     w=[95,80,75,62]
#     print(dot(v, w))
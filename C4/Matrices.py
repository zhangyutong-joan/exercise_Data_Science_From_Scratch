# 矩阵运算

def shape(A):
    """返回将矩阵A的大小（行、列）"""
    num_rows=len(A)
    num_cols=len(A[0]) if A else 0
    return num_rows,num_cols

def get_row(A,i):
    return A[i]
def get_column(A,j):
    return [A_i[j] for A_i in A]

def make_matrix(num_rows,num_cols,entry_fn):
    """创建一个矩阵,值为entry_fn()"""
    return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]

def is_diagonal(i,j):
    """单位矩阵，主对角线元素为1（可作为entry_fn()）"""
    return 1 if i==j else 0

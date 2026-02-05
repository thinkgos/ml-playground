import numpy as np

# axis参数的使用
# 对于多维数组, 几乎所有的聚合函数都可以接受一个 axis 参数. 这个参数允许你沿着指定的轴(维度)进行计算, 而不是对整个数组进行计算.
# axis=None:(默认)对所有元素进行计算, 返回一个标量.
# axis=0: 沿着第一个轴(垂直方向, 跨行)进行计算.结果的形状会"压缩"掉这个轴.
# axis=1: 沿着第二个轴(水平方向, 跨列)进行计算.
# 理解 axis 的窍门: 想象一下, axis=0 就是把数组"压扁"成一行, axis=1 就是把数组"压扁"成一列.


# 创建一个 3x4 的二维数组
matrix = np.arange(12).reshape(3, 4)
print(f"原始矩阵: \n{matrix}\n")
# 原始矩阵:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# 1. 对整个矩阵求和(axis=None, 默认)
total_sum = matrix.sum()
print(f"整个矩阵的和: {total_sum}\n")
# 整个矩阵的和: 66


# 2. 沿 axis=0(垂直) 求和, 即计算每一列的和
sum_by_col = matrix.sum(axis=0)
print(f"每列的和(axis=0): {sum_by_col}")
# 每列的和(axis=0): [12 15 18 21] (0+4+8, 1+5+9, ...)
# 结果是一个一维数组, 其长度等于原始矩阵的列数


# 3. 沿 axis=1(水平) 求和, 即计算每一行的和
sum_by_row = matrix.sum(axis=1)
print(f"每行的和(axis=1): {sum_by_row}\n")
# 每行的和(axis=1): [ 6 22 38] (0+1+2+3, 4+5+6+7, ...)
# 结果是一个一维数组, 其长度等于原始矩阵的行数


# 4. axis 参数同样适用于 mean, max 等函数
mean_by_col = matrix.mean(axis=0)
print(f"每列的平均值(axis=0): {mean_by_col}")
# 每列的平均值(axis=0): [4. 5. 6. 7.]

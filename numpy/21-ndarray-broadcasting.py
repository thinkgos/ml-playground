import numpy as np

# 广播机制
# 要使广播能够成功，必须满足以下两个条件之一：
# 维度相等: 两个数组的维度大小相等。
# 其中一个为 1: 两个数组中，有一个的维度大小为 1

# 标量与数组的运算
arr = np.arange(5)
print(f"arr: {arr}")
result = arr + 10  # 标量 10 被广播到 arr 的形状 (5,)
print(f"arr + 10: {result}")
# arr: [0 1 2 3 4]
# arr + 10: [10 11 12 13 14]


# 一维数组与二维数组的运算
matrix = np.arange(12).reshape(3, 4)
# matrix.shape: (3, 4)
row_vector = np.array([10, 20, 30, 40])
# row_vector.shape: (4,)
print(f"Matrix (3x4): \n{matrix}\n")
print(f"Row Vector (4,): {row_vector}\n")
# 将行向量加到矩阵的每一行
result = matrix + row_vector
# 广播过程:
# 1. matrix.shape: (3, 4)
# 2. row_vector.shape: (4,)
# 3. 比较末尾维度: 4 vs 4 (相等, OK)
# 4. 比较前一维度: 3 vs (不存在, 假设为1) (其中一个为1, OK)
# 5. row_vector 被广播成 [[10, 20, 30, 40], [10, 20, 30, 40], [10, 20, 30, 40]]
print(f"Matrix + Row Vector: \n{result}")
# Matrix + Row Vector:
# [[10 21 32 43]
#  [14 25 36 47]
#  [18 29 40 51]]


# 需要手动调整维度以启用广播
matrix = np.arange(12).reshape(3, 4)
# matrix.shape: (3, 4)
col_vector = np.array([100, 200, 300])
# col_vector.shape: (3,)
# 如果直接相加: matrix + col_vector，会失败！
# 1. matrix.shape: (3, 4)
# 2. col_vector.shape: (3,)
# 3. 比较末尾维度: 4 vs 3 (不相等，且没有一个是1)，Error!
# 我们需要将 col_vector 的形状从 (3,) 变为 (3, 1)
col_vector_reshaped = col_vector.reshape(3, 1)
print(f"Column Vector (3,): {col_vector}")
print(f"Reshaped Column Vector (3,1): \n{col_vector_reshaped}\n")
# 现在再相加
result_col = matrix + col_vector_reshaped
# 广播过程:
# 1. matrix.shape: (3, 4)
# 2. col_vector_reshaped.shape: (3, 1)
# 3. 比较末尾维度: 4 vs 1 (其中一个为1, OK) -> col_vector_reshaped 广播到 (3, 4)
# 4. 比较前一维度: 3 vs 3 (相等, OK)
print(f"Matrix + Reshaped Column Vector: \n{result_col}")
# Matrix + Reshaped Column Vector:
# [[100 101 102 103]
#  [204 205 206 207]
#  [308 309 310 311]]
# 小技巧: 使用 np.newaxis 也可以达到同样的效果
# col_vector[:, np.newaxis] 的形状就是 (3, 1)

import numpy as np

# 创建标准形态数组：zeros, ones, eye, full

# `np.zeros(shape, dtype=float)`: 创建一个指定形状 shape 且所有元素都为 0 的数组.
# `np.ones(shape, dtype=float)`: 创建一个指定形状 shape 且所有元素都为 1 的数组.
# `np.full(shape, fill_value, dtype=None)`: 创建一个指定形状 shape 且所有元素都为 fill_value 的数组.
# `np.eye(N, M=None)`: 创建一个 N×M 的单位矩阵（主对角线为 1, 其余为 0）.如果 M 为 None, 则默认为 N×N.


# 1. 创建一个 2 行 3 列的全零矩阵
arr_zeros = np.zeros((2, 3))
print(f"2x3 全零矩阵: \n{arr_zeros}")
# 2x3 全零矩阵:
# [[0. 0. 0.]
#  [0. 0. 0.]]

# 2. 创建一个长度为 5 的全一向量 (一维数组)
arr_ones = np.ones(5)
print(f"长度为 5 的全一向量: \n{arr_ones}")
# 长度为 5 的全一向量:
# [1. 1. 1. 1. 1.]

# 3. 创建一个 3x3, 所有元素都为 7 的矩阵
arr_full = np.full((3, 3), 7)
print(f"3x3 全 7 矩阵: \n{arr_full}")
# 3x3 全 7 矩阵:
# [[7 7 7]
#  [7 7 7]
#  [7 7 7]]

# 4. 创建一个 4x4 的单位矩阵
arr_eye = np.eye(4)
print(f"4x4 单位矩阵: \n{arr_eye}")
# 4x4 单位矩阵:
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

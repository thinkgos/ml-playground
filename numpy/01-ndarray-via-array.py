import numpy as np

# 从`Python`序列创建
# `np.array(object, dtype=None)`: 将`Python`的列表(`list`)或元组(`tuple`)直接转换为`NumPy`数组.

# 1. 从 Python 列表创建一维数组
list_1d = [1, 2, 3, 4, 5]
arr_1d = np.array(list_1d)
print(f"一维数组: \n{arr_1d}")
# 一维数组:
# [1 2 3 4 5]

# 2. 从嵌套列表创建二维数组 (矩阵)
list_2d = [[1, 2, 3], [4, 5, 6]]
arr_2d = np.array(list_2d)
print(f"二维数组: \n{arr_2d}")
# 二维数组:
# [[1 2 3]
#  [4 5 6]]

# 3. 创建时指定数据类型为浮点数
arr_float = np.array([1, 2, 3], dtype=np.float64)
print(f"指定数据类型的数组: \n{arr_float}")
# 指定数据类型的数组:
# [1. 2. 3.]

import numpy as np

# 对数组的维度进行重新排列
# ndarray.T: 一个特殊的属性, 用于获取数组的转置.对于二维数组, 它就是行和列的互换
# ndarray.transpose(*axes): 一个更通用的方法, 可以指定维度的任意排列顺序.

# 创建一个 2x3 矩阵
mat = np.array([[1, 2, 3], [4, 5, 6]])
print(f"原始矩阵 (2x3): \n{mat}\n")
# 1. 使用 .T 进行转置
mat_t = mat.T
print(f"转置后的矩阵 (3x2): \n{mat_t}\n")
# 转置后的矩阵 (3x2):
# [[1 4]
#  [2 5]
#  [3 6]]
# 2. 对于三维数组使用 transpose
arr_3d = np.arange(24).reshape((2, 3, 4))
print(f"原始三维数组 shape: {arr_3d.shape}")
# 原始三维数组 shape: (2, 3, 4)
# 将轴 0, 1, 2 重新排列为 1, 2, 0
arr_transposed = arr_3d.transpose((1, 2, 0))
print(f"transpose((1, 2, 0)) 后的 shape: {arr_transposed.shape}")
# transpose((1, 2, 0)) 后的 shape: (3, 4, 2)

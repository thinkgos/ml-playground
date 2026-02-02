import numpy as np

# 数组的核心属性：shape, dtype, ndim, size
# 这些属性是 `ndarray` 对象自带的元数据, 无需计算即可快速访问, 帮助我们理解数组的“骨架”.

# `ndarray.ndim`: 数组的维度数量(轴的个数).
# `ndarray.shape`: 一个元组, 表示数组在每个维度上的大小.
# `ndarray.size`: 数组中元素的总数量, 等于 shape 中各元素之积.
# `ndarray.dtype`: 描述数组中元素类型的对象.

# 创建一个 2 行 3 列 4 深度的三维数组
arr_3d = np.arange(24).reshape((2, 3, 4))
print(f"示例三维数组: \n{arr_3d}\n")
# 探查其核心属性
print(f"维度数量 (ndim): {arr_3d.ndim}")
# 维度数量 (ndim): 3
print(f"形状 (shape): {arr_3d.shape}")
# 形状 (shape): (2, 3, 4)
print(f"元素总数 (size): {arr_3d.size}")
# 元素总数 (size): 24
print(f"数据类型 (dtype): {arr_3d.dtype}")
# 数据类型 (dtype): int64 (具体位数可能因系统而异)

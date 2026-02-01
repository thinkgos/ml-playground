import numpy as np

# 依据规则创建：arange, linspace

# `np.arange([start, ]stop, [step, ], dtype=None)`: 创建一个等差序列, 类似于 Python 的 range() 函数, 但返回的是 NumPy 数组, 并且支持浮点数步长.
# `np.linspace(start, stop, num=50, endpoint=True)`: 在指定的区间内, 创建一个包含指定数量元素的等间隔序列.这在科学绘图或数据采样时非常有用.

# 1. 使用 arange 创建 0 到 9 的整数数组
arr_range = np.arange(10)
print(f"arange(10): {arr_range}")
# arange(10): [0 1 2 3 4 5 6 7 8 9]

# 2. 使用 arange 创建从 2 到 10, 步长为 2 的数组
arr_step = np.arange(2, 11, 2)
print(f"arange(2, 11, 2): {arr_step}")
# arange(2, 11, 2): [ 2  4  6  8 10]

# 3. 使用 linspace 在 0 和 1 之间创建 5 个等间隔的点
arr_linspace = np.linspace(0, 1, 5)
print(f"linspace(0, 1, 5): {arr_linspace}")
# linspace(0, 1, 5): [0.   0.25 0.5  0.75 1.  ]

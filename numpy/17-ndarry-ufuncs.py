import numpy as np

# 元素级运算之通用函数

# 创建两个数组
x = np.array([1, 2, 3, 4])
y = np.array([4, 3, 2, 1])
print(f"x = {x}")
print(f"y = {y}\n")

# 1. 二元 UFuncs (元素级算术和比较)
print(f"x + y -> {x + y}")  # 加法
print(f"x * y -> {x * y}")  # 乘法
print(f"x ** 2 -> {x**2}")  # 平方
print(f"x > 2 -> {x > 2}\n")  # 比较, 返回布尔数组
# x + y -> [5 5 5 5]
# x * y -> [4 6 6 4]
# x ** 2 -> [ 1  4  9 16]
# x > 2 -> [False False  True  True]
# 使用 np.maximum 找出 x 和 y 中对应位置的较大值
z = np.array([3, 1, 4, 2])
print(f"z = {z}")
print(f"np.maximum(x, z) -> {np.maximum(x, z)}\n")
# z = [3 1 4 2]
# np.maximum(x, z) -> [3 2 4 4]

# 2. 一元 UFuncs
arr = np.array([0, np.pi / 2, np.pi])
print(f"arr = {arr}")
print(f"np.sin(arr) -> {np.sin(arr)}\n")  # 对每个元素求正弦
# arr = [0.         1.57079633 3.14159265]
# np.sin(arr) -> [0.0000000e+00 1.0000000e+00 1.2246468e-16] (注意浮点数精度)
data = np.arange(-5, 6)
print(f"data = {data}")
print(f"np.abs(data) -> {np.abs(data)}\n")  # 对每个元素求绝对值
# data = [-5 -4 -3 -2 -1  0  1  2  3  4  5]
# np.abs(data) -> [5 4 3 2 1 0 1 2 3 4 5]
# 开平方根
values = np.array([1, 4, 9, 16])
print(f"np.sqrt(values) -> {np.sqrt(values)}\n")
# np.sqrt(values) -> [1. 2. 3. 4.]
# 创建一个包含正负浮点数的数组
data = np.array([3.7, -3.7, 2.5, -2.5, 3.14])
print(f"原始数据: {data}\n")
# 四舍五入到整数
# 注意：对于 x.5 的情况, NumPy 采用“银行家舍入法”, 即向最近的偶数舍入
print(f"np.round() -> {np.round(data)}")
# np.round() -> [ 4. -4.  2. -2.  3.]
# 向下取整 (floor)
print(f"np.floor() -> {np.floor(data)}")
# np.floor() -> [ 3. -4.  2. -3.  3.]
# 向上取整 (ceil)
print(f"np.ceil() -> {np.ceil(data)}")
# np.ceil() -> [ 4. -3.  3. -2.  4.]
# 截断取整 (trunc)
print(f"np.trunc() -> {np.trunc(data)}")
# np.trunc() -> [ 3. -3.  2. -2.  3.]

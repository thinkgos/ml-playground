import numpy as np

# 条件逻辑
# np.where(condition, x, y) 是一个三元的 UFunc, 它根据 condition (一个布尔数组) 来选择输出.
# 如果 condition 中某个位置为 True, 则输出该位置上 x 的值;如果为 False, 则输出该位置上 y 的值.

arr_a = np.array([1, 2, 3, 4, 5])
arr_b = np.array([10, 20, 30, 40, 50])
condition = np.array([True, False, True, False, True])

# 1. 基本用法
# 如果条件为 True, 取 arr_a 的值, 否则取 arr_b 的值
result = np.where(condition, arr_a, arr_b)
print(f"np.where(condition, arr_a, arr_b) -> {result}\n")
# np.where(condition, arr_a, arr_b) -> [ 1 20  3 40  5]

# 2. 结合条件判断实现数据清洗
data = np.random.randn(4, 4)
print(f"原始数据: \n{data}\n")
# 将所有大于 0.5 的值替换为 2, 小于 -0.5 的值替换为 -2, 其余保持不变

result_cleaned = np.where(data > 0.5, 2, np.where(data < -0.5, -2, data))
print(f"数据清洗后: \n{result_cleaned}\n")
# 这是一个嵌套的 np.where, 实现了复杂的条件逻辑, 而完全没有使用循环.
# 外层: np.where(data > 0.5, 2, <否则...>)
# 内层 (<否则...>): np.where(data < -0.5, -2, data)

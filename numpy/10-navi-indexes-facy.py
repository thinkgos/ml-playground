import numpy as np

# 花式索引
# 使用整数数组(或列表)作为索引, 可以一次性地选取、重排或修改任意不连续的元素.这是 NumPy 超越 Python 列表的一大特色.
# NOTE: 花式索引返回的是数据副本.

# 一维数组: arr[[idx1, idx2, ...]]
# 二维数组
#   - 选取特定行: arr[[row1, row2, ...]]
#   - 选取特定元素(按坐标对): arr[[row1, row2], [col1, col2]] (NOTE: 这是选取(row1, col1)和(row2, col2)两个点, 而不是一个矩形区域)

# 创建一个一维数组
arr_1d = np.arange(10, 20)
print(f"原始一维数组: {arr_1d}\n")
# 原始一维数组: [10 11 12 13 14 15 16 17 18 19]
# 1. 选取不连续的元素
indices = [1, 4, 7]
selected_elements = arr_1d[indices]
print(f"arr_1d[[1, 4, 7]] -> {selected_elements}\n")
# arr_1d[[1, 4, 7]] -> [11 14 17]
# 2. 重复选取和重排元素
reordered_elements = arr_1d[[5, 2, 8, 2]]
print(f"arr_1d[[5, 2, 8, 2]] -> {reordered_elements}\n")
# arr_1d[[5, 2, 8, 2]] -> [15 12 18 12]
# --- 二维数组示例 ---
arr_2d = np.arange(1, 17).reshape((4, 4))
print(f"原始二维数组: \n{arr_2d}\n")
# 原始二维数组:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]
# 3. 选取特定的行并重排
# 选取第 3 行, 然后第 0 行, 然后第 2 行
selected_rows = arr_2d[[3, 0, 2]]
print(f"arr_2d[[3, 0, 2]] -> \n{selected_rows}\n")
# arr_2d[[3, 0, 2]] ->
# [[13 14 15 16]
#  [ 1  2  3  4]
#  [ 9 10 11 12]]
# 4. 按坐标对选取特定的元素
# 选取 (0, 1), (2, 3), (3, 0) 三个位置的元素
points = arr_2d[[0, 2, 3], [1, 3, 0]]
print(f"arr_2d[[0, 2, 3], [1, 3, 0]] -> {points}\n")
# arr_2d[[0, 2, 3], [1, 3, 0]] -> [ 2 12 13]

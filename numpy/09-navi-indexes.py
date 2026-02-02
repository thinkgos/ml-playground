import numpy as np

# 基础索引
# 与 Python 列表类似, 通过方括号[]来访问单个元素或一个连续的子集.对于多维数组, 可以使用逗号分隔的索引元组.
# NOTE: 基础切片返回的是原数组的视图(View), 对切片结果的修改会直接反映在原数组上.

# 一维数据
#   - 索引: arr[i]
#   - 切片: arr[start:stop:step](与python list 规则完全相同)
# 多维数组:
#   - 索引: arr[row, col] 或 arr[idx_dim0, idx_dim1, ...]
#   - 切片: arr[start:stop, start:stop]可以对每个维度分别进行切片
#   - 简写: arr[i], 获取第i行全部数据


# 创建一个 3x4 的二维数组
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# 1. 访问单个元素
# 获取第 1 行(索引为1), 第 2 列(索引为2)的元素
element = arr_2d[1, 2]
print(f"arr_2d[1, 2] -> {element}\n")
# arr_2d[1, 2] -> 7
# 2. 切片获取子数组
# 获取前两行 (0, 1) 的后三列 (1, 2, 3)
sub_array = arr_2d[0:2, 1:4]
print(f"arr_2d[0:2, 1:4] -> \n{sub_array}\n")
# arr_2d[0:2, 1:4] ->
# [[2 3 4]
#  [6 7 8]]
# 3. 使用简写获取整行或整列
# 获取第一行 (索引为 0)
first_row = arr_2d[0]  # 等价于 arr_2d[0, :]
print(f"第一行: {first_row}\n")
# 第一行: [1 2 3 4]
# 获取第二列 (索引为 1)
second_col = arr_2d[:, 1]
print(f"第二列: {second_col}\n")
# 第二列: [ 2  6 10]
# 4. 切片赋值
# 将子数组 [0:2, 0:2] 的所有元素都设置为 0
print(f"修改前的 arr_2d: \n{arr_2d}\n")
arr_2d[0:2, 0:2] = 0
print(f"修改后的 arr_2d: \n{arr_2d}\n")
# 修改前的 arr_2d:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
# 修改后的 arr_2d:
# [[ 0  0  3  4]
#  [ 0  0  7  8]
#  [ 9 10 11 12]

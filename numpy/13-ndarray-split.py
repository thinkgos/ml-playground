import numpy as np

# 数组的拆分
# 将一个大数组沿着指定的轴拆分成多个子数组.


# np.split(ary, indices_or_sections, axis=0): 最通用的拆分函数.第二个参数可以是整数(表示平均拆分成几份)或一个一维数组(表示在哪些位置进行拆分), axis 参数指定了拆分的轴/维度.
# np.vsplit(ary, indices_or_sections): Vertical Split(垂直拆分), 是 np.split 在 axis=0 上的便捷封装.
# np.hsplit(ary, indices_or_sections): Horizontal Split(水平拆分), 是 np.split 在 axis=1 上的便捷封装.


# 创建一个 6x4 的数组
arr = np.arange(24).reshape((6, 4))
print(f"原始数组 (6x4): \n{arr}\n")
# 1. 平均拆分
# 使用 hsplit 将其沿列(水平)平均拆分成 2 份
hsplit_result = np.hsplit(arr, 2)
print("水平平均拆分成 2 份 (结果是列表):")
print(f"第一部分: \n{hsplit_result[0]}")
print(f"第二部分: \n{hsplit_result[1]}\n")
# 水平平均拆分成 2 份 (结果是列表):
# 第一部分:
# [[ 0  1]
#  [ 4  5]
#  [ 8  9]
#  [12 13]
#  [16 17]
#  [20 21]]
# 第二部分:
# [[ 2  3]
#  [ 6  7]
#  [10 11]
#  [14 15]
#  [18 19]
#  [22 23]]
# 2. 按位置拆分
# 使用 vsplit 将其沿行(垂直)拆分
# 在第 2 行之后和第 5 行之后进行拆分
# 这会产生三个子数组：arr[0:2], arr[2:5], arr[5:]
vsplit_result = np.vsplit(arr, [2, 5])
print("沿行在位置 [2, 5] 处拆分:")
print(f"第一部分 (0-1行): \n{vsplit_result[0]}\n")
print(f"第二部分 (2-4行): \n{vsplit_result[1]}\n")
print(f"第三部分 (5行): \n{vsplit_result[2]}\n")
# 沿行在位置 [2, 5] 处拆分:
# 第一部分 (0-1行):
# [[0 1 2 3]
#  [4 5 6 7]]
#
# 第二部分 (2-4行):
# [[ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]]
#
# 第三部分 (5行):
# [[20 21 22 23]]

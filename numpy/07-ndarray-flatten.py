import numpy as np

# 将一个多维数组“压平”成一个一维数组.
# ndarray.ravel(): 返回一个展平的视图（如果可能）.修改它可能会影响原始数组.
# ndarray.flatten(): 总是返回一个展平的副本.修改它绝不会影响原始数组.

# 创建一个 2x3 矩阵
a = np.array([[1, 2, 3], [4, 5, 6]])
print(f"原始矩阵 a: \n{a}\n")
# 使用 ravel()
raveled_a = a.ravel()
print(f"ravel() 结果: {raveled_a}")
# ravel() 结果: [1 2 3 4 5 6]
# 使用 flatten()
flattened_a = a.flatten()
print(f"flatten() 结果: {flattened_a}\n")
# flatten() 结果: [1 2 3 4 5 6]
# -- 关键区别：视图 vs 副本 --
# 修改 ravel() 的结果
raveled_a[0] = 100
print(f"修改 ravel() 结果后, 原始矩阵 a: \n{a}\n")
# 修改 ravel() 结果后, 原始矩阵 a:
# [[100   2   3]
#  [  4   5   6]]
# 修改 flatten() 的结果
flattened_a[1] = 200
# 重新创建原始矩阵用于对比
a = np.array([[1, 2, 3], [4, 5, 6]])
print(f"修改 flatten() 结果后, 原始矩阵 a 保持不变: \n{a}\n")
# 修改 flatten() 结果后, 原始矩阵 a 保持不变:
# [[1 2 3]
#  [4 5 6]]

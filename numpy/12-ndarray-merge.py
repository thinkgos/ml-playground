import numpy as np

# 数组的合并
# 将多个数组沿着指定的轴(维度)连接成一个更大的数组.
# NOTE: 除了要拼接的轴外, 其它轴的维度大小必须完全相同

# np.concatenate((a1, a2, ...), axis=0): 最通用的拼接函数.axis 参数指定了拼接的轴.axis=0 表示沿第一个轴(通常是行)拼接, axis=1 表示沿第二个轴(通常是列)拼接.
# np.vstack((a1, a2, ...)): Vertical Stack(垂直堆叠), 是 np.concatenate 在 axis=0 上的一个便捷封装.
# np.hstack((a1, a2, ...)): Horizontal Stack(水平堆叠), 是 np.concatenate 在 axis=1 上的一个便捷封装.


# 创建两个 2x3 的数组
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print(f"arr1: \n{arr1}\n")
print(f"arr2: \n{arr2}\n")
# 1. 使用 concatenate 沿行拼接 (axis=0)
concat_axis0 = np.concatenate((arr1, arr2), axis=0)
print(f"沿行拼接 (axis=0) 的结果 (4x3): \n{concat_axis0}\n")
# 沿行拼接 (axis=0) 的结果 (4x3):
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
# 2. 使用 vstack 实现同样的效果
vstack_result = np.vstack((arr1, arr2))
print(f"vstack 的结果 (与 axis=0 相同): \n{vstack_result}\n")
# 3. 使用 concatenate 沿列拼接 (axis=1)
concat_axis1 = np.concatenate((arr1, arr2), axis=1)
print(f"沿列拼接 (axis=1) 的结果 (2x6): \n{concat_axis1}\n")
# 沿列拼接 (axis=1) 的结果 (2x6):
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]
# 4. 使用 hstack 实现同样的效果
hstack_result = np.hstack((arr1, arr2))
print(f"hstack 的结果 (与 axis=1 相同): \n{hstack_result}\n")

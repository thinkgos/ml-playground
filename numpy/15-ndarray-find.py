import numpy as np

# 高效查找

# np.where(condition, [x, y]): 根据条件 condition, 从 x 和 y 中选择元素. 如果只有 condition, 则返回满足条件的元素的索引.
# np.searchsorted(a, v): 在一个已排序的数组 a 中, 查找 v 中元素应该插入的位置, 以维持数组的有序性.

# 1. np.where 的三元表达式用法
arr = np.arange(1, 11)
print(f"原始数组: {arr}")
# 将所有偶数替换为 0, 奇数替换为 -1
result = np.where(arr % 2 == 0, 0, -1)
print(f"np.where(arr % 2 == 0, 0, -1) -> {result}\n")
# np.where(arr % 2 == 0, 0, -1) -> [-1  0 -1  0 -1  0 -1  0 -1  0]

# 2. np.where 的索引查找用法
arr = np.array([1, 5, 2, 8, 5, 3, 5])
indices = np.where(arr == 5)
print(f"值为 5 的元素的索引: {indices[0]}\n")
# 值为 5 的元素的索引: [1 4 6]


# 3. np.searchsorted
sorted_arr = np.array([10, 20, 30, 40, 50])
# 查找 25 和 30 应该插入的位置
positions = np.searchsorted(sorted_arr, [25, 30])
print(f"在 {sorted_arr} 中查找 [25, 30] 的插入位置: {positions}")
# 在 [10 20 30 40 50] 中查找 [25, 30] 的插入位置: [2 2]
# 默认'left': 25 应该在索引 2 (值为30) 的左边；30 应该在现有 30 (索引2) 的左边
# 使用 side='right'
positions_right = np.searchsorted(sorted_arr, [25, 30], side="right")
print(f"使用 side='right': {positions_right}\n")
# 使用 side='right': [2 3]

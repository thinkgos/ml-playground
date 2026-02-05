import numpy as np

# 集合逻辑,
# 将NumPy数组看作集合, 进行去重、交集、并集等操作. 这些操作对于一维数组非常有用.
# np.unique(ar): 返回数组中不重复的元素, 并已排序.
# np.intersect1d(ar1, ar2): 计算两个数组的交集(共同元素).
# np.union1d(ar1, ar2): 计算两个数组的并集(所有元素, 去重).
# np.isin(ar1, ar2): 返回一个布尔数组, 表示 ar1 中的每个元素是否在 ar2 中.(旧有函数为in1d, 已过时.)
# np.setdiff1d(ar1, ar2): 计算差集, 即在 ar1 中但不在 ar2 中的元素.

names1 = np.array(["Alice", "Bob", "Cathy", "David"])
names2 = np.array(["Bob", "Eva", "David", "Frank"])
print(f"names1: {names1}")
print(f"names2: {names2}\n")

# 1. unique 去重
data = np.array(["A", "B", "C", "A", "B", "D"])
unique_data = np.unique(data)
print(f"unique: {unique_data}\n")
# unique: ['A' 'B' 'C' 'D']

# 2. intersect1d 交集
intersection = np.intersect1d(names1, names2)
print(f"交集: {intersection}\n")
# 交集: ['Bob' 'David']

# 3. union1d 并集
union = np.union1d(names1, names2)
print(f"并集: {union}\n")
# 并集: ['Alice' 'Bob' 'Cathy' 'David' 'Eva' 'Frank']

# 4. isin 成员测试
is_in = np.isin(names1, names2)
print(f"names1 的成员是否在 names2 中: {is_in}")
print(f"基于此筛选出共同成员: {names1[is_in]}\n")
# names1 的成员是否在 names2 中: [False  True False  True]
# 基于此筛选出共同成员: ['Bob' 'David']

# 5. setdiff1d 差集
diff = np.setdiff1d(names1, names2)
print(f"在 names1 中但不在 names2 中的成员: {diff}\n")
# 在 names1 中但不在 names2 中的成员: ['Alice' 'Cathy']

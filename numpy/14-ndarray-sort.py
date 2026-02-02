import numpy as np

# 排序
# np.sort(): 对数组进行排序, axis 参数指定了排序的轴/维度, 返回的是副本. 而.sort()方法是原地排序.
# np.argsort(): 返回排序后, 原始数组中元素的索引. 这是一种“间接排序”, 非常有用

# 创建一个随机一维数组
arr_1d = np.random.randint(1, 100, 10)
print(f"原始一维数组: {arr_1d}\n")
# 1. np.sort() 返回副本
sorted_copy = np.sort(arr_1d)
print(f"np.sort() 的结果 (副本): {sorted_copy}")
print(f"原数组不变: {arr_1d}\n")
# 2. .sort() 原地排序
arr_1d.sort()
print(f".sort() 后原数组被修改(非副本): {arr_1d}\n")
# 3. argsort() 间接排序
scores = np.array([88, 92, 75, 99, 85])
students = np.array(["Alice", "Bob", "Cathy", "David", "Eva"])
print(f"分数: {scores}")
print(f"学生: {students}")
# 获取按分数升序排列的索引
sorted_indices = np.argsort(scores)
print(f"排序后的索引 (argsort): {sorted_indices}")
# 排序后的索引 (argsort): [2 4 0 1 3]
# 使用这个索引来排序学生数组
print(f"按分数排序后的学生: {students[sorted_indices]}\n")
# 按分数排序后的学生: ['Cathy' 'Eva' 'Alice' 'Bob' 'David']
# 4. 多维数组排序
arr_2d = np.random.randint(1, 10, (3, 4))
print(f"原始二维数组: \n{arr_2d}\n")
# 按列排序 (沿 axis=0)
sorted_axis0 = np.sort(arr_2d, axis=0)
print(f"按列排序后: \n{sorted_axis0}\n")
# 按行排序 (沿 axis=1, 默认)
sorted_axis1 = np.sort(arr_2d, axis=1)
print(f"按行排序后: \n{sorted_axis1}\n")

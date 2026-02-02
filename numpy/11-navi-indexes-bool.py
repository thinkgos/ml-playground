import numpy as np

# 布尔索引
# 使用一个布尔类型的数组(通常是通过对原数组进行条件判断生成的)作为索引, 来选取或修改满足条件的元素.这是数据清洗和分析中最常用的技术之一
# 创建一个与原数组 arr 形状相同的布尔数组 bool_mask.使用 arr[bool_mask] 来选取 bool_mask 中为 True 位置对应的 arr 中的元素.

# 创建一个包含随机数据的数组
data = np.random.randn(3, 4)
print(f"原始数据: \n{data}\n")
# 1. 创建布尔掩码
# 找出所有小于 0 的元素
mask_negative = data < 0
print(f"布尔掩码 (data < 0): \n{mask_negative}\n")
# 原始数据:
# [[ 0.44122749 -0.33087015  2.43077119 -0.25209212]
#  [ 0.10961014 -0.89292129  0.22656912 -1.45436567]
#  [ 0.32053531 -0.38028442  0.55245945  0.43441589]]
# 布尔掩码 (data < 0):
# [[False  True False  True]
#  [False  True False  True]
#  [False  True False False]]
# 2. 使用布尔掩码进行筛选
# 获取所有小于 0 的元素, 结果会是一个一维数组
negative_values = data[mask_negative]
print(f"所有小于 0 的值: {negative_values}\n")
# 所有小于 0 的值: [-0.33087015 -0.25209212 -0.89292129 -1.45436567 -0.38028442]
# 3. 使用布尔掩码进行赋值
# 将所有小于 0 的值替换为 0
data[data < 0] = 0  # 这是更简洁的写法
print(f"将负数替换为 0 后的数据: \n{data}\n")
# 将负数替换为 0 后的数据:
# [[0.44122749 0.         2.43077119 0.        ]
#  [0.10961014 0.         0.22656912 0.        ]
#  [0.32053531 0.         0.55245945 0.43441589]]
# 4. 复合条件筛选
# 筛选出绝对值大于 1 的元素
# & 代表 "与", | 代表 "或"
data = np.random.randn(3, 4)  # 重新生成数据
mask_complex = (data > 1) | (data < -1)
print(f"原始数据: \n{data}\n")
print(f"绝对值 > 1 的值: {data[mask_complex]}\n")

import numpy as np

# 聚合运算


# 创建一个随机数组
data = np.random.randn(10) * 10
# 为了方便演示, 我们四舍五入到一位小数
data = np.round(data, 1)
print(f"数据: {data}\n")

# 1. 基本统计
print(f"总和 (sum): {data.sum()}")
print(f"平均值 (mean): {data.mean()}")
print(f"最大值 (max): {data.max()}")
print(f"最小值 (min): {data.min()}")
print(f"标准差 (std): {data.std()}\n")


# 2. 查找索引
print(f"最大值的索引 (argmax): {data.argmax()}")
print(f"最小值的索引 (argmin): {data.argmin()}\n")
# 假设 data.max() 是 13.5, 并且它在索引 3 的位置, 那么 data.argmax() 就返回 3

# 3. 累积运算
cumulative_sum = data.cumsum()
print(f"累积和 (cumsum): {cumulative_sum}\n")
# 举例：如果 data 是 [1, 2, 3], cumsum 结果是 [1, 1+2, 1+2+3] -> [1, 3, 6]
# 创建一个有明显异常值的数据
data_with_outlier = np.array([1, 2, 3, 4, 5, 100])


# 4. 中位数 vs 平均值
print(f"含异常值数据: {data_with_outlier}")
print(f"平均值 (受异常值影响大): {np.mean(data_with_outlier):.2f}")
print(f"中位数 (更稳健): {np.median(data_with_outlier)}\n")
# 含异常值数据: [  1   2   3   4   5 100]
# 平均值 (受异常值影响大): 19.17
# 中位数 (更稳健): 3.5


# 5. 百分位数
scores = np.array([75, 80, 82, 85, 88, 90, 92, 95, 99])
p25 = np.percentile(scores, 25)  # 25% 分位数 (第一四分位数)
p75 = np.percentile(scores, 75)  # 75% 分位数 (第三四分位数)
print(f"考试分数: {scores}")
print(f"25% 分位点: {p25}")
print(f"75% 分位点: {p75}\n")
# 考试分数: [75 80 82 85 88 90 92 95 99]
# 25% 分位点: 82.0
# 75% 分位点: 92.0


# 6. 加权平均值
grades = np.array([90, 85, 95])  # 成绩
weights = np.array([0.2, 0.3, 0.5])  # 权重
weighted_avg = np.average(grades, weights=weights)
print(f"成绩: {grades}, 权重: {weights}")
print(f"加权平均分: {weighted_avg:.2f}\n")
# 成绩: [90 85 95], 权重: [0.2 0.3 0.5]
# 加权平均分: 91.00


# 7. 相关系数
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 3.9, 6.2, 8.1, 9.8])  # y 约等于 2x
corr_matrix = np.corrcoef(x, y)
print(f"x 和 y 的相关系数矩阵: \n{corr_matrix}")
# x 和 y 的相关系数矩阵:
# [[1.         0.99955877]
#  [0.99955877 1.        ]]
# 右上角和左下角的值接近 1, 表示强正相关


# 8. 差分运算
stock_prices = np.array([100, 102, 105, 103, 108])
daily_changes = np.diff(stock_prices)
print(f"每日股价: {stock_prices}")
print(f"每日股价变动 (diff): {daily_changes}")
# 每日股价: [100 102 105 103 108]
# 每日股价变动 (diff): [ 2  3 -2  5]

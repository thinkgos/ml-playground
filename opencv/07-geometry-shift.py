import cv2
import numpy as np

img = cv2.imread('assets/lena.png')

#! 平移
cols, rows = img.shape[:2]
# 定义平移矩阵, 需要是 numpy 的 float32 类型
# 平移矩阵, x 轴平移 100, y 轴平移 50
M = np.float32([[1, 0, 100], [0, 1, 50]])

# 用仿射变换实现平移
dst = cv2.warpAffine(img, M, (rows, cols))
cv2.imwrite('assets/output/lena_geometry_shift.png', dst)

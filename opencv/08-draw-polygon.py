import cv2
import numpy as np

img = np.zeros((300, 512, 3), np.uint8)

#! 画多边形
# 定义四个顶点坐标
pts = np.array([[10, 50], [20, 100], [230, 230], [250, 40]], np.int32)
# 顶点个数: 4, 矩阵变成 4*1*2 维
# 第一个表示点的数量, 第二个表示通道, 第三个表示坐标
pts = pts.reshape((-1, 1, 2))
# 如果画多条直线, 可以一次性传多个2*1*2维的数组
cv2.polylines(img, [pts], True, (0, 255, 255), 5)
cv2.imwrite("assets/output/draw_polygon.png", img)

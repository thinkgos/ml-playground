import cv2

img = cv2.imread("assets/lena.png")

#! 翻转
# 参数2: = 0 表示垂直翻转,
#       > 0 表示水平翻转
#       < 0 表示垂直水平翻转
img4 = cv2.flip(img, 1)
cv2.imwrite("assets/output/lena_geometry_flip_horizontal.png", img4)

import cv2

img = cv2.imread('assets/lena.png')

#! 旋转
# 同平移一样, 也是用仿射变换实现的. 因此需要定义一个变换矩阵.
cols, rows = img.shape[:2]

# 参数1: 图片的旋转中心
# 参数2: 旋转角度(正: 逆时针, 负: 顺时针)
# 参数3: 缩放比例, 0.5 表示缩小一半
M = cv2.getRotationMatrix2D((rows / 2, cols / 2), 45, 0.5)
dst = cv2.warpAffine(img, M, (rows, cols))
cv2.imwrite('assets/output/lena_geometry_rotate.png', dst)
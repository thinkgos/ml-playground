import cv2

img = cv2.imread('assets/lena.png')

#! 缩放
# 按照指定的宽度、高度缩放图片
img1 = cv2.resize(img, (132, 150))
cv2.imwrite('assets/output/lena_geometry_resize_shrink1.png', img1)

# 按照比例缩放, 如 x,y 轴均缩小一倍, interpolation 采用缩放方法, 默认采用插值
img2 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imwrite('assets/output/lena_geometry_resize_shrink2.png', img2)

# 按照比例缩放, 如 x,y 轴均放大一倍
img3 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
cv2.imwrite('assets/output/lena_geometry_resize_zoom.png', img3)

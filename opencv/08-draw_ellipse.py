import cv2
import numpy as np

img = np.zeros((300, 512, 3), np.uint8)

#! 画椭圆
# 只需要定义椭圆的中心(x,y), x/y轴的长度, 以及angle旋转角度, startAngle椭圆的起始角度和endAngle椭圆的结束角度, 以及线的颜色和线宽即可.
cv2.ellipse(img, (256, 150), (200, 100), 0, 0, 360, (255, 255, 0), -1)
cv2.imwrite('assets/output/draw_ellipse.jpg', img)
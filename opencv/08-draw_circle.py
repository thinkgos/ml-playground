import cv2
import numpy as np

img = np.zeros((300, 512, 3), np.uint8)

#! 画圆
# 只需要定义圆的中心和半径, 以及线的颜色和线宽即可. 这里的线宽为-1表示填充圆.
cv2.circle(img, (256, 150), 100, (0, 0, 255), -1)
cv2.imwrite('assets/output/draw_circle.jpg', img)
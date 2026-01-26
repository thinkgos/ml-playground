import cv2
import numpy as np

img = np.zeros((300, 512, 3), np.uint8)

#! 画矩形
# 只需要定义矩形的左上角和右下角, 以及线的颜色和线宽即可.
cv2.rectangle(img, (50, 100), (400, 200), (0, 255, 0), 5)
cv2.imwrite("assets/output/draw_rect.png", img)

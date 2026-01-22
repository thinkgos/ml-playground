import cv2
import numpy as np

img = np.zeros((300, 512, 3), np.uint8)

#! 画线
# 只需要定义起始点和终止点, 以及线的颜色和线宽即可.
cv2.line(img, (0, 0), (512, 300), (255, 0, 0), 5)
cv2.imwrite('assets/output/draw_line.jpg', img)

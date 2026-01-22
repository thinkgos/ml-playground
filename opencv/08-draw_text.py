import cv2
import numpy as np

img = np.zeros((300, 512, 3), np.uint8)

#! 添加文字
cv2.putText(
    img,
    "OpenCv", # 要增加的文本
    (50, 250), # 文字的起始位置(左下角为起始点)
    cv2.FONT_HERSHEY_SIMPLEX, # 字体
    2, # 文字大小
    (255, 255, 255), # 文字颜色
    lineType=cv2.LINE_AA,
)
cv2.imwrite('assets/output/draw_text.jpg', img)
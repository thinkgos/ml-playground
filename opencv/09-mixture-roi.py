import numpy as np
import cv2

#! 拉位操作
img1 = cv2.imread('assets/lena.png')
logo = cv2.imread('assets/logo.png')

# 把log放在左上角, 只关心这一区域
rows, cols = logo.shape[:2]

# 创建掩膜
logo2gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(logo2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# 只对roi区域进行融合
roi = img1[:rows, :cols]
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
dst = cv2.add(img1_bg, logo)  # 进行融合
img1[:rows, :cols] = dst  # 融合后放在原图上
cv2.imwrite('assets/output/lena_mixture_logo.png', img1)

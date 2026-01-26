import cv2

img = cv2.imread("assets/lena.png", cv2.IMREAD_COLOR)

# img[:, :, 0] # 蓝色通道
print(img[100, 2])  # (100,2) 的像素值

# ROI 感兴趣区域
roi = img[100:220, 120:250]
cv2.imwrite("assets/output/lena_operator_roi.png", roi)

# 通道分割与合并, 最好是使用numpy中的索引
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

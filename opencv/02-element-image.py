import cv2

# 读取图片
img = cv2.imread('assets/lena.png', cv2.IMREAD_COLOR)
print(img.shape)
# 转换为灰度图
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('assets/output/lena_gray.png', img)

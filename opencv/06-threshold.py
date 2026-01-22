import cv2

img = cv2.imread('assets/lena.png', cv2.IMREAD_GRAYSCALE)

#! 固定阀值
# 就是像素点值大于阈值变成一类值，小于阈值变成另一类值
# 参数1: 图片, 一般是灰度图
# 参数2: 设定的阀值
# 参数3: 对于THRESH_BINARY、THRESH_BINARY_INV阈值方法所选用的最大阈值，一般为255
# 参数4: 阀值方式, 有五种
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('assets/output/lena_threshold_binary.png', th1)
ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imwrite('assets/output/lena_threshold_binary_inv.png', th2)
ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
cv2.imwrite('assets/output/lena_threshold_trunc.png', th3)
ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
cv2.imwrite('assets/output/lena_threshold_tozero.png', th4)
ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imwrite('assets/output/lena_threshold_tozero_inv.png', th5)

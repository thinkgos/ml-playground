import cv2

img = cv2.imread("assets/lena.png", cv2.IMREAD_GRAYSCALE)
# 边缘检测, canny算法
edges = cv2.Canny(img, 30, 70)

cv2.imwrite("assets/output/lena_canny.png", edges)

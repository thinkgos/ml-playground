import cv2

img = cv2.imread("assets/sun.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ! 轮廓
# 轮廓是一系列相连的点组成的曲线, 代表了物体的基本外形.
# 轮廓是连续的, 边缘并不全都连续.
# 其实边缘主要是作为图像的特征使用, 比如可以用边缘特征可以区分脸和手,
# 而轮廓主要用来分析物体的形态, 比如物体的周长和面积等,
# 可以说边缘包括轮廓
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 寻找二值化图中的轮廓
contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE,
)
# 绘制找出来的轮廓
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
img = cv2.imwrite("assets/output/sun_contour.png", img)

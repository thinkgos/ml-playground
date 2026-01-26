import cv2

img = cv2.imread("assets/lena.png", cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("assets/output/lena_convert_gray.png", img)

# TODO: 转换为 HSV 颜色空间
# https://codec.wang/docs/opencv/start/changing-colorspaces
# HSV 颜色空间, 常用于特定颜色物体追踪
# https://baike.baidu.com/item/HSV%E9%A2%9C%E8%89%B2%E6%A8%A1%E5%9E%8B/21501482?fromtitle=HSV&fromid=547122

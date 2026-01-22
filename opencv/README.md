# opencv

## 1. 基本环境

[01-basic](01-basic.py)

## 2. 基本元素 - 图片

`opencv`上的彩色图是以**B-G-R**格式存储的, 灰度图只有一个通道.  
图像坐标的起始点`(0, 0)`是在**左上角**, 所以行对应的是y, 向下增长, 列对应的是x, 向右增长.  
在`opencv`中, `shape`为`(y, x, z)`, 其中`y`为图像的高度, `x`为图像的宽度, `z`为图像的通道数.

[02-element-image](02-element-image.py)

## 3. 从摄像头读取视频

`cv2.VideoCapture()`, `cv2.VideoWriter()`

## 4. 图像基本操作

- ROI感兴趣的区域
- 获取宽高通道属性
- 分离和合并图像通道

[04-operator](04-operator.py)

## 5. 颜色空间转换

[05-color-convert](05-color-convert.py)

## 6 阀值分割

使用固定阀值, 自适应阀值和Otsu阀值法"二值化"图像

[固定阀值](06-threshold.py)
[自适应阀值](06-threshold-adaptive.py)

## 7. 图像几何变换

缩放, 翻转, 旋转, 平移

[resize缩放](07-geometry-resize.py)
[flip翻转](07-geometry-flip.py)
[shift平移](07-geometry-shift.py)
[rotate旋转](07-geometry-rotate.py)

## 8. 绘图

[画线](08-draw_line.py)
[画矩形](08-draw_rect.py)
[画圆](08-draw_circle.py)
[画椭圆](08-draw_ellipse.py)
[画多边形](08-draw_polygon.py)
[添加文字](08-draw_text.py)

## 9. 图像混合

[图像混合](09-mixture.py)
[图像混合-ROI](09-mixture-roi.py)

## 10 平滑图像

模糊/平滑图片来消除图片噪声.  
滤波与模糊都属于卷积, 不同滤波方法之间只是卷积核不同(对线性滤波而言)  
低通滤波器是模糊, 高通滤波器是锐化.

- 低通滤波器就是允许低频信号通过, 在图像中边缘和噪点都相当于高频部分, 所以低通滤波器用于去除噪点、平滑和模糊图像.  
- 高通滤波器则反之, 用来增强图像边缘, 进行锐化处理.

[均值滤波](10-filter_linear_blur.py)
[方框滤波](10-filter_linear_box.py)
[高斯滤波](10-filter_linear_gaussian.py)
[中间滤波](10-filter_non_linear_median.py)
[双边滤波](10-filter_non_linear_bilateral.py)

## 11. 边缘检测

TODO

## 12. 形态学操作

膨胀, 腐蚀, 开运算, 闭运算.

形态学操作一般作用于二值化图(也可直接作用于原图), 来连接相邻的元素或分离成独立的元素. 腐蚀和膨胀是针对图片中的白色部分!

`kernel`核也叫结构元素, 形态学操作其实也是应用卷积来实现的, 结构元素可以是矩形/椭圆/十字形，可以用`cv2.getStructuringElement()`来生成不同形状的结构元素

```python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 矩形结构
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))  # 椭圆结构
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))  # 十字形结构
```

### 12.1 腐蚀

腐蚀的效果是把图片"变瘦"，其原理是在原图的小区域内取局部最小值.`cv2.erode`

[腐蚀](12-morphology_erode.py)

### 12.2 膨胀

膨胀的效果是把图片"变胖"，其原理是在原图的小区域内取局部最大值.`cv2.dilate`

[膨胀](12-morphology_dilate.py)

### 12.3 开运算

开运算是先腐蚀后膨胀，其作用是去掉小的物体，保留大的物体. `cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)`

[开运算](12-morphology_open.py)

### 12.4 闭运算

闭运算是先膨胀后腐蚀，其作用是填充物体内部的空洞，保留物体的边界. `cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)`

[闭运算](12-morphology_close.py)

- 如果我们的目标物体外面有很多无关的小区域，就用**开运算**去除掉
- 如果物体内部有很多小黑洞，就用**闭运算**填充掉

### 12.5 形态学梯度

形态学梯度是膨胀减去腐蚀的结果，其作用是保留物体的边界, 会得到物体的轮廓. `cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)`

### 12.6 礼帽

礼帽是原始图像减去开运算的结果，其作用是突出物体的轮廓. `cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)`

### 12.7 黑帽

黑帽是闭运算减去原始图像，其作用是突出物体的内部空洞. `cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)`

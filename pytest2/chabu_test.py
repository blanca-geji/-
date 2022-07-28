import numpy as np
import cv2 as cv

img2 = np.zeros((200, 200, 3), np.uint8)  # 生成一个空灰度图像

# 起点和终点的坐标
ptStart = (20, 0)
ptEnd   = (199, 40)
point_color = (255, 255, 255)  # BGR
thickness = 1
lineType = 4
cv.line(img2, ptStart, ptEnd, point_color, thickness, lineType)

cv.namedWindow("image2")
cv.imshow('image2', img2)
cv.waitKey (10000) # 显示 10000 ms 即 10s 后消失
cv.destroyAllWindows()
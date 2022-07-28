import cv2
import numpy as np
import math
a=np.load('line_output.npy')
graphTable=a.tolist()

img2 = np.zeros((2744, 2744, 3), np.uint8)  # 生成一个空灰度图像
cv2.namedWindow("line_img",cv2.WINDOW_NORMAL)
cv2.imshow("line_img", img2)
count=0


for i in range(0,13824,1):

    #if graphTable[i][4]>0:
    cv2.line(img2, (int(graphTable[i][0]), int(graphTable[i][1])), (int(graphTable[i][2]),int(graphTable[i][3])), 1, 4)
    count=count+1
    print('now: ', count, ' /13824 ')

cv2.waitKey(0)
cv2.imshow("line_img", img2)
print('hello')




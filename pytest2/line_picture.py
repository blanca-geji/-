import random
import cv2
import numpy as np
import math


#   计算每条线的像素值得函数
def count_line_value(x1,y1,x2,y2):
    XE=point_lis[x2][y2][0]-point_lis[x1][y1][0]
    YE=point_lis[x2][y2][1]-point_lis[x1][y1][1]

    start_point_x=point_lis[x1][y1][0]
    start_point_y=point_lis[x1][y1][1]
    end_point_x = point_lis[x2][y2][0]
    end_point_y = point_lis[x2][y2][1]

    line_length=math.sqrt(math.pow(XE,2)+math.pow(YE,2))
    line_value = 0
    step_count = abs(XE) + abs(YE)  # 逐点比较数步数
    error = 0  # 偏差判别标志位
    x_index = y_index = 0
    for step in range(0, step_count):
        if error >= 0:  # 判断XE YE是因为在不同象限XE YE 的进给方向不一样
            if XE >= 0:
                x_index = x_index + 1
            else:
                x_index = x_index - 1
            error = error - abs(YE)
        else:
            if YE >= 0:
                y_index = y_index + 1
            else:
                y_index = y_index - 1
            error = error + abs(XE)
        #print(start_point_y + y_index, start_point_x + x_index)
        line_value=img[start_point_y+y_index,start_point_x+x_index]+line_value  # 图像像素点的索引值
    line_value=line_value/line_length   #归一化操作，消除线段长度的差别
    if line_value<100:
       ptStart = (start_point_x, start_point_y)
       ptEnd = (end_point_x, end_point_y)
       point_color = (255, 255, 255)  # BGR
       cv2.line(img2, ptStart, ptEnd, point_color, 1, 4)
       cv2.imshow('line_img', img2)
    #cv2.waitKey(1000)  # 显示 10000 ms 即 10s 后消失
    print("table",i,j,k,m,"\r")
    print("point:",start_point_x,start_point_y,end_point_x,end_point_y)
    line_output.append((start_point_x,start_point_y,end_point_x,end_point_y,line_value))
    #print(line_value,line_length)

line_output=[]

# 读取并返回黑白图
img = cv2.imread("test3.jpg", 0)
img=img[56:2800,0:2744]   #  截取原图像
cv2.namedWindow("raw_img",0)
cv2.imshow("raw_img", img)


img = cv2.GaussianBlur(img, (3, 3), 0)  # 用高斯滤波处理原图像降噪
img= cv2.Canny(img, 50, 150)  # 50是最小阈值,150是最大阈值
cv2.namedWindow("canny",0) #可调大小
cv2.namedWindow("1",0)  #可调大小
cv2.imshow('canny', img)



img2 = np.zeros((2744, 2744, 3), np.uint8)  # 生成一个空灰度图像
cv2.namedWindow("line_img",cv2.WINDOW_NORMAL)
cv2.imshow("line_img", img2)


# get the shape message of the picture
sp = img.shape[0:2]
print(sp)

# x = np.empty([19,19], dtype = int)

b=0
item0=[]
item1=[]
item2=[]
item3=[]
k = range(56,2744,56)
for i in k :
    item0.append((i  ,  0))
    item1.append((2743,  i))
for i in range  (2688,0,-56):
    item2.append((i  ,2743))
    item3.append((0  ,  i))


print(item0)
#  将坐标重新打包成一个二维数组
#  在二维数组的数据结构下更好遍历所有的线段
#point_lis = list(zip(item0,item1))
point_lis=[item0,item1,item2,item3]
i=j=k=m=0
count=0
lis1=range(0,48)

#  遍历所有的可能连线
for i in lis1:
    for j  in lis1 :
        for k in range(i+1,4):
            for m in  lis1:
                count=count+1
                print ('now: ',count,' /13824 ')
                count_line_value(i,j,k,m)

#  保存数据
m=np.array(line_output)
np.save('line_output.npy',m)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("testgrad.jpg", img)



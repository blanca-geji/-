import math
def count_line_value(x1,y1,x2,y2):
    XE=z[x1][y1][0]-z[x2][y2][0]
    YE=z[x1][y1][1]-z[x2][y2][1]
    line_length=math.sqrt(XE^2+YE^2)
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
        print(x_index, y_index)
        #  line_value=  # 图像像素点的索引值
    # line_value=line_value/line_length   #归一化操作，消除线段长度的差别

                     


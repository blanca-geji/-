import turtle

'''初始化坐标系'''
t = turtle.Pen()
t.goto(0,0)
t.goto(-200,0)
t.goto(200,0)
t.goto(0,0)
t.goto(0,200)
t.goto(0,-200)
t.goto(0,0)

XE = int(input("请输入终点横坐标(<=200)："))
YE = int(input("请输入终点纵坐标(<=200)："))
#NXY为一共需要步进的次数
NXY = abs(XE)+abs(YE)
#FM为偏差计算
FM=0
#XOY标识象限
XOY = 0
#ZF标识步进种类（ZF=1为+x，ZF=2为-x，ZF=3为+y，ZF=4为-y）
ZF = 0

if(XE>0 and YE>0):
    XOY = 1
elif(XE<0 and YE>0):
    XOY = 2
elif(XE<0 and YE<0):
    XOY = 3
elif(XE>0 and YE<0):
    XOY = 4
#验证
'''
print("终点坐标为","(",XE,YE,")")
print("终点在第",XOY,"象限")
print("NXY:",NXY)
'''
#循环
for i in range(1,NXY):
    if(FM>=0):
        if(XOY==1 or XOY==4):
            ZF = 1
        else:
            ZF = 2
        FM = FM - abs(YE)
    else:
        if(XOY==1 or XOY==2):
            ZF = 3
        else:
            ZF = 4
        FM = FM + abs(XE)
    #步走控制程序
    if(ZF==1):
        t.forward(1)
    elif(ZF==2):
        t.backward(1)
    elif(ZF==3):
        t.left(90)
        t.forward(1)
        t.right(90)
    elif(ZF==4):
        t.right(90)
        t.forward(1)
        t.left(90)

exit = input("press space to exit")

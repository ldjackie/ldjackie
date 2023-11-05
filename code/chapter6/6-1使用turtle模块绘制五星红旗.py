import math
import turtle as t
t.setup(960,640,10,10)  	# 设置矩形尺寸和位置
t.bgcolor("red")		# 设置背景色
t.pencolor("black")     	# 设置分割线的画笔颜色
t.speed(5)              	# 设置画笔速度
# 画横线
t.penup()               	# 提起画笔
t.goto(-480, 0)         	# 将画笔移动到指定位置
t.pendown()		# 放下画笔
t.forward(960) 		# 从指定位置绘制960像素的一条线
# 画竖线
t.penup()			# 提起画笔
t.seth(-90)             	# 改变画笔方向
t.goto(0, 320)         	# 将画笔移动到指定位置
t.pendown()		# 放下画笔
t.forward(640)          	# 从指定位置绘制640像素的一条线


# 画横线
t.penup()
t.seth(0)
for i in range(9):			# 通过循环，绘制10条横辅助线
    t.goto(-480,288-i*32)
    t.pendown()
    t.forward(480)
    t.penup()
# 画竖线
t.penup()
t.seth(-90)
for i in range(14):			# 通过循环，绘制15条竖辅助线
    t.goto(-448+i*32,320)
    t.pendown()
    t.forward(320)
    t.penup()


# 画五个星星连线
t.pencolor("white")	# 将画笔颜色设置为白色
t.goto(-32*10,32*5)
t.pendown()
t.goto(-32*5,32*8)
t.penup()
t.goto(-32*10,32*5)
t.pendown()
t.goto(-32*3,32*6)
t.penup()
t.goto(-32*10,32*5)
t.pendown()
t.goto(-32*3,32*3)
t.penup()
t.goto(-32*10,32*5)
t.pendown()
t.goto(-32*5,32*1)
t.penup()

# 画大五角星
t.penup()
t.pencolor("yellow")
t.fillcolor("yellow")
t.goto(-32*10,32*5)
t.pendown()
t.seth(90)
t.forward(96)
t.right(162)
t.begin_fill()
for i in range(5):
    t.forward(-math.cos(54)*96*2)
    t.right(144)
t.end_fill()
t.penup()

#画小五角星1
t.goto(-32*5,32*8)
t.pendown()
t.seth(-90-math.atan(5/3)*180/3.14)
t.forward(32)
t.right(162)
t.begin_fill()
for i in range(5):
    t.forward(-math.cos(54)*32*2)
    t.right(144)
t.end_fill()
t.penup()
#画小五角星2
t.goto(-32*3,32*6)
t.pendown()
t.seth(-90-math.atan(7/1)*180/3.14)
t.forward(32)
t.right(162)
t.begin_fill()
for i in range(5):
    t.forward(-math.cos(54)*32*2)
    t.right(144)
t.end_fill()
#画小五角星3
t.penup()
t.goto(-32*3,32*3)
t.pendown()
t.seth(90+math.atan(7/2)*180/3.14)
t.forward(32)
t.right(162)
t.begin_fill()
for i in range(5):
    t.forward(-math.cos(54)*32*2)
    t.right(144)
t.end_fill()
#画小五角星4
t.penup()
t.goto(-32*5,32*1)
t.pendown()
t.seth(90+math.atan(5/4)*180/3.14)
t.forward(32)
t.right(162)
t.begin_fill()
for i in range(5):
    t.forward(-math.cos(54)*32*2)
    t.right(144)
t.hideturtle()	# 隐藏turtle的画笔形状
t.end_fill()
t.done()		#暂停程序，停止画笔绘制，保持绘图窗体不关闭
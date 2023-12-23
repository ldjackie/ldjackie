import os,turtle

def readpos(file):			#读取坐标文件，返回list坐标数据
    if not os.path.exists(file):	#检验坐标文件是否存在
        print("file lost!")
        return
    pos=list()			#声明pos保存坐标信息
    with open(file,"rb+") as fileobj:	#以rb+模式打开字节文件
        while True:
            byte1=fileobj.read(2)	#读取2个字节，作为坐标x值
            byte2=fileobj.read(2)	#读取2个字符，作为坐标y值
            if not byte1:		#检测是否到达文件结尾
                break
	    #将字节数据转型为整形数据
            n1=int.from_bytes(byte1,byteorder="big",signed=True)
            n2=int.from_bytes(byte2,byteorder="big",signed=True)
            pos.append((n1,n2))	#坐标x，y构成元组，追加到pos中
    return pos

def drawtracks(pos):		#根据pos坐标列表，绘制轨迹
    if not pos :			#检验pos列表
        return
    scr = turtle.Screen()		#获取turtle屏幕，出来点击事件
    turtle.setup(1124,800)		#设置屏幕尺寸
    turtle.title("轨迹绘制")		#设置标题
    turtle.bgpic('./sd.gif')		#设置背景地图
    turtle.speed(2)		#设置绘制速度
    turtle.penup()			#抬起笔触，准备移动画笔坐标
    turtle.goto(pos[0][0],pos[0][1])	#画笔移动到第一个坐标点
    turtle.pendown()		#落下笔触，准备绘制轨迹
    turtle.color("yellow")		#设置画笔颜色
    for tp in  pos[1:]:		#遍历坐标点，绘制轨迹
        turtle.goto(tp[0],tp[1])
        turtle.circle(2)		#坐标点绘制圆形标注
    scr.exitonclick()		#点击屏幕退出

if __name__ == "__main__":
    file="./position.dat"
    pos=readpos(file)
    drawtracks(pos)
number = int(input("请输入一个数字："))
res = 1
#判断数字是负数，0或者正数
if number<0:
    print("输入有误，负数没有阶乘")
elif number == 0:
    print("0的阶乘为1")
else:
    for i in range(1,number+1):
        res = res*i
    print("%d的阶乘为%d"%(number,res))
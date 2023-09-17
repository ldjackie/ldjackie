#!/usr/bin/env Python3
#输入温度
a = float(input('请输入摄氏温度：'))
b = float(input('请输入华氏温度：'))
#转换温度
c = a * 1.8 + 32
d = (b - 32) / 1.8
#输出输出结果
print("摄氏温度{}转换为华氏温度为：{}".format(a,c))
print("华氏温度{}转换为摄氏温度为：{}".format(b,d))
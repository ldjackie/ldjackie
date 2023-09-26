#引用math模块
import math
# 三边a b c三个参数
def test(a, b, c):
 # 根据三角形特性，两边之和大于第三边来做判断
    if a+b > c and a+c > b and b+c > a:         
        p = (a+b+c)/2
        temp = p*(p-a)*(p-b)*(p-c)
   # 调用math函数里的sqrt方法
        s = math.sqrt(temp)                                    
        print("可以构成三角形，面积为: ", s)
    else:
        print("三边不能构成三角形！！")
while True:
    if __name__=='__main__':
        x = float(input("请输入第一条边："))
        y = float(input("请输入第二条边："))
        z = float(input("请输入第三条边："))
        test(x, y, z)
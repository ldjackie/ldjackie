#方法一：直接输出
def fib1(n):
    f1=1
    f2=1
    if (n==1 or n==2):
        return 1
    else:
        for i in range(3,n+1):
            f1,f2 = f2,f1+f2
        return f2
#输出：8

#方法二：使用递归
def fib2(n):
    if (n==1 or n==2):
        return 1
    else:
        return fib2(n-1)+fib2(n-2)
#当需要斐波那契数列的第六项时
print(fib1(6))
print(fib2(6))
#输出：8
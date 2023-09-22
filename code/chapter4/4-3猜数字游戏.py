#引入生成随机数的模块
import random
#程序设定生成 1-60 之间的一个随机数，让用户猜
randomNum = random.randint(1,60)
print("这个神秘数字是在1-60之间。")
#设定用户只能猜 3 次
for number in range(1,4):
    print("请输入你猜测的数字：")
    guessNum = int(input( ))
    if guessNum == 0:
        break
    if guessNum < randomNum:
        print("猜小咯")
    elif guessNum > randomNum:
        print("猜大咯")
    else:
        break
if(guessNum == randomNum):
    print("恭喜你，猜对啦！")
else:
    print("很遗憾，正确的数字是",str(randomNum))
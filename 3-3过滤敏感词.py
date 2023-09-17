#!/usr/bin/env Python3
words = ("垃圾","辣鸡","不要脸","死亡","赌博")
text = input('请输入你的文字：')
for word in words:
    if word in text:
        text = text.replace(word, "*")
print('过滤后的文本内容为：',text)
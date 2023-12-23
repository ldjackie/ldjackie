import wordcloud,os,jieba

def readwords(file):
    words={}		#存放词语的字典
    fileobj=open(file,mode="r",encoding="UTF-8")	#以文本可读方式打开文件
    try:
        while True:
            wd=fileobj.readline().strip('\n')		#按行读取，删除‘\n’
            if not wd:		#词语读取结束
                break
            if len(wd)<2:		#词语长度小于2
                continue
            if words.get(wd):	#保存词语
                words[wd]+=1
            else:
                words[wd]=1
    finally:
        fileobj.close()
    #排序，并返回前50个词语
    wordlist=sorted(words.items(),key=lambda x:x[1],reverse=True)
    return wordlist[:50]

def showpic(wdlist):
    wc=wordcloud.WordCloud(background_color="white",	#设置词语
                           font_path="./fzhcjw.ttf",
                           width=800,height=600,margin=2)
    wdstr=""		#待生成词云的字符文本
    for wd in wdlist:
        wdstr+=(wd[0]+" ")*wd[1]
    wc.generate(wdstr)	#产生词云
    wc.to_file("wordCloud.png")	#保存未图片

if __name__ == "__main__":
    file="./十四五.txt"
    wdlist=readwords(file)
    showpic(wdlist)
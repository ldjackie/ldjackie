from snownlp import SnowNLP
# 读取文章内容，数据格式是列表list
with open("二十大报告全文.txt", "r", encoding="utf-8") as f:
    text_list = f.readlines()
text_string = "".join(t for t in text_list)  # 将列表转为文本字符串str

# 中文字符串处理类
s = SnowNLP(text_string)

# 统计关键词
keywords = s.keywords(3)  # 统计前3个关键词
print("关键词：", keywords)

# 分词
words = s.words  # 分词列表
w = list()
w.append(words)

# 词频
s = SnowNLP(w)  # 分词列表w,元素为列表
tf = s.tf  # 获取词频
for dictionary in tf:
  # print(dictionary)
  # 字典按键值由大至小排序
    for k, v in sorted(dictionary.items(), key=lambda d: d[1], reverse=True):
        if len(k) > 1:   # 词语在两个字符以上
            print("%s\t\t%d" % (k, v))
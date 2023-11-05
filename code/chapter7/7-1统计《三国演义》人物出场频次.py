import jieba
# 排除词库
excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如此", "商议", "如何", "主公", "军士", "左右", "军马", "引兵", "次日", "大喜", "天下", "东吴", "于是", "今日", "不敢", "魏兵","人马", "陛下", "一人"}
# 以只读方式读取文本内容，文本编码为uft-8
txt = open("三国演义.txt", "r", encoding="utf-8").read()
# 用lcut()进行分词
words = jieba.lcut(txt)
counts = {}
# 统一处理人名信息，例如诸葛亮和孔明为同一人物
# 可根据小说原文自行添加
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
        counts[rword] = counts.get(rword, 0) + 1
# 清洗无用词
for word in excludes:
    del(counts[word])
# 将人名转为列表并进行排序
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
# 输出排名前10的人物
for i in range(10):
    word, count=items[i]
    print(word, count)
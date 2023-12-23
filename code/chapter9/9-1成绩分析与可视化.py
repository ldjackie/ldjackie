import numpy as np
import matplotlib.pyplot as plt

# 根据均值、标准差,求指定范围的正态分布概率值
def normfun(x, mu, sigma):
    pdf = np.exp(-((x - mu)**2)/(2*sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf

#读取分数文件，绘制直方图
def scoreAna(filename):
    plt.rcParams['font.family'] = 'Microsoft YaHei' #用来正常显示中文标签
    score_data=np.loadtxt(filename)
    x = np.arange(min(score_data), max(score_data), 1)
    nor_data= normfun(x, score_data.mean(), score_data.std())
    flag1, =plt.plot(x, nor_data,"r-") #画出理论的正态分布概率曲线
    score_x=range(0,101,10)
    plt.hist(score_data,bins=score_x ,density=True)
    plt.xlabel("分数")
    plt.ylabel("人数")
    plt.title("成绩分布")
    plt.legend([flag1],["正态分布曲线"])
    plt.show()

if __name__ == '__main__':
    scoreAna("scores01.csv")

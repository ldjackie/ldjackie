import numpy as np
import matplotlib.pyplot as plt

def covidAna(filename):	#绘制疫情图表的方法
    #读取疫情数据
    covid_data=np.loadtxt(filename,dtype=int,skiprows=1,encoding="UTF-8",usecols=(1,2,3),delimiter=',')
    #读取日期
    covid_date=np.loadtxt(filename,dtype=str,skiprows=1,encoding="UTF-8",usecols=(0),delimiter=",")
    #读取首行
    covid_title=np.loadtxt(filename,dtype=str,encoding="UTF-8",max_rows=1,delimiter=",")
    plt.style.use("ggplot")	#设置图标风格，背景带有网格线
    plt.rcParams['font.family'] = 'Microsoft YaHei'  # 用来正常显示中文标签
    line1,line2,line3, =plt.plot(covid_date,covid_data)	#绘制折线
    plt.xticks(range(len(covid_date)),covid_date,rotation=90)	#设置x轴标题
    plt.xlabel('日期')
    plt.ylabel('人数')
    plt.legend([line1,line2,line3],covid_title[1:])	#绘制图例
    plt.show()

if __name__ == '__main__':
   covidAna("covid-us.csv")

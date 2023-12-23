from pyecharts import options as opts
from pyecharts.charts import Map
import numpy as np
#渲染地理图表
def weatherAna(filename):
	#读取降水量数据
    wea_data=np.loadtxt(filename,dtype=str,delimiter=",",encoding="GBK")
    map=(
        Map().add("降雨(mm)",wea_data,"河南")
        .set_global_opts(title_opts=opts.TitleOpts(title="河南省降水示例"),
	visualmap_opts=opts.VisualMapOpts(max_=300,is_piecewise=True))
    	)
    map.render("weather.html")	#渲染html文件

if __name__ == '__main__':
   weatherAna("weather.csv")

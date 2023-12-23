# 编码格式UTF-8
# 所属项目pythonBK，代码文件logFilter.py
# Author Freshen 2021/5/25 15:25
import os,shutil

def readlog(filename):
    ipall = dict()		#定义dict保存IP地址和次数
    if not os.path.exists(filename):		#判定文件是否存在
        print("文件%s丢失"%filename )
        return
    with open(filename,"r") as fileobj:		#只读模式打开文件
        print("====日志文件分析开始====")
        while True:			#循环读取每一行数据
            line = fileobj.readline()
            # print("……")
            if not line:		#读取不到数据，结束循环
                break;
            if line.find("python-requests"):		#判定是否含有指定内容
                ipstr = line[:line.index("-")]		#截取IP地址
                if ipall.get(ipstr):			#地址曾保存，则计数累加
                    ipall[ipstr] += 1
                else:						#地址未保存，则计数为1
                    ipall[ipstr] = 1
    return ipall			#返回所有IP地址信息

if __name__ == '__main__':
    filepath = "./ip-request.log"		#日志文件
    ipdict = readlog(filepath)
	#按照dict数据的值降序排列数据
    ipdict = sorted(ipdict.items(),key=lambda x: x[1],reverse=True)
    for ip in ipdict[:10]:		#输出前10项数据
        print("IP:%s\t访问次数:%s"%(ip[0],ip[1]))
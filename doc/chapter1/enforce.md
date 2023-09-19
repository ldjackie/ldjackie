# 1  安装并配置Python开发环境

## 1.4 任务实施

### 1.4.1 安装Python并配置环境变量

​	**1. 任务描述**

​	本任务主要是在Windows操作系统上进行Python解释器的下载、安装和基本设置，配置Python环境变量，并完成集成开发环境PyCharm的下载、安装和使用，最终分别能在命令提示符下和PyCharm下运行简单的Python程序。

​	**2. 工作内容**

​	1）安装Python解释器

​	Python可应用于多平台，包括Linux、Windows和Mac OS X等。现以Windows操作系统为例，演示Python解释器的下载和安装过程。具体步骤如下。

​	（1）访问Python官网 https://www.python.org。

![image-20230917183649192](C:\Users\PJ_jackie\AppData\Roaming\Typora\typora-user-images\image-20230917183649192.png)

​	（2）下载安装包。

![image-20230919163418589](C:\Users\PJ_jackie\AppData\Roaming\Typora\typora-user-images\image-20230919163418589.png)

​	（3）安装Python解释器。

![image-20230919163526222](C:\Users\PJ_jackie\AppData\Roaming\Typora\typora-user-images\image-20230919163526222.png)

![image-20230919163536007](C:\Users\PJ_jackie\AppData\Roaming\Typora\typora-user-images\image-20230919163536007.png)

![image-20230919163552044](C:\Users\PJ_jackie\AppData\Roaming\Typora\typora-user-images\image-20230919163552044.png)

![image-20230919163608053](C:\Users\PJ_jackie\AppData\Roaming\Typora\typora-user-images\image-20230919163608053.png)

![image-20230919163615111](C:\Users\PJ_jackie\AppData\Roaming\Typora\typora-user-images\image-20230919163615111.png)

​	（4）验证安装是否成功。打开命令提示符，输入python -V。

![image-20230919163701926](C:\Users\PJ_jackie\AppData\Roaming\Typora\typora-user-images\image-20230919163701926.png)

 	2 ）配置Python环境变量

​	（1）在桌面上右击【我的电脑】选择【属性】，打开“设置”窗口，选择【高级系统设置】，打开“系统属性”对话框。 	 ![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps15.jpg) 

​	（2）点击【环境变量】按钮，进入到“环境变量”对话框。  

![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps16.jpg)

​	（3）找到“Path”环境变量并双击或点击下方的【新建】，打开“编辑环境变量”对话框。 

![image-20230919165221292](C:\Users\PJ_jackie\AppData\Roaming\Typora\typora-user-images\image-20230919165221292.png)

​	（4）配置后，利用Win10中的命令提示符，验证Python和pip环境变量的配置，操作如下：从键盘上按“win+R”，输入“cmd”调出命令行，输入命令“pip”，若有如下相关提示，说明环境变量配置成功。 

![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps17.jpg) 

​	3） 执行Python 

​	（1）交互模式执行Python。

​	在Windows操作系统中按“Win+R”快捷键打开“运行”；输入“cmd”后，点击“确定，打开“命令提示符”；在命令行模式输入“python”后回车，即可进入 Python 的交互模式。

![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps22.jpg)

​	进入Python环境下，在命令提示符“>>>”后输入代码后，按下回车键，即可逐行运行并打印运行结果；运行完成后可通过quit( )或exit( )函数退出交互模式。

![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps18.jpg)

​	（2）脚本运行方式 

​	使用Windows自带的文本编辑器“记事本”在D盘新建了一个文件“hello.py”，路径为“D:\hello.py”。该文件包含两行代码，第一行代码是计算1988和2098的乘积并将计算结果保存到变量 a 中，第二行代码是打印输出a的值。然后在终端中运行该脚本文件“hello.py”，可以看到准确地输出了1988×2098 的结果。

 ![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps20.jpg)

![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps19.jpg)

​	4) 下载、安装、配置PyCharm2021 

​	（1）访问PyCharm官网

​	 访问PyCharm官网，在PyCharm的下载页面中会出现Professional和Community两个版本，即专业版和社区版。

![image-20230919170131067](C:\Users\PJ_jackie\AppData\Roaming\Typora\typora-user-images\image-20230919170131067.png)

​	PyCharm专业版与PyCharm社区版的区别如下表。

| **区别项**               | **PyCharm专业版** | **PyCharm社区版** |
| ------------------------ | ----------------- | ----------------- |
| 智能Python编辑器         | √                 | √                 |
| 图形化调试器和测试运行器 | √                 | √                 |
| 导航和重构               | √                 | √                 |
| 代码检查                 | √                 | √                 |
| VCS支持                  | √                 | √                 |
| 科学工具                 | √                 |                   |
| Web开发                  | √                 |                   |
| PythonWeb框架            | √                 |                   |
| PythonProfiler           | √                 |                   |
| 远程开发功能             | √                 |                   |
| 数据库和SQL支持          | √                 |                   |

​	（2）下载PyCharm2021

 	点击Community下方的“Downloading”进行下载，选择另存为，存放到磁盘制定路径。 	

![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps26.jpg)

​	（3）安装PyCharm2021 

​	双击本地的PyCharm安装包“pycharm-community-2021.1.2.exe”，进入安装首页。

  ![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps30.jpg)

![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps29.jpg)

 ![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps34.jpg)

![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps33.jpg)

 ![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps38.jpg)

 

![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps37.jpg)

​	（4）首次运行并配置PyCharm2021

​	双击桌面上的“PyCharm”快捷方式，进入程序首页，勾选协议许可“I confirm that...”选项，点击“Continue”按钮，进入“Pycharm Community 2021”页面。

  

![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps41.jpg)![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps42.jpg)

![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps44.jpg) 

​	在“Customize”定制页，背景默认为“Darcula”即黑色经典样式，可以调整为“IntelliJ Light”即高亮样式；字体大小默认为12，可以根据实际情况调整为14或16或其他，其余设置选择默认。 

![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps47.jpg)

![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps46.jpg)

​	完成Python项目的创建。

 ![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps51.jpg)

![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps50.jpg)

​	（5）在PyCharm中运行“Hello World！”程序

​	在“Py_Demo”项目上点击右键选择“New”，输入“h”后双击“Python file”即可创建一个名字为“h.py”的python文件。

![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps56.jpg)

 ![img](file:///C:\Users\PJ_JAC~1\AppData\Local\Temp\ksohtml87280\wps54.jpg)

 	在代码区添加代码print('Hello World!')，然后点击右键选择“Run 'h'”,在运行结果区显示运行结果。

![image-20230919172849089](C:\Users\PJ_jackie\AppData\Roaming\Typora\typora-user-images\image-20230919172849089.png)
# Shape
# Shape the shape by my self 
# 介绍写网站的冲动
也就是自己来塑造自己的“形状”，也可以说未来，说的有点夸张，其实就是一个展现自己的网站吧，因为自己也是经历了实习和第一份工作，现在已经离职了，正在寻找新的机会，当然，在工作中也明白了点点滴滴都需要来积累，因此，希望能够自己完成一个小demo来展现一下自己。
# 用到的主要工具
目前使用的主要是flask框架以及其相关的一些插件

包括 flask-login flask-script flask-sqlalchemy具体的插件可以看我的requirement.txt

# 下载安装的步骤


1.本地新建项目
>git clone git@github.com:PythonScientists/Shape
>cd Shape
>virtualenv env


2.安装数据库以及依赖
>在config文件中修改数据库配置
>pip install -r requirements.txt


3.运行程序
>python manager.py server


4.额外介绍
我的程序是用gunicron+nginx+supervisro运行的
如果你们也想要这样部署的话，可以这么做
>在supervisor配置gunicorn
>在nginx.conf文件中转发端口


![系统结构图展示](https://github.com/PythonScientists/Shape/blob/master/other/photo/未命名文件.png)
![系统界面展示](https://github.com/PythonScientists/Shape/blob/master/other/photo/content.png)

   

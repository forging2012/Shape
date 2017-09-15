# Shape
# Shape the shape by my self 
## 介绍写网站的冲动
也就是自己来塑造自己的“形状”，也可以说未来，说的有点夸张，其实就是一个展现自己的网站吧，因为自己也是经历了实习和第一份工作，现在已经离职了，正在寻找新的机会，当然，在工作中也明白了点点滴滴都需要来积累，因此，希望能够自己完成一个小demo来展现一下自己。网站只写了几天，因此不足的地方希望大家原谅，如果有不足的地方在这里真心的希望大家随意“批评”，我看到一定马上更正。
## 目前用到的主要工具
目前使用的主要是flask框架以及其相关的一些插件

包括 flask-login flask-script flask-sqlalchemy具体的插件可以看我的requirement.txt


## 以后会新增使用的工具
1.会涉及爬虫，会用到reuqests来写相关的模块
2.会涉及语言的处理，会使用到之前使用过的pd,np结合jieba分词+nltk语言处理
3.会涉及分布式的任务，因此会部署上celery和rabbitmq(之前涉及过几千的任务并发处理的情形，因此有同样经历的大爷们可以一起讨论一下)
4.会涉及图表的展示，使用比较擅长的echart和matplotlib来处理

## 下载安装的步骤


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

## 需要注意的情况
本项目是基于python3.4的，因此可能对于python2的同学安装的时候会出现一些问题，不过可以先尽量使用python3安装，以后会加入适应python2的情况的


## 为了避免遇到问题时留言不及时，可以加我的微信


![微信](https://github.com/PythonScientists/Shape/blob/master/other/photo/person.jpg)


![系统结构图展示](https://github.com/PythonScientists/Shape/blob/master/other/photo/未命名文件.png)
![系统界面展示](https://github.com/PythonScientists/Shape/blob/master/other/photo/content.png)

   

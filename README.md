# learning_python

code_1.py

code_2.py

code_2_1.py

code_3.py 学习“操作文件与目录”部分完成的搜索作业，命令行中制定字符串搜索并显示包含目标的并且带有完整路径的文件名

code_4.py 学习“正则表达式”部分完成的作业，匹配合法的电子邮箱地址

base064.py 学习“base64”库完成的作业，编码时自动略去补全的'='，并在解码时能够自动填回来

BMP_judge.py 学习struct用法，完成的作业，编写函数分析文件头，判断是否为BMP文件并输出尺寸和颜色数。

login.py 学习md5摘要算法，完成作业：设计简单的登录认证系统，同时采用‘加盐’方式保护用户的口令信息
功能设计有：注册、登录、改密，其中用户名有合法性、存在性和重复性认证

big_multyply.py 学习大数运算，以模拟手工运算的方式执行大数乘法，可以去掉首位的0

divider.py 设计了一个用于求一个数全部约数的算法。该算法首先求出素数表，然后求出质因数，最后根据质因数合成全部素数

longest_common_sequence.py 学习了最大子串的分析模式。采用标记矩阵的形式，利用对角累加来迭代之前的比较结果。设置了最大串长和最大子串标记来取串。[原博客](http://codepub.cn/2015/07/03/Python-implementation-of-the-longest-common-subsequences/)有讲解最大子序列（非连续），仅作了解，未自主实现。

rename.py 自己写的小脚本，批量修改了没有规范格式的MID文件。其中汇报了WindowsError Error:3的错误。本以为是路径不存在，还反复用os.getcwd(),os.path.exists(-)调试。后来注意到文件名中不允许非法字符：'?','\','*'等。

qiushibaike.py 调用urllib，urllib2库尝试爬虫抓包。程序对糗事百科的内容进行了抓取，呈现内容有文字和图片两种方式。地址抽取采用随机抓取的方式，未完全捕获，未设置查重。matplotlib.pyplot库的使用有待加强。

import os
from tkinter import *
from scrapy import cmdline

def startSpider():
    # 开始爬虫程序
    cmdline.execute('scrapy crawl bqh2'.split())

# 创建窗口
root = Tk()
# 窗口大小
root.geometry('535x305+200+200')
# 标题
root.title('点击开始获取小电影资源')
# 点击按钮
Button(root, text="开始查询", font=('微软雅黑', 20), command=startSpider).grid(row=1)
# 显示窗口
root.mainloop()





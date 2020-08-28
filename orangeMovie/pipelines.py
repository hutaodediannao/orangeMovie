# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from typing import List, Any

from redis import *
from tkinter import Tk, LEFT, BOTH
from tkinter import ttk


class OrangemoviePipeline(object):
    list: List[Any]

    def open_spider(self, spider):
        self.list = []
        self.fp = open('./movies.txt', mode='a', encoding='utf-8')
        pass

    def close_spider(self, spider):
        self.fp.close()
        self.drowUIDeskTop()
        pass

    def process_item(self, item, spider):
        self.fp.write(
            f'[title:{item["title"]}, img:{item["imgSrc"]}, href:{item["href"]}, downloadUrl:{item["downloadUrl"]}]\n')

        # 写入redis数据库持久化
        # redis = StrictRedis(host='127.0.0.1', port=6379, db=0)  # 连接redis数据库
        # redis.rpush('title', item['title'])
        # redis.rpush('downloadUrl', item['downloadUrl'])

        self.list.append(item)
        return item

    # 绘制GUI
    def drowUIDeskTop(self):
        print('=============================================>', '爬虫爬取完成了')
        root = Tk()  # 初始框的声明
        root.geometry('1000x700+100+50')
        root.title('宅男神器，你懂的')
        columns = ("序号", "片名", "迅雷下载地址")
        treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)  # 表格

        treeview.column("序号", width=100)  # 表示列,不显示
        treeview.column("片名", width=400)  # 表示列,不显示
        treeview.column("迅雷下载地址", width=800)

        treeview.heading("序号", text="序号")  # 显示表头
        treeview.heading("片名", text="片名")  # 显示表头
        
        treeview.heading("迅雷下载地址", text="迅雷下载地址")
        treeview.pack(side=LEFT, fill=BOTH)

        for (index, item) in enumerate(self.list):  # 写入数据
            treeview.insert('', index, values=(f'{index + 1}', item['title'], item['downloadUrl']))
        root.mainloop()
        pass

    def sign(self, downloadUrl):
        print('downloadUrl====================>', downloadUrl)
        pass

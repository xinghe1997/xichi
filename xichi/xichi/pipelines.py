# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class XichiPipeline(object):
   # def __init__(self):
        #self.file = open('ip.json','wb')
    def process_item(self,item,spider):
        #line = json.dumps(dict(itme))+"\n"
        #self.file.write(line.encode('utf-8'))
        return item

# -*- coding: utf-8 -*-
import scrapy
import json
import requests
class DailiSpider(scrapy.Spider):
    name = 'daili'
    allowed_domains = ['https://www.xicidaili.com']
    start_urls = ['https://www.xicidaili.com/wt/']

    def parse(self, response):
        item = []
       #保存路径
        f = open('ip.json','wb')
        #测试proxy链接
        test_url ="http://xabc.io/p"
        #提取所有tr
        trs = response.xpath("//tr[position() > 1]")
        #遍历
        for tr in trs:
            #定义一个变量来保存本次ip
            ip = tr.xpath("td[2]/text()").get()
            proxy = {'http' : 'http://'+ip+':'+tr.xpath("td[3]/text()").get()};
            #捕获
            try:
                #0.5秒内无回应，或失败都舍弃
                test = requests.get(test_url, proxies=proxy, timeout=0.5)
                #判断状态码，等于200就保存
                if test.status_code == 200:  
                    #添加进数组
                    item.append(proxy)
            except:
                #测试proxy捕获到错误时跳过本次循环
                continue  
        line = json.dumps(item)
        #保存文件，编码utf-8
        f.write(line.encode('utf-8'))
       
        
        
           
               
            
      

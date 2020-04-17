# -*- coding: utf-8 -*-
import scrapy
import json

class DailiSpider(scrapy.Spider):
    name = 'daili'
    allowed_domains = ['https://www.xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nt']

    def parse(self, response):
        item = []
        trs = response.xpath("//tr[@class='odd']")
        for tr in trs:
            item.append({'ip':tr.xpath("td[2]/text()").get(),'post':tr.xpath("td[3]/text()").get()})
        self.file = open('ip.json','wb')
        line = json.dumps(item)+"\n";
        self.file.write(line.encode('utf-8'))
        
      

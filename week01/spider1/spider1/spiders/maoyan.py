# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from spider1.items import Spider1Item
from scrapy.selector import Selector

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']
                  
    def start_requests(self):
        for i in range(0,10):
            url = f'https://maoyan.com/films?showType=3&offset={i*30}'
            yield scrapy.Request(url = url,callback=self.parse,dont_filter=False)
    
    # print("---------------")

    def parse(self,response):
        print(response.url)
        print(response.text)
        for each in response.xpath('//div[@class="movie-hover-title"]'):
            item = Spider1Item()
            print(each)
            title = each.xpath('./a/span/[@class="name"]/text()')
            category = each.xpath('./a/span/[@class="hover-tag"]')
            date = each.xpath('./a/@href')

            item['title'] = title.encode('utf-8')
            item['category'] = category.encode('utf-8')
            item['date'] = date.encode('utf-8')
            print('-------------------')
            print(item)

            yield item
       
       
       


        

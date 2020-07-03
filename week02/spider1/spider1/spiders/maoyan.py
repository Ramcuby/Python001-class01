# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from spider1.items import Spider1Item
from scrapy.selector import Selector

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']
                  
    # def start_requests(self):
    #     for i in range(0,10):
    #         url = f'https://maoyan.com/films?showType=3&offset={i*30}'
    #         yield scrapy.Request(url = url,callback=self.parse,dont_filter=False)
    
    # print("---------------")

    def parse(self,response):
        items = []
        # print(response.body.decode())
        # print(response.text)
        i=0
        top=10
        for each in response.xpath('//div[@class="movie-hover-info"]'):
            if(i<top):
                item = Spider1Item()
                # print(each)
                title = each.xpath('div[2]/@title').extract_first().strip()
                category = each.xpath('div[2]/text()[2]').extract_first().strip()
                date = each.xpath('div[4]/text()[2]').extract_first().strip()

                item['title'] = title #.encode('utf-8')
                item['category'] = category #.encode('utf-8')
                item['date'] = date #.encode('utf-8')
                print('-------------------')
                
                items.append(item)
                # print(item)
                i+=1
            else:
                break
            yield item
            

        # return items
       
       
       


        

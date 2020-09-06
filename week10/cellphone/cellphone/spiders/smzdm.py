# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from snownlp import SnowNLP
from cellphone.items import CellphoneItem
from scrapy.selector import Selector

class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']
    start_urls = ['http://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']

    # def parse(self, response):
        # pass
    def start_request(self):
        for i in range(1,2):
            url = f'https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p{i}/#feed-main/'
            yield scrapy.Request(url = url, callback = self.parse, dont_filter=True)
    
    def parse(self, response):
        item = CellphoneItem()
        link = Selector(response=response).xpath('//ul[@id="feed-main-list"]/li/div/div[1]/a/@href').extract()
        for i in range(0,len(link)):
            yield scrapy.Request(url=link[i], meta={'item': item}, callback=self.parse2, dont_filter=True)
    
    def parse2(self, response):
        item = response.meta['item']
        link = Selector(response=response).xpath('//div[@id="commentTabBlockNew"]/ul[2]/li/a/@href').extract()
        if len(link) == 0:
            dates = Selector(response=response).xpath('//li[@class="comment_list"]/div[2]/div[1]/div[1]/meta/@content').extract()
            for i in range(1,len(dates)+1):
                date = Selector(response=response).xpath(f'//li[@class="comment_list"][{i}]/div[2]/div[1]/div[1]/meta/@content').extract_first()
                if len(date) == 0:continue
                estimates = pd.Series(Selector(response=response).xpath('//span[@itemprop="description"]/text()').extract())
                def _sentiment(text):
                    return SnowNLP(text).sentiments
                for j in range(0,len(estimates)):
                    estimate = estimates[j].strip()
                    if len(estimate) == 0:continue
                    sentiment = _sentiment(estimate)
                    if sentiment < 0.4:continue
                    n_star = sentiment // 0.2 + 1
                    item['date'] = date
                    item['n_star'] = n_star
                    item['estimate'] = estimate
                    item['sentiment'] = sentiment
                    yield item
        else:
            for i in range(0,len(link)-2):
                yield scrapy.Request(url =link[i], meta={'item':item}, callback = self.parse3, dont_filter=True)
                
    def parse3(self, response):
        item = response.meta['item']
        dates = Selector(response=response).xpath('//li[@class="comment_list"]/div[2]/div[1]/div[1]/meta/@content').extract()
        for i in range(1,len(dates)+1):
            date = Selector(response=response).xpath(f'//li[@class="comment_list"][{i}]/div[2]/div[1]/div[1]/meta/@content').extract_first()
            if len(date) == 0:continue
            estimates = pd.Series(Selector(response=response).xpath('//span[@itemprop="description"]/text()').extract())
            def _sentiment(text):
                return SnowNLP(text).sentiments
            for j in range(0,len(estimates)):
                estimate = estimates[j].strip()
                if len(estimate) == 0:continue
                sentiment = _sentiment(estimate)
                if sentiment < 0.4:continue
                n_star = sentiment // 0.2 + 1
                item['date'] = date
                item['n_star'] = n_star
                item['estimate'] = estimate
                item['sentiment'] = sentiment
                yield item
            

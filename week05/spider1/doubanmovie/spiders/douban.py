# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from doubanmovie.items import DoubanmovieItem


class DoubanSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    # 起始URL列表
    start_urls = ['https://movie.douban.com/subject']

#   注释默认的parse函数
#   def parse(self, response):
#        pass


    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    # https://movie.douban.com/subject/26871465/comments?start=0&limit=20&sort=new_score&status=P
    # https://movie.douban.com/subject/26871465/comments?start=20&limit=20&sort=new_score&status=P

    def start_requests(self):
        for i in range(0, 2):
            # url = f'https://movie.douban.com/top250?start={i*25}'
            url = f'https://movie.douban.com/subject/26871465/comments?start={i*20}&limit=20&sort=new_score&status=P'
            yield scrapy.Request(url=url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        items = []
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title_list = soup.find_all('div', attrs={'class': 'comment'})
        
        for i in range(len(title_list)):
            # 在items.py定义
            item = DoubanmovieItem()
            # author = title_list[i].find('a').find('href')
            comments = title_list[i].find('span', attrs={'class': 'short'}).text
            
            comments_dict = dict(很差=1,较差=2,还行=3,推荐=4,力荐=5)
            
            t1 = title_list[i].find('span',attrs={'class':'comment-info'}).find_all('span')
            star = t1[1]['title']
            
            t2 = title_list[i].find('span',attrs={'class':'comment-info'}).find('a')
            author = t2.text
            
            item['author'] = author
            item['comments'] = comments
            item['star'] = comments_dict[star]
            items.append(item)
        return items

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd 

class Spider1Pipeline:
    def process_item(self, item, spider):
        title=item['title'],
        category=item['category'],
        date=item['date']

        mylist = {'title':[],'category':[],'date':[]}
        mylist['title'].append(list(title))
        mylist['category'].append(list(category))
        mylist['date'].append(date)
        # mylist = [title, category, date]
        movie1 = pd.DataFrame(data = mylist,columns=['title','category','date'])
        # print("hello----------------------")
        # print(mylist)
        movie1.to_csv('movie1_1.csv',mode='a+',encoding='utf8', index=False, header=False)
        # with open('maoyan_movie_top100.csv', 'a+', encoding='utf-8') as file:
        #     line = "{title},{category},{date}\n".format(
        #         title=item['title'],
        #         category=item['category'],
        #         date=item['date'])
        #     file.write(line)
        return item

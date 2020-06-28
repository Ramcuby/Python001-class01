# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Spider1Pipeline:
    def process_item(self, item, spider):
        with open('maoyan_movie_top10.csv', 'a+', encoding='utf-8') as file:
            line = "{title},{category},{date}\n".format(
                title=item['title'],
                category=item['category'],
                date=item['date'])
            file.write(line)
        return item

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd 
import pymysql

class DoubanmoviePipeline:
    def process_item(self, item, spider):
        author = item['author']
        comments = item['comments']
        star = item['star']

        mylist = {'author':[],'comments':[],'star':[]}
        mylist['author'].append(author)
        mylist['comments'].append(comments)
        mylist['star'].append(star)
        print('--'*40)
        print(mylist)
        print('--'*40)

        conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = 'admin',
                       database = 'movies',
                       charset = 'utf8mb4'
                        )

        # 获得cursor游标对象
        con1 = conn.cursor()

        # 操作的行数
        count = con1.execute('select * from douban1;')
        # print(f'查询到 {count} 条记录')

        # 获得一条查询结果
        result = con1.fetchone()
        # print(result)

        # 获得所有查询结果
        # print(con1.fetchall())
        con1.close()
        
        table = 'douban1'
        keys = ', '.join(mylist.keys())
        values = ', '.join(['%s'] * len(mylist))

        con2 = conn.cursor()
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
        
        # con2.execute(sql, tuple(mylist.values()))
        # conn.commit()

        try:
            if con2.execute(sql, tuple(mylist.values())):
                print('Successful')
                conn.commit()
        except:
            print('Failed')
            conn.rollback()
            
        con2.close()
        conn.close()

        return item

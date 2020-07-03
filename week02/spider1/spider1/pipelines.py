# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd 
import pymysql

class Spider1Pipeline:
    def process_item(self, item, spider):
        title=item['title'],
        category=item['category'],
        date=item['date']

        mylist = {'title':[],'category':[],'date':[]}
        mylist['title'].append(list(title))
        mylist['category'].append(list(category))
        mylist['date'].append(date)

        # movie1 = pd.DataFrame(data = mylist,columns=['title','category','date'])
        # movie1.to_csv('movie1_1.csv',mode='a+',encoding='utf8', index=False, header=False)
        # with open('maoyan_movie_top100.csv', 'a+', encoding='utf-8') as file:
        #     line = "{title},{category},{date}\n".format(
        #         title=item['title'],
        #         category=item['category'],
        #         date=item['date'])
        #     file.write(line)
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
        count = con1.execute('select * from maoyan;')
        print(f'查询到 {count} 条记录')


        # 获得一条查询结果
        result = con1.fetchone()
        print(result)

        # 获得所有查询结果
        print(con1.fetchall())
        con1.close()
        
        table = 'maoyan'
        keys = ', '.join(mylist.keys())
        values = ', '.join(['%s'] * len(mylist))

        con2 = conn.cursor()
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)

        try:
            if con2.execute(sql, tuple(mylist.values())):
                print('Successful')
                conn.commit()
        except:
            print('Failed')
            conn.rollback()
        con2.close()
        conn.close()

        # con1.close()
        # conn.close()

        # 执行批量插入
        # values = [(id,'testuser'+str(id)) for id in range(4, 21) ]
        # cursor.executemany('INSERT INTO '+ TABLE_NAME +' values(%s,%s)' ,values)

        
        return item




# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class CellphonePipeline:
    def process_item(self, item, spider):
        conn = pymysql.connect(host = 'localhost',
                        port = 3306,
                        user = 'root',
                        password = 'admin',
                        database = 'monitor',
                        charset = 'utf8mb4'
                        )
        
        sql = 'DROP TABLE cellphone;'
        sql1 = ''' CREATE TABLE IF NOT EXISTS `cellphone`(
                `id` INT UNSIGNED AUTO_INCREMENT,
                `date` varchar(30) not null,
                `n_star` int(5) not null,
                `estimate` varchar(200) NOT NULL,
                `sentiment` decimal(11,10) not null,
                PRIMARY KEY ( `id` )
                )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;'''
        sql2 = "INSERT INTO `cellphone`(`date`, `n_star`, `estimate`, `sentiment`) VALUES ('{date}','{n_star}', '{estimate}', '{sentiment}')".format(date=item['date'], n_star=item['n_star'], estimate=item['estimate'], sentiment=item['sentiment']);
        
        try:
            # 获得cursor游标对象
            con1 = conn.cursor()
            con1.execute(sql)
            con1.execute(sql1)
            con1.execute(sql2)
            conn.commit()
        except Exception as e:
            print(sql1)
            print(e,'操作失败!===========================')
        con1.close()
        conn.close()
        return item

import pymysql
import pandas as pd
from pandasql import sqldf

sql  =  ['SELECT * FROM data;',
        'SELECT * FROM data LIMIT 10;',
        'SELECT id FROM data;  //id 是 data 表的特定一列',
        'SELECT COUNT(id) FROM data;',
        'SELECT * FROM data WHERE id<1000 AND age>30;',
        'SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;',
        'SELECT * FROM table1 t1 INNER_JOIN table2 t2 ON t1.id = t2.id;',
        'SELECT * FROM table1 UNION SELECT * FROM table2;',
        'DELETE FROM table1 WHERE id=10;',
        'ALTER TABLE table1 DROP COLUMN column_name;'
        ]


conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = 'admin',
                       database = 'pandas',
                       charset = 'utf8mb4'
                        )

# 获得cursor游标对象
con1 = conn.cursor()

# df = pd.read_sql(sql[1],con=conn)
# print(df)

df_data=pd.read_sql('select * from data',con=conn)
df_table1=pd.read_sql('select * from table1',con=conn)
df_table2=pd.read_sql('select * from table2',con=conn)
# print(df_data)
# print(df_table1)
# print(df_table2)

print("SQL 1:"+sql[0])
print(df_data)

print("SQL 2:"+sql[1])
print(df.head(10))

print("SQL 3:"+sql[2])
print(df_data['id'])

print("SQL 4:"+sql[3])
print(df_data['id'].count())

print("SQL 5:"+sql[4])
df5=df_data[(df_data['id']<1000) & (df_data['age']>30)]
print(df5)

print("SQL 6:"+sql[5])
df6=df_table1.groupby('id')['order_id'].nunique()
print(df6)

print("SQL 7:"+sql[6])
df7=pd.merge(df_table1,df_table2,on='id')
print(df7)

print("SQL 8:"+sql[7])
df8=pd.concat([df_table1,df_table2]).drop_duplicates()
print(df8)

print("SQL 9:"+sql[8])
df_table1=df_table1.loc[df_table1['id']!=10]
print(df_table1)

print("SQL 10:"+sql[9])
df_table1=df_table1.drop(['column_name'],axis=1)
print(df_table1)

con1.close()
conn.close()
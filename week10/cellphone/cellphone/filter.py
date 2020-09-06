import pymysql
import pandas as pd
conn = pymysql.connect(host = 'localhost',
                        port = 3306,
                        user = 'root',
                        password = 'admin',
                        database = 'monitor',
                        charset = 'utf8mb4'
                        )
sql = 'SELECT * FROM cellphone;'
df = pd.read_sql(sql,conn)
df.dropna()
print(df.isnull().sum())
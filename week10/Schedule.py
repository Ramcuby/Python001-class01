from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os

# 输出时间
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))    
    os.system('cd /Users/zhl/Python001-class01/week10/cellphone && scrapy crawl smzdm')

# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week='0-6', hour=08, minute=12)   #每天08：12运行一次爬虫
scheduler.start()
import csv

import pandas as pd
from pymongo import MongoClient
import json

username = "root"
password = "123456"
client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))
# client = MongoClient("root:123456@localhost",27017)
db = client ["liveshare"]
collection = db ["lotto"]

csvfile = '/Users/jarvis/Downloads/2014/4星彩_2014.csv'
# df = pd.read_csv('/Users/jarvis/Downloads/2014/4星彩_2014.csv')
# data = df.to_dict('records')
# reviews_df = pd.read_csv(csvfile, )

# print(reviews_df)

usecols = ['遊戲名稱','期別','開獎日期','銷售總額','銷售注數','總獎金','獎號1','獎號2','獎號3']
df= pd.read_csv(csvfile, usecols=usecols)
# df = df.dropna(axis=1)
print(df.head())
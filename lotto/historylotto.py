import pandas as pd
from pymongo import MongoClient
import json
import glob

totalYears = ["2014","2015","2016","2017","2018","2019","2020","2021"]

def read_csv(csvfile,yearForData):  
    client = MongoClient("localhost",27017)
    db = client["lotto"]
    collection_name = "history"+yearForData
    collection = db[collection_name] 
    data = pd.read_csv(csvfile,index_col=False,encoding = "utf-8") #原資料index是三星彩,index_col=False =>重新配置一個index
    newdata = data.loc[:,~data.columns.str.contains("^Unnamed")]
    #出現unnamed是因為在存入csv時把索引一起存入,可用此種方式強制移除
    #避免出現此問題,在寫入csv時,index=False
    cleandata =newdata.dropna(axis = 1 ,how = "all") #刪除四星彩多一列空值

    data_json = json.loads(cleandata.to_json(orient="records")) #寫出以行分隔的json格式
    collection.insert(data_json)

for thisyear in totalYears:
    filePath = glob.glob(f"/Users/jarvis/Documents/python3/liveshare/data/{thisyear}/*.csv") #glob查找特定副檔名檔案 /*副檔名
    for file in filePath:
        read_csv(file,thisyear)



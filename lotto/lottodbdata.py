from bs4 import BeautifulSoup
from numpy import sort
import requests
from pymongo import MongoClient
# from django.conf import settings
import sys
sys.path.append("..")
from liveshare.settings import setDBconnect

dbclient = setDBconnect()
db = dbclient["lotto"]
collection = db['lotto']

#BINGO
def getbingo():
    result = collection.find_one({'遊戲名稱': 'BINGO'},sort=[( '_id', -1 )])
    return result

#雙贏彩
def getdoublewin():
    result = collection.find_one({'遊戲名稱': '雙贏彩'},sort=[( '_id', -1 )])
    return result

#抓取威力彩
def getpowerlotto():
    result = collection.find_one({'遊戲名稱': '威力彩'},sort=[( '_id', -1 )])
    return result

#抓取38樂合彩
def get38():
    result = collection.find_one({'遊戲名稱': '38樂合彩'},sort=[( '_id', -1 )])
    return result

#抓取大樂透
def getbiglotto():
    result = collection.find_one({'遊戲名稱': '大樂透'},sort=[( '_id', -1 )])
    return result

#抓取49樂台彩
def get49():
    result = collection.find_one({'遊戲名稱': '49樂台彩'},sort=[( '_id', -1 )])
    return result

#抓取今彩539
def get539():
    result = collection.find_one({'遊戲名稱': '今彩539'},sort=[( '_id', -1 )])
    return result

#抓取39樂合彩
def get39():
    result = collection.find_one({'遊戲名稱': '39樂合彩'},sort=[( '_id', -1 )])
    return result

#抓取3星彩
def get3star():
    result = collection.find_one({'遊戲名稱': '3星彩'},sort=[( '_id', -1 )])
    return result

#抓取4星彩
def get4star():
    result = collection.find_one({'遊戲名稱': '4星彩'},sort=[( '_id', -1 )])
    return result

if __name__ == '__main__' :
    print(getbingo())
    print(getdoublewin())
    print(getpowerlotto())
    print(get38())
    print(getbiglotto())
    print(get49())
    print(get539())
    print(get39())
    print(get3star())
    print(get4star())


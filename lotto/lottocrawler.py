import pymongo
from bs4 import BeautifulSoup
from numpy import sort
import requests
from pymongo import MongoClient
import urllib.parse
import sys
sys.path.append("..")
from liveshare.settings import setDBconnect

# username = urllib.parse.quote_plus('jarvis')
# password = urllib.parse.quote_plus("#5X7@@7hi6TYnCe")
# server = "mongodb+srv://{}:{}@cluster0.jry7x.mongodb.net/myFirstDatabase?retryWrites=true".format(username, password)
# cluster = MongoClient(server)
# db = cluster['lotto']
# collection = db['lotto']

# client = MongoClient("localhost",27017)


url = "https://www.taiwanlottery.com.tw/index_new.aspx"
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
sourcedata = soup.find('div',id='rightdown')
lottonames =  "大樂透", "威力彩", "今彩539", "雙贏彩", "BINGO BINGO賓果賓果", "3星彩", "4星彩", "38樂合彩", "49樂合彩", "39樂合彩"
lottodata = {
    '大樂透': 'getbiglotto', 
    '威力彩': 'getpowerlotto',
    '今彩539': 'get539',
    '雙贏彩': 'getdoublewin',
    'BINGO': 'getbingo',
    '3星彩': 'get3star',
    '4星彩': 'get4star',
    '38樂合彩': 'get38',
    '49樂合彩': 'get49',
    '39樂合彩': 'get39'
}
url2 = "https://www.taiwanlottery.com.tw/result_all.htm"
html2 = requests.get(url2)
soup2 = BeautifulSoup(html2.text, 'html.parser')
sourcedata2 = soup2.find('div',id='right_full')
tableDetail = sourcedata2.find_all('table',{'class', 'tableyun'})

#Bingo
def getbingo():
    data = sourcedata.select('div.contents_box01')
    perid = data[0].find('span' , 'font_black15').text
    perid = perid.split()
    opendate,openserial = perid[0] , perid[1]
    ballred = data[0].find('div' , 'ball_red').text
    bigOrSmall = data[0].find('div' , 'ball_blue_BB1').text
    singleOrDouble = data[0].find('div' , 'ball_blue_BB2').text
    numbers = data[0].find_all('div' , 'ball_tx ball_yellow')
    numberlist = ([int(i.text.rstrip(" ")) for i in numbers])
    result = {'遊戲名稱':'BINGO', '開獎日期': opendate , '期別': openserial , '開出獎號': numberlist , '超級獎號': ballred , "猜大小": bigOrSmall , "猜單雙": singleOrDouble }
    return result

#爽贏彩
def getdoublewin():
    data = sourcedata.select('div.contents_box06')
    perid = data[0].find('span' , 'font_black15').text
    perid = perid.split()
    opendate,openserial = perid[0] , perid[1]
    numbers = data[0].find_all('div' , 'ball_tx ball_blue')
    numberlist = [int(i.text.rstrip(" ")) for i in numbers]
    numberlist = (numberlist[:12])
    result = {'遊戲名稱':'雙贏彩', '開獎日期': opendate , '期別': openserial , '開出獎號': numberlist}
    return result

#抓取威力彩
def getpowerlotto():
    data = sourcedata.find_all('div' , 'contents_box02')
    perid = data[0].find('span' , 'font_black15').text
    perid = perid.split()
    opendate,openserial = perid[0] , perid[1]
    numbers = data[0].find_all('div' , 'ball_tx ball_green')
    firstnumbers = [int(i.text.rstrip(" ")) for i in numbers ]
    firstnumbers = (firstnumbers[:6])
    sp_num = data[0].find_all('div' , 'ball_red')
    sp_num = int(sp_num[0].text.rstrip(" "))
    totalbonus = tableDetail[0].find('span', id ='SL638Total_new').text
    totalSoldAmount = tableDetail[0].find('span', id ='SL638labTotal_new').text
    totalOrder = (int(totalSoldAmount.replace(",","")) // 100)
    result = {'遊戲名稱':'威力彩', '開獎日期': opendate , '期別': openserial , "開出獎號" : firstnumbers , "第二區" : sp_num  }
    return result

#抓取38樂合彩
def get38():
    data = sourcedata.find_all('div' , 'contents_box02')
    perid = data[0].find('span' , 'font_black15').text
    perid = perid.split()
    opendate,openserial = perid[0] , perid[1]
    numbers = data[1].find_all('div' , 'ball_tx ball_green')
    firstnumbers = [int(i.text.rstrip(" ")) for i in numbers]
    firstnumbers = (firstnumbers[:6])
    result = {'遊戲名稱':'38樂合彩', '開獎日期': opendate , '期別': openserial , "開出獎號" : firstnumbers }
    return result

#抓取大樂透
def getbiglotto():
    data = sourcedata.find_all('div' , 'contents_box02')
    perid = data[0].find('span' , 'font_black15').text
    perid = perid.split()
    opendate,openserial = perid[0] , perid[1]
    numbers = data[2].find_all('div' , 'ball_tx ball_yellow')
    firstnumbers = [int(i.text.rstrip(" ")) for i in numbers]
    firstnumbers = (firstnumbers[:6])
    sp_num = data[2].find_all('div' , 'ball_red')
    sp_num = int(sp_num[0].text.rstrip(" "))
    result = {'遊戲名稱':'大樂透', '開獎日期': opendate , '期別': openserial , '開出獎號' : firstnumbers, '特別號': sp_num}
    return result

#抓取49樂台彩
def get49():
    data = sourcedata.find_all('div' , 'contents_box02')
    perid = data[0].find('span' , 'font_black15').text
    perid = perid.split()
    opendate,openserial = perid[0] , perid[1]
    numbers = data[3].find_all('div' , 'ball_tx ball_yellow')
    firstnumbers = [int(i.text.rstrip(" ")) for i in numbers]
    firstnumbers = (firstnumbers[:6])
    result = {'遊戲名稱':'49樂台彩', '開獎日期': opendate , '期別': openserial , '開出獎號' : firstnumbers }  
    return result

#抓取今彩539
def get539():
    data = sourcedata.find_all('div' , 'contents_box03')
    perid = data[0].find('span' , 'font_black15').text
    perid = perid.split()
    opendate,openserial = perid[0] , perid[1]
    numbers = data[0].find_all('div' , 'ball_tx ball_lemon')
    firstnumbers = [int(i.text.rstrip(" ")) for i in numbers]
    firstnumbers = (firstnumbers[:5])
    result = {'遊戲名稱':'今彩539', '開獎日期': opendate , '期別': openserial , '開出獎號' : firstnumbers }  
    return result

#抓取39樂合彩
def get39():
    data = sourcedata.find_all('div' , 'contents_box03')
    perid = data[0].find('span' , 'font_black15').text
    perid = perid.split()
    opendate,openserial = perid[0] , perid[1]
    numbers = data[1].find_all('div' , 'ball_tx ball_lemon')
    firstnumbers = [int(i.text.rstrip(" ")) for i in numbers]
    firstnumbers = (firstnumbers[:5])
    result = {'遊戲名稱':'39樂合彩', '開獎日期': opendate , '期別': openserial , '開出獎號' : firstnumbers }  
    return result

#抓取3星彩
def get3star():
    data = sourcedata.find_all('div' , 'contents_box04')
    perid = data[0].find('span' , 'font_black15').text
    perid = perid.split()
    opendate,openserial = perid[0] , perid[1]
    numbers = data[0].find_all('div' , 'ball_tx ball_purple')
    firstnumbers = [int(i.text.rstrip(" ")) for i in numbers]
    result = {'遊戲名稱':'3星彩', '開獎日期': opendate , '期別': openserial , '開出獎號' : firstnumbers }  
    return result

#抓取4星彩
def get4star():
    data = sourcedata.find_all('div' , 'contents_box04')
    perid = data[0].find('span' , 'font_black15').text
    perid = perid.split()
    opendate,openserial = perid[0] , perid[1]
    numbers = data[1].find_all('div' , 'ball_tx ball_purple')
    firstnumbers = [int(i.text.rstrip(" ")) for i in numbers]
    result = {'遊戲名稱':'4星彩', '開獎日期': opendate , '期別': openserial , '開出獎號' : firstnumbers }  
    return result

def updateDB(values):
    dbclient = setDBconnect()
    db = dbclient["lotto"]
    collection = db['lotto'] 
    collection.update_one(values,{'$setOnInsert':values},upsert=True)

if __name__ == '__main__' :
    print("台彩爬蟲程式")
    funclist = ["getbingo()", "getdoublewin()", "getpowerlotto()", 'get38()', \
        'getbiglotto()', 'get49()', 'get539()', 'get39()', 'get3star()', 'get4star()']
    for fun in funclist:
        result = eval(fun)
        updateDB(result)
    # print(funclist)
    # print(getbingo())
    # print(getdoublewin())
    # res = (getpowerlotto())
    # updateDB(res)
    # print(get38())
    # print(getbiglotto())
    # print(get49())
    # print(get539())
    # print(get39())
    # print(get3star())
    # print(get4star())


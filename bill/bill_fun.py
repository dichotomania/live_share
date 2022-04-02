from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage ,TextMessage ,PostbackEvent
from django.conf import settings
import requests

#line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

try:
    import xml.etree.cElementTree as ET #c語言開發較快
except ImportError:
    import xml.etree.ElementPath as ET
 
def current(event): #當期中獎  
    try:
        content = requests.get("https://invoice.etax.nat.gov.tw/invoice.xml")
        tree = ET.fromstring(content.text) # fromstring =>string轉為xml,節點從rss開始
        items = list(tree.iter( "item")) 
        #tree.iter() 遞迴查詢所有子結點
        #tree.findall() tree.find() 從節點中的直接子結點查詢,不會遞迴查詢
        title = items[0][0].text #當期期別
        number = (items[0][3].text).replace("</p>","\n").replace("<p>","") #當期獎號
        message = title + "\n" + number[:-1] #[:-1]為去除number最後一行空格
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))

    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="讀取發票號碼發生錯誤"))


#顯示前兩期中獎號碼
def oldData(event):#前期中獎
    try:
        content = requests.get("https://invoice.etax.nat.gov.tw/invoice.xml")
        tree = ET.fromstring(content.text)
        items = list(tree.iter( "item")) 
        message = ""
        for i in range(1,3): #抓前兩期就好,太舊的過了領獎期限
            title = items[i][0].text
            number = (items[i][3].text).replace("</p>","\n").replace("<p>","")
            message = message + title + "\n" + number +"=============="+"\n"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="讀取發票號碼發生錯誤"))
        
        
#末三碼對獎
def show3number(event,mtext):  
    try:  
        content = requests.get("https://invoice.etax.nat.gov.tw/invoice.xml")
        tree = ET.fromstring(content.text)
        items = list(tree.iter( "item")) 
        number = (items[0][3].text).replace("</p>","").replace("<p>","：").replace("、","：")
        numberlist = number.split("：")
        speciallist =[] #特別獎,頭獎末三碼list,有符合在進行接下來判斷
        speciallist.append(numberlist[2][5:8]) #特別獎末三碼
        speciallist.append(numberlist[4][5:8]) #特獎末三碼
        firstlist = [] #頭獎末三碼
        firstlist.append(numberlist[6][5:8])
        firstlist.append(numberlist[7][5:8])
        firstlist.append(numberlist[8][5:8])
        addnumber = numberlist[10] #增開六獎
        
        if mtext in speciallist:
            message = "符合特別獎或特獎末三碼,請繼續輸入前五碼"
        elif mtext in firstlist:
            message = "符合頭獎末三碼,至少中六獎！請繼續輸入前五碼"
        elif mtext in addnumber:
            message = "恭喜！！中了六獎 兩百元"
        else:
            message = "未中獎,再接再厲"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="讀取發票號碼發生錯誤"))


 #特別、特、頭獎前五碼
 def show5number(event,mtext):
    try:
        content = requests.get("https://invoice.etax.nat.gov.tw/invoice.xml")
        tree = ET.fromstring(content.text)
        items = list(tree.iter( "item"))
        number = (items[0][3].text).replace("</p>","").replace("<p>","：").replace("、","：")
        numberlist = number.split("：")
        special1 = numberlist[2][:5] #特別獎前五碼
        special2 = numberlist[4][:5] #特獎前五碼
        headlist = [] #頭獎全碼
        headlist.append(numberlist[6])
        headlist.append(numberlist[7])
        headlist.append(numberlist[8])

        if mtext == special1:
            message = "恭喜！！中了特別獎 一千萬元"
        elif mtext == special2:
            message = "恭喜！！中了特獎 二百萬元"
        elif True:
            for i in range(3):
                winnumber = headlist[i]
            if mtext == winnumber:
                message = "恭喜！！中了頭獎 二十萬元"
            elif mtext[1:5] == winnumber[1:5]:
                message = "恭喜！！中了二獎 四萬元"
            elif mtext[2:5] == winnumber[2:5]:
                message = "恭喜！！中了三獎 一萬元"
            elif mtext[3:5] == winnumber[3:5]:
                message = "恭喜！！中了四獎 四千元"
            elif mtext[4] == winnumber[4]:
                message = "恭喜！！中了五獎 一千元"
            else:
                message = "恭喜！！中了六獎 二百元"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))        
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發票號碼發生錯誤！')) 
        
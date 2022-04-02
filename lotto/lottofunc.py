from django.conf import settings
from linebot.models import  TextSendMessage ,PostbackEvent
from linebot import LineBotApi, WebhookParser
from lotto import lottodbdata

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

def clickfunc(event):
    if  isinstance(event, PostbackEvent):
        print("[from postback data] " , event.postback.data)
        postBackData = eval(event.postback.data)
        userClick = postBackData["userclick"]
        if userClick == "最新開獎":
            # print("userclick 最新開獎")
            useFunction=postBackData["取獎號方法"]+"()"
            crawResult = eval("lottodbdata."+useFunction)
            opendate = crawResult['開獎日期']
            opennum = crawResult['期別']
            balls = (crawResult['開出獎號'])

            if crawResult['遊戲名稱'] == '大樂透':
                spball = (crawResult['特別號'])
                msg = f"{crawResult['遊戲名稱']}\n開獎日期:{opendate}\n期別:{opennum}\n開出獎號: {balls}\n特別號: {spball}"
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=msg))

            elif crawResult['遊戲名稱'] == '威力彩':
                spball = (crawResult['第二區'])
                msg = f"{crawResult['遊戲名稱']}\n開獎日期:{opendate}\n期別:{opennum}\n開出獎號: {balls}\n第二區: {spball}"
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=str(msg)))

            elif crawResult['遊戲名稱'] == 'BINGO':
                supernum = (crawResult['超級獎號'])
                bigOrSmall = crawResult['猜大小']
                singleOrDouble = crawResult['猜單雙']
                msg = f"{crawResult['遊戲名稱']}\n開獎日期:{opendate}\n期別:{opennum}\n開出獎號: {balls}\n超級獎號: {supernum}\n猜大小: {bigOrSmall}\n猜單雙: {singleOrDouble}"
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=str(msg)))

            else:
                msg = f"{crawResult['遊戲名稱']}\n開獎日期:{opendate}\n期別:{opennum}\n開出獎號: {balls}"
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=str(msg)))                
            
        elif userClick == "上期獎號":
           print(postBackData[1])
           print(postBackData[2])

from linebot import LineBotApi
from django.conf import settings
from linebot.models import CarouselTemplate, CarouselColumn ,PostbackTemplateAction ,TemplateSendMessage, TextSendMessage, QuickReplyButton,QuickReply,LocationAction,URIAction
import googlemaps
from geopy.distance import geodesic

gmaps=googlemaps.Client(key="*")
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

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

def getLottoMenu(event):
    print("getLottoMenu")
    lottonames = [key for key in lottodata]
    #"大樂透", "威力彩", "今彩539", "雙贏彩", "BINGO BINGO賓果賓果", "3星彩", "4星彩", "38樂合彩", "49樂合彩", "39樂合彩"
    ccl = []
    for lottoname in lottonames:
        lottofunc = lottodata[lottoname]
        column = CarouselColumn(
            text = lottoname ,
            actions= [
                #Postback data 回傳到 Views.py
                PostbackTemplateAction(
                    label="最新開獎",
                    text= f"{lottoname} 最新開獎",
                    data= "{'responType': '台彩postback', 'userclick': '最新開獎', '取獎號方法': '%s', '遊戲名稱': '%s' }"  %(lottofunc , lottoname)                  
                ),
                PostbackTemplateAction(
                    label="上期獎號",
                    text= f"{lottoname} 上期獎號",
                    data= f"台彩postback,上期獎號,lastNumber,{lottoname}"
                )
            ]
        )
        ccl.append(column)

    carouselMessage = TemplateSendMessage(
        alt_text='CarouselTemplate',
        template=CarouselTemplate(ccl)
    )
    line_bot_api.reply_message(event.reply_token,carouselMessage)

def sendUserLocation(event):
    replymessage = TextSendMessage(
        text='請點傳送位置並分享您的位置給我',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=LocationAction(label="傳送位置")
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token,replymessage)

def listLottoStore(event):
    print("listLotto")
    rad = 500 #半徑內距離
    latitudevalue = event.message.latitude
    longitudevalue = event.message.longitude
    addressvalue=event.message.address
    userprofile=event.source.user_id
    message="目前的經度"+str(latitudevalue)+"目前的緯度"+str(longitudevalue)
    loc = {'lat': latitudevalue, 'lng': longitudevalue}
    x1 = loc['lat']
    y1 = loc['lng']
    mapResults = gmaps.places_nearby(keyword="彩卷",location=loc, radius=rad ,language="zh-TW")
    if mapResults['status'] == 'ZERO_RESULTS':
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=str("附近沒有彩卷行")))         
        return

    storeList = mapResults["results"]
    newStoreList = []
    ccl = []
    # print(storeList)
    for store in storeList:
        #print(store)
        storeName = store['name']
        storeAddress = store['vicinity']
        storeRating = store['rating']
        storeLocation =  store['geometry']['location']
        #計算兩座標點距離
        x2 = storeLocation['lat']
        y2 = storeLocation['lng']
        storeDistance = geodesic((x1,y1), (x2,y2))
        storeDistance = int(storeDistance.meters)
        result = {'storeDistance':storeDistance, 'storeName':storeName, 'storeRating': storeRating, \
            'storeAddress':storeAddress, 'storelat':x2 , 'storelng':y2, 'userlat': x1, 'userlng':y1}
        newStoreList.append(result)

    newStoreList.sort(key= lambda x: x.get('storeDistance'))
    # print(newStoreList)
    for store in newStoreList:
        column = CarouselColumn(
            title = store['storeName'],
            text = f"{store['storeAddress']}\n距離:{store['storeDistance']} 公尺",
            actions= [
                URIAction(
                    label = '立即前往',
                    uri = f"https://www.google.com.tw/maps/dir/{store['userlat']},{store['userlng']}/{store['storeAddress']}/"
                )
            ]
        )
        ccl.append(column)

    carouselMessage = TemplateSendMessage(
        alt_text='附近的彩卷行',
        template=CarouselTemplate(ccl)
    )
    line_bot_api.reply_message(event.reply_token,carouselMessage)

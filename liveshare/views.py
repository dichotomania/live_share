import os
from datetime import date, datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage ,TextMessage ,PostbackEvent,LocationMessage
from lotto import lottofunc, lottomenu
from bill import bill_fun

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError as invaildkey:
            print("[Invaild Channel secret] : ", invaildkey)
            return HttpResponseForbidden()
        except LineBotApiError as apierror:
            print(str(apierror))
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if event.message.type == 'text':

                    if event.message.text == "開獎資訊":
                        lottomenu.getLottoMenu(event)
                    elif event.message.text == "尋找彩券行":
                        lottomenu.sendUserLocation(event)
                    elif event.message.text == "本期中獎":
                        bill_fun.current(event)
                    elif event.message.text == "前期中獎":
                        bill_fun.oldData(event)   
                    elif event.message.text == "末三碼對獎":
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入發票最後三碼進行對獎！')) 
                    elif len(event.message.text ) == 3 and event.message.text .isdigit():
                        bill_fun.show3number(event,event.message.text)

                elif event.message.type == "location":
                    lottomenu.listLottoStore(event)

            if  isinstance(event, PostbackEvent):
                print(type(event) , event)
                if 'responType' in event.postback.data:
                    responDataDict = eval(event.postback.data)
                    if responDataDict['responType'] == "台彩postback":
                        lottofunc.clickfunc(event)                   
    
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


def config(request):
    day = 1
    timenow = datetime.now()
    ospath = settings.BASE_DIR
    server = settings.SERVER
    return render(request, 'index.html', locals())

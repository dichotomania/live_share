# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 15:16:57 2022

@author: USER
"""

#Get rich menu list
from linebot.exceptions import LineBotApiError


from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('HVzXr2fkdSziz+fVjitO2EGxv4YMdBMzz7RJJhU6/XHE9pQwsryegJojRufqoxVIB949WzuHbj7BCKjI9B5xTEIHuCZg77d3Gw3kJ4GP1BqQm8h0x0O7qBvtyGER3S24lDcVAgv559B5i0j1KdXo4gdB04t89/1O/w1cDnyilFU=')
rich_menu_list =line_bot_api.get_rich_menu_list()

total = []
for rich_menu in rich_menu_list:
    total.append(rich_menu.rich_menu_id)
    #line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)
print(total)





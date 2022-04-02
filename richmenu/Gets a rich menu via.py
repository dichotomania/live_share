# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 15:13:05 2022

@author: USER
"""

from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('HVzXr2fkdSziz+fVjitO2EGxv4YMdBMzz7RJJhU6/XHE9pQwsryegJojRufqoxVIB949WzuHbj7BCKjI9B5xTEIHuCZg77d3Gw3kJ4GP1BqQm8h0x0O7qBvtyGER3S24lDcVAgv559B5i0j1KdXo4gdB04t89/1O/w1cDnyilFU=')

rich_menu = line_bot_api.get_rich_menu("richmenu-22fe538a4d73fa0cae0db60900175b65")

print(rich_menu)
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 14:05:43 2022

@author: USER
"""

#Create rich menu alias A

import requests
import json

headers = {"Authorization":"Bearer HVzXr2fkdSziz+fVjitO2EGxv4YMdBMzz7RJJhU6/XHE9pQwsryegJojRufqoxVIB949WzuHbj7BCKjI9B5xTEIHuCZg77d3Gw3kJ4GP1BqQm8h0x0O7qBvtyGER3S24lDcVAgv559B5i0j1KdXo4gdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
 
body = {
        "richMenuId": "richmenu-22fe538a4d73fa0cae0db60900175b65",   # menu_a的id
       }



req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu/alias/richmenu-alias-a', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)
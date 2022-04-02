# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 14:04:39 2022

@author: USER
"""

#Update rich menu alias b

import requests
import json

headers = {"Authorization":"Bearer HVzXr2fkdSziz+fVjitO2EGxv4YMdBMzz7RJJhU6/XHE9pQwsryegJojRufqoxVIB949WzuHbj7BCKjI9B5xTEIHuCZg77d3Gw3kJ4GP1BqQm8h0x0O7qBvtyGER3S24lDcVAgv559B5i0j1KdXo4gdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
 
body = {
    "richMenuId": "richmenu-aca8a851b4b93475292236c10e7ec9a9",   # menu_b的id
    }  




req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu/alias/richmenu-alias-b', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)
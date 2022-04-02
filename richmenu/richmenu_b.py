# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 16:03:29 2022

@author: USER
"""
import requests
import json

headers = {"Authorization":"Bearer HVzXr2fkdSziz+fVjitO2EGxv4YMdBMzz7RJJhU6/XHE9pQwsryegJojRufqoxVIB949WzuHbj7BCKjI9B5xTEIHuCZg77d3Gw3kJ4GP1BqQm8h0x0O7qBvtyGER3S24lDcVAgv559B5i0j1KdXo4gdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
        "size": {"width": 2500, "height": 1686},
        "selected": "true",
        "name": "richmenu-demo-2",
        "chatBarText": "發票選單",
       "areas": [
      {
        "bounds": {
          "x": 0,
          "y": 0,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "message",
          "label": "使用說明",
          "text": "使用說明"
        }
      },
      {
        "bounds": {
          "x": 833,
          "y": 0,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "message",
          "label": "末三碼對獎",
          "text": "末三碼對獎"
        }
      },
      {
        "bounds": {
          "x": 1666,
          "y": 0,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "message",
          "label": "掃描對獎", 
          "text": "掃描對獎"
        }
      },
            {
        "bounds": {
          "x": 0,
          "y": 843,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "message",
          "label": "本期中獎",
          "text": "本期中獎"
        }
      },
            {
        "bounds": {
          "x": 833,
          "y": 843,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "message",
          "label": "前期中獎", 
          "text": "前期中獎"
        }
      },
      {
        "bounds": {
          "x": 1666,
          "y": 843,
          "width": 833,
          "height": 843
        },
        "action": {
                "type": "richmenuswitch",
                "richMenuAliasId": "richmenu-alias-a",
                "data": "richmenu-changed-to-a"
                
 }
      }
   ]
}

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)
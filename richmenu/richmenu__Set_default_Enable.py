# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 11:31:10 2022

@author: USER
"""

import requests

headers = {"Authorization":"Bearer HVzXr2fkdSziz+fVjitO2EGxv4YMdBMzz7RJJhU6/XHE9pQwsryegJojRufqoxVIB949WzuHbj7BCKjI9B5xTEIHuCZg77d3Gw3kJ4GP1BqQm8h0x0O7qBvtyGER3S24lDcVAgv559B5i0j1KdXo4gdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu-22fe538a4d73fa0cae0db60900175b65', 
                       headers=headers)

print(req.text)




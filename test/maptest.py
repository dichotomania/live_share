#address_to_coordinate.py
from turtle import distance
import requests
import urllib.request
import json
import time
import googlemaps
from geopy.distance import geodesic
import math

gmaps=googlemaps.Client(key="AIzaSyBTbe1RWM9HOIbJT1XSrDHNmRwfy5A-Dr8")

loc = {'lat': 24.02421254799439, 'lng': 121.56980328261852}
rad = 100

mapResults = gmaps.places_nearby(keyword="彩卷",location=loc, radius=rad ,language="zh-TW")
print(mapResults)
mapResults = dict(mapResults)
print(type(mapResults))
if mapResults['results'] :
    print("test")
else :
    print("no data")

storeList = mapResults["results"]
print(storeList)

if mapResults['status'] == 'ZERO_RESULTS':
    print("data")
else:
    print("data get ")

for store in storeList:
    print(store)
    storeName = store['name']
    storeAddress = store['vicinity']
    storeRating = store['rating']
    storeLocation =  store['geometry']['location']
    #計算兩座標點距離
    x1 = loc['lat']
    y1 = loc['lng']
    x2 = storeLocation['lat']
    y2 = storeLocation['lng']
    storeDistance = geodesic((x1,y1), (x2,y2))
    storeDistance = int(storeDistance.meters)
    print(storeName)
    print(storeRating)
    print(storeAddress)
    print(storeDistance)

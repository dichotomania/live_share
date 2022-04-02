import pymongo
from pymongo import MongoClient
import urllib.parse

username = urllib.parse.quote_plus('jarvis')
password = urllib.parse.quote_plus("#5X7@@7hi6TYnCe")
url = "mongodb+srv://{}:{}@cluster0.jry7x.mongodb.net/myFirstDatabase?retryWrites=true&w=majority/".format(username, password)
cluster = MongoClient(url)
db = cluster['Sample']
collection = db['temporary']


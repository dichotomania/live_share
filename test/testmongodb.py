import pymongo

myclient = pymongo.MongoClient("mongodb://root:123456@localhost:27017/")
mydb = myclient["liveshare"]
mycol = mydb["lotto"]

mydict = { "name": "John", "address": "Highway 37" }
mydict2 = { "name": "John", "address": "Highway 37" , "sex": "male"}
dictlist = [mydict ,mydict2]

# x = mycol.insert_one(mydict2)

x = mycol.insert_many(dictlist)
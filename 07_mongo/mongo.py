#Stefan Tan
#SoftDev2 pd8
#K06 -- Yummy Mongo Py
#2019-02-28

import pymongo

SERVER_ADDR = "104.248.49.56"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.MongoTrees
collection = db.prizes

'''
Finds all earthquakes by alert.
'''
def findPrizeYear(year):
    prizes = collection.find({"year":year})
    for p in prizes:
        print(p)

findPrizeYear(2018)

    

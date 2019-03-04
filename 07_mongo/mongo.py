#Stefan Tan
#SoftDev2 pd8
#K07 -- Import/Export Bank
#2019-03-01

'''
Name of Dateset: Nobel Prize
Description:
It contains data on all the winners of the Nobel Prizes, categorized by year, category, and etc.
Link to Raw Data: http://api.nobelprize.org/v1/prize.json
Summary of Import Method:
-Got rid of the first curly brace and the respective ending curly brace as well as the "prizes" or else it will be imported as 1 document.
-Added --jsonArray flag in the mangoimport command that we used before to import the data. 
'''

import pymongo

SERVER_ADDR = "104.248.49.56"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.MongoTrees
collection = db.prizes

'''
Finds prizes by year.
'''
def findPrizeYear(year):
    prizes = collection.find({"year":year})
    for p in prizes:
        print(p)

'''
Finds prizes by category.
'''
def findPrizeCategory(category):
    prizes = collection.find({"category":category})
    for p in prizes:
        print(p)

'''
Finds prizes by category and year.
'''
def findPrizeCY(category, year):
    prizes = collection.find({"$and":[{"category":category}, {"year":year}]})
    for p in prizes:
        print(p)

'''
Finds prizes by category and less than specified id.
'''
def findPrizeCatID(category, ID):
    prizes = collection.find({"$and":[{"category":category}, {"laureates.id":{"$lt": ID}}]})
    for p in prizes:
        print(p)

'''
Finds prizes by category and year and id.
'''
def findPrizeCYID(category, year, ID):
    prizes = collection.find({"$and":[{"category":category}, {"year":year}, {"laureates.id":ID}]})
    for p in prizes:
        print(p)

findPrizeYear("2018")
findPrizeCategory("physics")
findPrizeCY("physics", "2018")
findPrizeCatID("physics", "10")
findPrizeCYID("physics", "2018", "960")
    

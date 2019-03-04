#Stefan Tan
#SoftDev2 pd8
#K06 -- Yummy Mongo Py
#2019-02-28

import pymongo

SERVER_ADDR = "104.248.49.56"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.MongoTrees
collection = db.earthquakes

'''
Finds all earthquakes by alert.
'''
def findEQAlert(alert):
    earthquakes = collection.find({"features.properties.alert":alert})
    for e in earthquakes:
        print(e)

'''
Finds all earthquakes with the magnitude.
'''
def findEQMag(magnitude):
    earthquakes = collection.find({"features.properties.mag":magnitude})
    for e in earthquakes:
        print(e)

'''
Finds all earthquakes with n numbers of tsunami.
'''
def findEQTsunami(n):
    earthquakes = collection.find({"features.properties.tsunami":n})
    for e in earthquakes:
        print(e)

'''
Finds all earthquakes with a magnitude less than or equal to the parameter.
'''
def findEQMagLess(magnitude):
    earthquakes = collection.find({"features.properties.mag":{"$lte":score}})
    for e in earthquakes:
        print(e)

print("START")
findEQAlert("green")
print("HELLO")


    

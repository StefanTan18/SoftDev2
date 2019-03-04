#Stefan Tan
#SoftDev2 pd8
#K06 -- Yummy Mongo Py
#2019-02-28

import pymongo

SERVER_ADDR = "104.248.49.56"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.test
collection = db.restaurants

'''
Finds all restaurants in a specified borough.
'''
def findRestBorough(borough):
    restaurants = collection.find({"borough":borough})
    for restaurant in restaurants:
        print(restaurant)

'''
Finds all restaurants in a specified zip code.
'''
def findRestZip(zipcode):
    zipcode = str(zipcode)
    restaurants = collection.find({"address.zipcode":zipcode})
    for restaurant in restaurants:
        print(restaurant)

'''
Finds all restaurants in a specified zip code and with a specified grade.
'''
def findRestZipGrade(zipcode, grade):
    zipcode = str(zipcode)
    restaurants = collection.find({"$and":[{"address.zipcode":zipcode},
                                              {"grades.grade":grade}]})
    for restaurant in restaurants:
        print(restaurant)

'''
Finds all restaurants in a specified zip code with a score below a specified threshold.
'''
def findRestZipScore(zipcode, score):
    zipcode = str(zipcode)
    score = str(score)
    restaurants = collection.find({"$or":[{"address.zipcode":zipcode},
                                            {"grades.score":{"$lt":score}}]})
    for restaurant in restaurants:
        print(restaurant)

def findRestBCG(borough, cuisine, grade):
    restaurants = collection.find({"$and":[{"borough":borough},
                                           {"cuisine": cuisine},
                                           {"grades.grade":grade}]})
    for restaurant in restaurants:
        print(restaurant)

print("Printing restaurants based on borough...\n\n")
findRestBorough("Manhattan")
print("\n\nPrinting restaurants based on zipcode...\n\n")
findRestZip(10017)
print("\n\nPrinting restaurants based on zipcode and grade...\n\n")
findRestZipGrade(10017, "B")
print("\n\nPrinting restaurants based on zipcode and score...\n\n")
findRestZipScore(10017, 20)
print("\n\nPrinting restaurants based on borough, cuisine, and grade...\n\n")
findRestBCG("Manhattan", "American", "A")

    

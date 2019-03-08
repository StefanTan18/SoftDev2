from flask import Flask, render_template, request, session, url_for, redirect, flash
import os
import pymongo
import json

app = Flask(__name__)
app.secret_key = os.urandom(32)

SERVER_ADDR = "104.248.49.56"
connection = pymongo.MongoClient(SERVER_ADDR)
connection.drop_database("WorldWarZ")
db = connection.WorldWarZ
collection = db.movies

f = open("data/movies.json")
data = json.load(f)
collection.remove()
collection.insert_many(data["movies"])

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/ip", methods=['POST'])
def connect():
    try:
        connection.drop_database("WorldWarZ")
        connection = pymongo.MongoClient(request.form['ip'])
        db = connection.WorldWarZ
        collection = db.movies

        f = open("./data/movies.json")
        data = json.load(f)
        collection.remove()
        collection.insert_many(data["movies"])
        
    except:
        flash("Not a valid ip address to connect to")
        print("Not a valid ip address to connect to")

if __name__ == "__main__":
    app.debug = True
    app.run()

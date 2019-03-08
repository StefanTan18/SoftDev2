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

with open('data/movies.json') as f:
    lines = f.read()
    data = json.loads(lines)
    collection.insert_many(data)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/ip", methods=['POST'])
def connect():
    #try:
    ip = request.form['ip']
    connection = pymongo.MongoClient(SERVER_ADDR)
    connection.drop_database("WorldWarZ")
    connection = pymongo.MongoClient(ip)
    db = connection.WorldWarZ
    collection = db.movies
        
    with open('data/movies.json') as f:
        lines = f.read()
        data = json.loads(lines)
        collection.insert_many(data)
        
    #except:
      #  flash("Not a valid ip address to connect to")
       # print("Not a valid ip address to connect to")

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.debug = True
    app.run()

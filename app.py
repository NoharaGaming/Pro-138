from re import search
from unicodedata import name
from flask import Flask, jsonify, request
from data import data

app =  Flask(__name__)

@app.route("/starData")
def starData():
    name = request.args.get("name")
    search = next(i for i in data if i["name"]==name)
    return jsonify({
        "data":search,
        "message":"success"
    
    }),200

app.run()
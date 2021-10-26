#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 14:28:30 2021

@author: fennieliang
"""
#pip install flask
#open terminal for mac type
#export FLASK_APP=lesson0408_flask1.py

#for windows type
#set FLASK_APP=lesson0408_flask1.py

#flask run


from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>My Python Class.</h1>"

@app.route("/Users/<name>")#must be your own path name
def user(name):
    return  "<h2>Hello, {}!</h2>".format(name)
app.run()

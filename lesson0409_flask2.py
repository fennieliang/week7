#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 14:28:30 2021

@author: fennieliang
"""

#open terminal for mac type
#export FLASK_APP=lesson0409_flask2.py

#for windows type
#set FLASK_APP=lesson0409_flask2.py

#flask run


from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
    #when using render_template the index.html file 
    #needs to be placed in templates of current folder as /templates/index.html

@app.route("/Users/<name>")#must be your own path name
def user(name):
    return render_template("user.html",name=name)
    #when using render_template the user.html file 
    #needs to be placed in templates of current folder as /templates/user.html
app.run()

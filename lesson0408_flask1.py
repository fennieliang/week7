#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 14:28:30 2021

@author: fennieliang
"""
#pip install flask

'''
for running flask:
first make sure your previous running program
is stopped by using control c on the terminal, 
or click on the red button on the spyder console

from terminal:
1.on mac type
  export FLASK_APP=lesson0408_flask1.py

or on windows type
  set FLASK_APP=lesson0408_flask1.py

2. type flask run
3. copy and paste the result server address to 
   a browser

'''

from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>My Python Class for week7.</h1>"

@app.route("/Users/<name>")#must be your own path name
def user(name):
    return  "<h2>Hello, {}!</h2>".format(name)
app.run()

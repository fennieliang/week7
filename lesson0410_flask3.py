#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 14:28:30 2021

@author: fennieliang
"""
#pip install flask-moment
'''
for running flask:
first make sure your previous running program
is stopped by using control c on the terminal, 
or click on the red button on the spyder console

from terminal:
1.on mac type
  export FLASK_APP=lesson0410_flask3.py

or on windows type
  set FLASK_APP=lesson0410_flask3.py

2. type flask run
3. copy and paste the result server address to 
   a browser

'''


from flask import Flask, render_template
from datetime import datetime



app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html", current_time=datetime.utcnow())
    #when using render_template the index.html file 
    #needs to be placed in templates of current folder as /templates/index.html

@app.route("/Users/<name>")#must be your own path name
def user(name):
    return render_template("user.html", name=name)
    #when using render_template the user.html file 
    #needs to be placed in templates of current folder as /templates/user.html
app.run()

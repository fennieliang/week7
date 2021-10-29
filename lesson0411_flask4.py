#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 14:28:30 2021

@author: fennieliang
"""
'''
for running flask:
first make sure your previous running program
is stopped by using control c on the terminal, 
or click on the red button on the spyder console

from terminal:
1.on mac type
  export FLASK_APP=lesson0411_flask4.py

or on windows type
  set FLASK_APP=lesson0411_flask4.py

2. type flask run
3. copy and paste the result server address to 
   a browser

'''


from flask import Flask, render_template
  
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index1.html')

@app.route('/my-link/')
def my_link():

  url = "https://www.businessinsider.in/business/news/top-10-richest-people-in-the-world/articleshow/74415117.cms"
  
  page = requests.get(url)
  
  soup = BeautifulSoup(page.content, "html.parser")
  
  targets = soup.find_all('strong')#the easy bit
  
  s=""
   
  for target in targets:
      s=s+target.text+'<p>'
      #list result in html format and 
      #seperate each line with <p>
  
  
  return s

if __name__ == '__main__':
  app.run(debug=True)


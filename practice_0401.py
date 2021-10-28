#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 10:01:40 2021

@author: fennieliang
"""

from bs4 import BeautifulSoup
import requests
import re

url = "https://www.businessinsider.in/business/news/top-10-richest-people-in-the-world/articleshow/74415117.cms"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

targets = soup.find_all('strong') #extract top 10 name and possession

#for target in targets:
    
    #print (target.text)

#this part from class
def find_name(string):
        matches = re.finditer('([A-Z][a-z]+\s){1,}', string)
        return matches

def find_digit(string):
        matches = re.finditer('(\d+,){0,}(\d+.)(\d+)', string)
        return matches
    
  
for target in targets:
    values = find_name(target.text)
    keys = find_digit(target.text)   
    for value in values:
        print (value[0], end=':')
    for key in keys:
        print (key[0])
    

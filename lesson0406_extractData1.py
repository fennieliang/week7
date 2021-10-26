#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 16:39:05 2021

@author: fennieliang

extract yahoo stock
"""


#pip install selenium

from bs4 import BeautifulSoup
from selenium import webdriver

######################################
driver = webdriver.Chrome("/Users/fennieliang/Documents/Doc/nccu/spider_py/chromedriver")


driver.get("https://tw.stock.yahoo.com/h/kimosel.php")

content = driver.page_source
soup = BeautifulSoup(content)


container = soup.find_all('table')#get all tables
print (len(container))

'''
for tb in container:
    for tds in tb.find_all('a'):
        print(tds.text)
        

#get tables with attributs align=center
container = soup.find_all('table',attrs = {'align':'center'})
print (len(container))
for tb in container:
    for tds in tb.find_all('a'):
        print(tds.text)

'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 16:39:05 2021

@author: fennieliang

extract yahoo stock
"""


#pip install selenium
#for using webdriver you need to download chrome driver first
#first check your chrome version
#open chrome click the top left chrome>about google chrome
#get your own chrome version then go to the following page
#https://chromedriver.chromium.org/downloads
#select the right verison to download
#put the driver in your preferred folder as the following example path


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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:19:28 2021

@author: fennieliang

extract a list of stock names and numbers
"""
from bs4 import BeautifulSoup
from selenium import webdriver
import re

from lesson_04_class import FileOperate as fo

######################################
driver = webdriver.Chrome("/Users/fennieliang/Documents/Doc/nccu/spider_py/chromedriver")


driver.get("https://www.tej.com.tw/webtej/doc/uid.htm")

content = driver.page_source
soup = BeautifulSoup(content)
print (len(soup.find_all('td')))
path = '/Users/fennieliang/Documents/GitHub/python/lesson04/'
name = 'stock_detail.txt'
string =''
fo.create(path, name, string)

#first way of extracting all the tds
for td in soup.find_all('td'):
    
    p= re.sub(r'\W+',' ',td.text)
    
    #print(p.strip())
    string = p.strip()+'\n'
    fo.append(path, name, string)
'''
#second way of extraction, use regular patten match: x:str="(.*?)" 

for td in re.findall("x:str=\"(.*?)\"",soup.prettify()):
       
    #print(p.strip())
    string = td.strip()+'\n'
    print (string)
    fo.append(path, name, string)
'''






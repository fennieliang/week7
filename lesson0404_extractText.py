#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 17:00:10 2021

@author: fennieliang
"""
#top 10 richest person in the world

from bs4 import BeautifulSoup
import requests

#
#url = "https://docs.spyder-ide.org/current/index.html"
#url = "https://www.bbc.co.uk/schedules/p00fzl6g"
url = "https://www.businessinsider.in/business/news/top-10-richest-people-in-the-world/articleshow/74415117.cms"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# check if the website works
print(soup.get_text())# scrape text from the website

targets = soup.find_all('strong')#the easy bit

for target in targets:
    
    print (target.text)
    
    

'''
practic 0401 put the targets into a key:value dictionary
'''




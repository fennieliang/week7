#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 13:26:36 2021

@author: fennieliang
"""

from bs4 import BeautifulSoup
import requests
import re

url = "https://www.businessinsider.in/business/news/top-10-richest-people-in-the-world/articleshow/74415117.cms"

page = requests.get(url).text

#split once to cut the page into two parts
tt=page.split('</script><div id="fb-root">')

#for the second part do another split
tt2=tt[1].split('<div style="display:none;">')

#calculate the length of the first part of the second split
print(len(tt2[0]))

#remove everything before <strong> from the above
new_t = re.sub('(.*?)<strong>', '', tt2[0])

#check the new length
print (len(new_t))
#print (new_t)

#split sentence using strong tag
sections =tt2[0].split('<strong>')

for section in sections:
    print(section)
    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 14:59:04 2018

@author: little_frog
"""

import requests
from pyquery import PyQuery as pq
import time

path = '/picture/%s.jpg'
###offset
for p in range(1,12):
    page = 'http://www.beautylegmm.com/Lucy/beautyleg-1305.html?page='
    page = page+str(p)
    html = requests.get(page)
    if html.status_code != 200:
        continue
    
    html = html.text
    doc = pq(html)

    img = doc('img').items()
    for im in img:
        img_path = 'http://www.beautylegmm.com'+im.attr('src')
        r = requests.get(img_path)
        with open(path%img_path[-8:-4],'wb') as f:
            f.write(r.content)
            time.sleep(1)
 ###enjoy

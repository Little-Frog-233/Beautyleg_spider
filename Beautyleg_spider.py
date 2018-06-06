#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 14:59:04 2018

@author: ruicheng
"""

import requests
from pyquery import PyQuery as pq
import time

path = '/Users/ruicheng/Documents/图片/爬虫图片保存/美腿寫真 No.1305 Lucy 2016.06.13 [48P]/%s.jpg'
#path_description = '/Users/ruicheng/Documents/图片/爬虫图片保存/美腿寫真 No.1607 Avril 2018.05.18 [67P]/description.txt'
###还差一个网页推移的offset即可实现自动化
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
        with open(path%img_path[-8:-4],'wb') as f:###以二进制打开
            f.write(r.content)
            time.sleep(1)
            



###爬取图片
#count = 0
#for num in range(1,68):
#    num = '0000'+str(num)
#    num = num[-4:]
#    r = requests.get('http://www.beautylegmm.com/photo/beautyleg/2018/1607/beautyleg-1607-%s.jpg'%num)
#    with open(path%num,'wb') as f:###以二进制打开
#        f.write(r.content)###一定要是.content才能获取二进制文件，用.text获取的是文本文件
#    count+=1
#    if count==10:
#        time.sleep(1)

        
#img = doc('img').items()
#for im in img:
#    print(im.attr('src'))
#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: test2.py
# Author: cx
# Created Time: Tue Nov 28 21:34:33 2023
##########################################################################
import requests
from bs4 import BeautifulSoup
import os

#url = "http://go7188.tpddns.cn:11081/"
#url = "http://go7188.tpddns.cn:11081/0023%20%E8%AE%A1%E7%AE%97%E6%9C%BA%E4%B8%93%E4%B8%9A"
url = "http://go7188.tpddns.cn:11081/0001%20%E8%81%8C%E4%B8%9A%E8%A7%84%E5%88%92PPT%E8%8C%83%E6%9C%AC%EF%BC%88%E5%8E%9F%E6%96%87%E5%9F%BA%E7%A1%80%E4%B8%8A%E4%BF%AE%E6%94%B9%E5%B0%B1%E5%8F%AF%EF%BC%8C%E5%8F%AF%E6%8D%A2%E6%88%90%E5%85%B6%E4%BB%96PPT%E6%A8%A1%E6%9D%BF%EF%BC%89"
response = requests.get(url).text
print(response)

soup = BeautifulSoup(response,"html.parser")
all_tags = soup.findAll("a")

ppt_dir = "ppt/"
if os.path.exists(ppt_dir) is not True: 
	os.makedirs(ppt_dir)

for tag in all_tags:
	res = requests.get("http://go7188.tpddns.cn:11081/"+ tag['href']).content
	with open(ppt_dir + tag.string, "wb") as f:
		f.write(res)
		
	print(url + tag['href'])





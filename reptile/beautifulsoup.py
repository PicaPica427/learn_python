#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: beautifulsoup.py
# Author: cx
# Created Time: Mon Nov 27 23:49:42 2023
##########################################################################
import requests
from bs4 import BeautifulSoup

content = requests.get("http://books.toscrape.com/").text
soup = BeautifulSoup(content,"html.parser") # 指定解析器 #BeautifulSoup将html解析成树状结构
all_prices = soup.findAll("p",attrs={"class":"price_color"}) #返回可迭代对象
all_titles = soup.findAll("h3")
for title in all_titles:
	all_links = title.findAll("a")
	for link in all_links:
		print(link.string)
	

for price in all_prices:
#	print(price)
	print(price.string)


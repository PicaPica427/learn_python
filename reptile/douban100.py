#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: test.py
# Author: cx
# Created Time: Tue Nov 28 00:05:36 2023
##########################################################################
import requests
from bs4 import BeautifulSoup

for start in range(0,250,25):
	i = 1
	content = requests.get("https://movie.douban.com/top250?start={}".format(start), \
														headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
																				Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0)"}).text
	soup = BeautifulSoup(content,"html.parser") # 指定解析器 #BeautifulSoup将html解析成树状结构
	print(soup)
	titles = soup.findAll("span",attrs={"class":"title"})
	for title in titles:
		if '/' not in title.string:
			print(f"{start+i}",title.string)

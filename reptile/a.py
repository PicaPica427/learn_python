#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: a.py
# Author: cx
# Created Time: Mon Nov 27 22:34:17 2023
##########################################################################

# HTTP请求
# requests library

# HTML 网页结构
# Beautiful Soup library

# HTTP
	# Hypertext Transfer Protocol

# HTTP请求
	# GET方法 获得数据 ，  POST方法 创建数据

import requests
# 有些浏览器会根据User-agent判断请求是否来自于真人
# 伪造浏览器请求头
#head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
#response = requests.get("https://www.bilibili.com",headers = head)

# F12 network 请求标头 User-Agent
response = requests.get("https://movie.douban.com/top250",headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0)"})
#response = requests.get("https://movie.douban.com/top250") #418 


#response = requests.get("https://books.toscrape.com")
if response.ok :
	print(response.status_code)
	print(response.text)
	f = open("text.txt","w")
	f.write(response.text)
else:
	print(response)
	print("request error")


# HTML			 定义网页的结构和信息
# CSS  			 定义网页的样式
# JavaScript 定义网页和用户的交互逻辑

from bs4 import BeautifulSoup

content requests.get("http://www.example.com/").text
soup = BeautifulSoup(content,"html.parser") # 指定解析器 #BeautifulSoup将html解析成树状结构
all_prices = soup.findAll("p",attrs={"class":"price_color"}) #返回可迭代对象
for price in all_prices:
	print(price)





#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: test2.py
# Author: cx
# Created Time: Tue Nov 28 21:34:33 2023
##########################################################################
# 缩进导致的问题
# 没有注意网址格式的问题

# 比较字符串 直接==
# os.path.dirname() os.makedirs
# global value

import requests
from bs4 import BeautifulSoup
import os

url = "http://go7188.tpddns.cn:11081/"
response = requests.get(url).text

soup = BeautifulSoup(response,"html.parser")
all_dir = soup.findAll("a")

file_list = {}

local_dir = "build/"
if os.path.exists(local_dir) is not True: 
	os.makedirs(local_dir)

def func(dir_): 
	global local_dir
	old_dir  = local_dir 

	for tag in dir_:
		if(tag.string == "[To Parent Directory]"):
			continue

		# print("tag:" + tag.string)
		if "." in tag.string: # 文件
			web_path   = url + tag['href']
			local_path = local_dir + tag.string
			file_list[local_path] = web_path
			print(web_path)
			# print("add " + web_path  )
			# print("add " + local_path)
			
			os.makedirs(os.path.dirname(local_path),exist_ok=True)
			res = requests.get(web_path).content
			with open(local_dir + tag.string,"wb") as f:
				f.write(res)

		else: 
			local_dir  = local_dir  + tag.string + "/"
			now_path = url + tag['href'][1:]
			# print("cal " + now_path)
			
			
			res = requests.get(now_path).content
			# print("code: " , requests.get(now_path).status_code)

			func(BeautifulSoup(res,"html.parser").findAll("a"))

			# for x,y in file_list.items():
			# 	print(x,"-->",y)
			# print(file_list)
	#print("ppt_dir=",ppt_dir)
	#print("old_dir=",old_dir)
		local_dir  = old_dir


func(all_dir)

for x,y in file_list.items():
	print(x,"-->",y)
# print(file_list)



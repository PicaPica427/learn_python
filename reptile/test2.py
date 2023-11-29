#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: test2.py
# Author: cx
# Created Time: Tue Nov 28 21:34:33 2023
##########################################################################
#正则表达式 re
#网络请求分析
#json数据分析 及 可视化
#爬虫 requests库
#dict 增删查改
#sorted函数
#os库
#读写文件/图片


import requests
import re
import os

#url = "https://www.qschina.cn/university-rankings/world-university-rankings/2024"
url = "https://www.qschina.cn/sites/default/files/qs-rankings-data/cn/2208747.txt?_=1701178520496"
response = requests.get(url)


js = response.json()["data"]

country = {} #dict
univs   = [] #list
region  = {}


logo_dir = "logo/"
if os.path.exists(logo_dir) is not True: 
	os.makedirs(logo_dir)


for i in js:
#	<div class="td-wrap"><a href="/universities/university-kragujevac" class="uni-link">克拉古耶瓦茨大学</a></div>
	#m = re.match(r'<div.*?link">(.*?)</a></div>',i["title"])
	#print(i["rank_display"]+" ",m.group(1))


	if i["country"] not in country.keys():
		country[i["country"]] = 1
	else:
		country[i["country"]] += 1

	# if i["region"] not in region.keys():
	# 	region[i["region"]] = 1
	# else:
	# 	region[i["region"]] += 1

	m = re.match(r'<div.*?link">(.*?)</a></div>',i["title"])

	print(i["rank_display"]+" " + i["score"],m.group(1)) 
	univs.append(i["rank_display"] + " " + m.group(1)+'\n') #to write qs100.txt


	pic_url = "https://www.qschina.cn" + i["logo"] #"https://www.qschina.cn/sites/default/files/university-of-cambridge_95_small.jpg"
	
	# g = requests.get(pic_url).content              #write logo/pic
	# with open(logo_dir + i["rank_display"] + " " +  m.group(1) + ".jpg","wb") as fw:
	# 	fw.write(g)

		
f_rank = open("qs100.txt","w")
for i in univs:
	f_rank.write(i)



del country['']

country = dict(sorted(country.items(),key=lambda x:x[1],reverse=False)) # sort
# region  = dict(sorted(region .items(),key=lambda x:x[1],reverse=False)) # sort


#for i,j in country.items():
#	print(i,j)
# for i,j in region.items():
# 	print(i,j)




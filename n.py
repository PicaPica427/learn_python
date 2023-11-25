#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: n.py
# Author: cx
# Created Time: Sat Nov 25 15:00:17 2023
##########################################################################
# 拆包
# 字典 sicp opencv

# 拆包
# Tuple....
# eg. a,b = 1,2

tTuple = {1,2,3,4} # 也可以是[列表]{集合}
c,d,e,f = tTuple

print("tTuple:",tTuple)
print("tTuple:",c,d,e,f)
print("tTuple:",*tTuple) # 使用*进行拆包
# a, b, c ,d = *tup     # error

c,*_,d = tTuple  # 将中间的东西打包给 _
print("tTuple:",c,d,"*_:",_)

Dict = {"1":"a","2":"b","3":"c"}
print(*Dict) #拆包得到字典的key


(lambda **kwargs: print("lambda:",kwargs))(**Dict)  # **Dict 用于字典传参



#函数拆包
def f(a,*args): # 多余的参数被打包成元组
	print(a)
	print(args) 

g = lambda a,*args: print(args)

arg = (1,2,3,4,5,6,[1,2,3])
#f(1,2,3,"45")
#g(1,2,3,"45")

g(1,arg)#作为单独的参数传参
g(*arg) #解包后传参


# 命令行传参
import sys
print(len(sys.argv)) #len获得长度
print(sys.argv)










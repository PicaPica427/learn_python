#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: a.py
# Author: cx
# Created Time: Mon Nov 20 23:18:28 2023
##########################################################################

# https://www.w3schools.com/python/python_lists.asp

# TASK1

thislist = ["apple","banana","cherr", 1]
print(thislist)
print(len(thislist))


# type(list) is list 
print(type(thislist))

for i in thislist:
	print(i,end=' ...  ')

print("--------------------")


# type((1,2,3)) is Tuple 
print(type((1,2)))



#	There are four collection data types in the Python programming language
	# List is a collection which is ordered and changeable. Allows duplicate members.
	# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
	# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
	# Dictionary is a collection which is ordered** and changeable. No duplicate members.

#------------------------------------------------------------
# TASK2 

thislist = [i for i in range(10,20)]
print(thislist)
print(thislist[1])
print(thislist[-1])
print(thislist[2:5]) # 12 13 14
print(thislist[:4])  # 10 11 12 13
print(thislist[8:])  # 18 19
print(thislist[::3]) # 10 13 16 19
print(thislist[::-1]) # 19 18 .... 10
print(thislist[::-2]) # 19 17 .... 11 

print(thislist[8:3:-2]) # 18 16 14          not 3:8:-2
print(thislist[-4:-1]) # 16 17 18           not include -1(19)

a = 15         # change it 
if a in thislist:
	print("find it ")
else:
	print("can't find")

#------------------------------------------------------------

# TASK 3

thislist = ["a","b","c","d","e"]
thislist[1] = "B"
thislist[2:4] = ["C","D"]
print(thislist) # change successful

thislist[4:6] = ["E","F"] # ?
print(thislist) # list len add 1 

thislist.insert(5,"Z")
print(thislist) # "E","Z","F"

thislist.append("X")
print(thislist)

thislist.insert(999,"Y") # out of range, but insert right
print(thislist)


append_list = ["1","2","3"]
thislist.extend(append_list) # 1,2,3 will be appended to the end of thislist 
print(thislist) 

thistuple = {1:"123",2:"12345"}  # and so on, tuple or set can used this way to appended.
thislist.extend(thistuple) # 1,2 will be appended to the end of thislist 
print(thislist)            # not include "123","12345"



thislist.pop()
# thislist.pop(999) # out of range, cause exception

# del 
# del thislist

thislist.remove('Z') # delete first match

print(thislist)            


# thislist.clear()
# print(thislist)            

# for i in thislist:
# 	print(i)
for i in range(len(thislist)):
	print(thislist[i],end=' ')
print()

# [print(x,end=' ') for x in thislist]  # work right

# newlist = [expression for item in iterable if condition == True]     # List Comprehension


newlist = [x.upper() for x in thislist if type(x) != int ]
print(newlist)

newlist.sort() 
newlist.sort(reverse=True) # Sort Descending

newlist.sort(key = lambda x : abs(ord(x[0])-50)) # 2,3,1 .... # Customize Sort Function # who closed 50

print(newlist)

#TASK4 

# Copy a List : 2 method    list.copy() and list(list1)

oldlist = [1,2,3]
newlist = oldlist # newlist will only be a reference to list1 , changes made in newlist will automatically also be made in list2

newlist = oldlist.copy()
new2list = list(oldlist)

oldlist[1] = 4

print(newlist)
print(new2list)


print(new2list + oldlist) # plus list and list



# Tuple

# 需要修改元素时 先转换成list

thistuple = ("apple","banana","cherry","cherry",True)
print(thistuple)
print(len(thistuple))

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
print(thistuple[1])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)



fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow,*red) = fruits # or not include ()

print(green)
print(yellow)
print(red)



fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2


print(mytuple)

#-----------
print("Set")
thisset = {"apple", "banana", "cherry", "apple"} # set {}    list []    tuple () 
thislist = {1,2,3}
print(thisset)
print(len(thisset)) # second apple will be ignore

thisset = ("apple", "banana", "cherry", True, 1, 2) # True and 1
print(set(thisset + thisset)) #此处不是set + set
a = set(thisset)
a.add("1")
a.update([1,5,6,7,8,9,10])

try :
	a.remove("1")
	a.remove("22")
except:
	print("not found")

print(a)
print()

# ---------------------------
setA = {1,2,3,4}
setB = {"a","b","c",4}

setC = setA.union(setB)
print(setC)

setC = setA.intersection(setB)
print(setC)

setC = setA.symmetric_difference(setB)
print(setC)

print(setA & setB)
print(setA | setB)
print(setA - setB)
print(setA ^ setB)
print(setA ^ setB)


list1 = ['a','b']
list2 = ['c','d','e']


import itertools
#笛卡尔积
for i in itertools.product(list1,list2):
	print(i)



# ---------------------------

#Dictionary
Dict = {
	"age"  : 10 ,
	"name" : "x",
	"score": "1",
	"func" : lambda x: x+1,
	"l" : [1,2,3]
}

x = Dict.get("func")
print(x)
x = Dict["func"](1)
print("call:",x)

def print_func():
	print("Dict:")
	for i in Dict.keys(): # 遍历 keys方法   Dict.values()获得值列表
	#	print("  {:>5} : {}".format(i,Dict[i]))
	#	print("  %5s : %s" % (i,Dict[i]))
		print(f"  {i:>5} : {Dict[i]}")

def print_func2():
	x = Dict.items()
#Test
#-----
#	'dict_items' object does not support item assignment
#	x["age"] = 50 
#-----
	print("print2:",x)
	
print_func2()

Dict["age"] = 20
print_func()

x = Dict.values()
Dict["age"] = 30
print_func()
print(x)        # 会跟着字典一起改变

#查找
if "age" in Dict:
	print("exist")
if "fu" in Dict:
	print("exist")
else:
	print("not found")

#删除
del Dict["age"]
# del Dict["11111111"] # cause exception
Dict.pop("l")

print_func()


# 使用copy 或 dict()拷贝字典!


# 嵌套字典
dict1 = {"1":1,"2":2}
dict2 = {"2":2}
dict3 = {"a":dict1,"b":dict2}

print(dict3["a"]["1"])


	


























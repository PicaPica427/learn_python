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











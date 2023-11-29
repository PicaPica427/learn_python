#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: build-in.py
# Author: cx
# Created Time: Sun Nov 26 11:04:49 2023
##########################################################################

# map(function, iterable, ...)
	# Python3 return iterator

l =  map(lambda x:x*x+2,[1,2,3,4,5])
print(list(l))

# vars([object])

class A():
	a = "A"
	b = "C"
	def get(c):
		return (c.a,c.b)

a = A().get()
print(a)

print(vars(A)) #注意接受的是类 而不是类的实例
print()


# enumerate(sequence, [start=0])

import numpy as np
a = np.random.randint(1, 100, [1,10])

a = list(*a) # *a 拆分array 
a.sort() # no return value

l = [i for i in a] 
print( list(enumerate(l))) #为每个元素增加一个Index


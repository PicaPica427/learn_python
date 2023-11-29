#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: oop.py
# Author: cx
# Created Time: Sun Nov 26 11:35:58 2023
##########################################################################
class A():
	a = "A"
	b = "C"
	c = 1
	def get(self):
		return (self.a,self.b)

a = A()
b = A()

# A.c = 5 #更改类属性
# a.c = 4   #只能更改类实例里的属性

print(a.c)
print(b.c)
print(A.c)

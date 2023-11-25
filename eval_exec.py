#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
##########################################################################
# File Name: eval_exec.py
# Author: cx
# Created Time: Sat Nov 25 15:55:50 2023
##########################################################################

#eval exec

# find more details and python dynamic code here
# https://zhuanlan.zhihu.com/p/60257325

# eval(expression, globals=None, locals=None)

x = 1
def f():
	y = 2
	z = eval("x+y")
	print(z)
	z = eval("x+y",{"x":2,"y":2})
	print(z)
	z = eval("x+y",{"x":2,"y":2},{"x":2,"y":3})
	print(z)

f()


# exec(object[, globals[, locals]])
x = 1
y = 1
z = exec("x = 1+y")
print("exec:",x,y,z) # 3,2,None






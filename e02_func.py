# -*- coding: utf-8 -*-
## 
import re
from functools import reduce

#1 lamda 匿名函数
mul = lambda x:x*x
add = lambda x:x+x
iterable =  [1,2,3,4,5,6,7,8,9]

#2 map
m0 = map(add, iterable)
print(list(m0))

funcs = [mul, add]
m1 = map(lambda f:f(3), funcs)
print(list(m1))

#3 reduce
func = lambda x,y:x+y
m2= reduce(func, iterable)
print(m2)

#4 filter
def is_odd(n):
    return n % 2 == 1

m3 = filter(is_odd, iterable)
print(list(m3))


#5 sorted
print("-----sorted------")
nums = [36, 5, -12, 9, -21]
print(nums)
print(sorted(nums))
#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
print(sorted(nums, key=abs)) 

names = ['bob', 'about', 'Zoo', 'Credit']
print(names)
print(sorted(names))
print(sorted(names, key=str.lower, reverse=True)) #小写比较，并反向排序


#6 decorator装饰器
import time


def log(func):
	def wrapper(*args, **kw):
		print("%s() in" %func.__name__)
		ret = func(*args, **kw)
		print("%s() out" %func.__name__)
		return ret
	return wrapper

## error with return value
# def log2(func):
# 	print("%s() in" %func.__name__)
# 	ret = func()
# 	print("%s() out" %func.__name__)
# 	return ret

@log
def now():
	print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

@log
def now_time():
	tm = time.localtime(time.time())
	print(time.strftime('%Y-%m-%d %H:%M:%S',tm))
	return tm

now()
print(now_time())



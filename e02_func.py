# -*- coding: utf-8 -*-
## 
import re
import collections
from functools import reduce


#1. lamda 匿名函数
mul = lambda x:x*x
add = lambda x:x+x
iterable =  [1,2,3,4,5,6,7,8,9]


#2. map:接收一个函数和一个序列，返回一个Iterator,惰性序列
m0 = map(add, iterable)
print(type(m0), m0)
print("Iterable:", isinstance(m0, collections.Iterable))
print("Iterator:", isinstance(m0, collections.Iterator))
print("map:", list(m0), "\n")

m1 = map(lambda f:f(3), [mul, add])
print("map:", list(m1))


#3. reduce:接收一个函数和一个序列，返回一个计算结果
r1 = reduce(lambda x,y:x+y, iterable)
print("reduce:", r1)

words = ["how", "are", "you", "can", "i", "help", "you"]
r2 = reduce(lambda x,y:x+' '+y, words)
print("reduce:", r2)


#4. filter：接收一个函数和一个序列，返回处理为True的结果
def is_odd(n):
    return n % 2 == 1

m3 = filter(is_odd, iterable)
print("filter:", list(m3))


#5. sorted
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
import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print("%s() in" %func.__name__)
		ret = func(*args, **kw)
		print("%s() out\n" %func.__name__)
		return ret
	return wrapper


@log
def now():
	print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

@log
def now_time():
	tm = time.localtime(time.time())
	print(time.strftime('%Y-%m-%d %H:%M:%S',tm))
	return tm

print("\n---------decorator------------")
print(now)
now()
print(now_time())


# test other way.
def log2(func):
	print("%s() in" %func.__name__)
	ret = func()
	print("%s() out" %func.__name__)
	return ret

def foofunc():
	print("hello test")
	return "hello"

ret = log2(foofunc)
print(ret)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test time module '

__author__ = 'Kevin deng'


import time
import datetime


#1、datetime时间函数

#datetime与字符串间的转换
def datetime2str(dt):
	return dt.strftime("%Y-%m-%d %H:%M:%S")

def str2datetime(strtime):
	return datetime.datetime.strptime(strtime, "%Y-%m-%d %H:%M:%S")

#取当前时间(datetime)
def test_datetime():
	print("\ntest_datetime:")
	now = datetime.datetime.now()
	print("now datetime:", type(now), now)

	strtime = datetime2str(now)
	print(type(strtime), strtime)

	dt = str2datetime(strtime)
	print(type(dt), dt)


#2、时间戳（float）函数

#时间戳timestamp(float)与字符串间的转换
def timestamp2str(timestamp):
	time_array = time.localtime(timestamp)
	return time.strftime("%Y-%m-%d %H:%M:%S", time_array)

def str2timestamp(strtime):
	time_array = time.strptime(strtime, "%Y-%m-%d %H:%M:%S")
	return time.mktime(time_array)

#取当前时间戳
def test_timestamp():
	print("\ntest_timestamp:")
	now = time.time()
	print("now time:", type(now), now)

	strnow = timestamp2str(now)
	print(type(strnow), strnow)

	tm = str2timestamp(strnow)
	print(type(tm), tm)


#3、时间字符串格式变换
def test_strtime():
	print("\ntest_strtime:")
	strtime = "2017-05-16 15:43:42"

	#use time
	time_array = time.strptime(strtime, "%Y-%m-%d %H:%M:%S")
	print("time_array:", time_array)
	str2 = time.strftime("%Y/%m/%d %H:%M:%S", time_array)
	print(strtime, "->", str2)

	#use datetime
	dt = datetime.datetime.strptime(strtime, "%Y-%m-%d %H:%M:%S")
	str3 = dt.strftime("%Y/%m/%d %H:%M:%S")
	print(strtime, "->", str3)


#计算时间差
def time_diff_now(strtime):
	print("\n----time_diff_now------")

	# datetime
	now = datetime.datetime.now()
	print("now:", type(now), now)

	old = datetime.datetime.strptime(strtime, "%Y-%m-%d %H:%M:%S")
	print("old:", type(old), old)

	diff = now-old
	print("now-old:",type(diff), diff)
	print("seconds:", diff.seconds)
	print("microseconds:", diff.microseconds)
	print("days:", diff.days)

	# time
	time_now = time.time()
	time_next = time_now + 20
	print("now: %s" % timestamp2str(time_now))
	print("next: %s" % timestamp2str(time_next))


# 计时函数。windows下正常，linux下不对
def time_clock_diff():
	print("\n----time_clock_diff------")
	cl1 = time.clock()
	print("cl1:", type(cl1), cl1) #第一个次运行结果，不能只看值
	time.sleep(1.3)

	cl2 = time.clock()
	print("cl2:", type(cl2), cl2)
	time.sleep(0.8)

	cl3 = time.clock()
	print("cl3:", type(cl3), cl3)

	diff = cl2-cl1
	print("cl2-cl1:", type(diff), diff)

def perf_counter_diff():
	print("\n----perf_counter_diff------")
	cl1 = time.perf_counter()
	print("cl1:", type(cl1), cl1)
	time.sleep(1.3)

	cl2 = time.perf_counter()
	print("cl2:", type(cl2), cl2)
	time.sleep(0.8)

	cl3 = time.perf_counter()
	print("cl3:", type(cl3), cl3)

	diff = cl2-cl1
	print("cl2-cl1:", type(diff), diff)


# 用装饰器来增加时间统计功能
from functools import wraps

def timethis(func):
	''' Decorator that reports the execution time.
	'''
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(func.__name__, end-start)
		return result
	return wrapper	


@timethis
def test():
	test_datetime()
	test_timestamp()
	test_strtime()

	strtime = "2017-02-16 15:43:42"
	time_diff_now(strtime)

	time_clock_diff()
	perf_counter_diff()


if __name__=='__main__':
	test()

	# 去掉wrapper装饰器来运行
	func = test.__wrapped__
	func()
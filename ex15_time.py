#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test time module '

__author__ = 'Kevin deng'


import time
import datetime

#把datetime转成字符串
def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d-%H")

#把字符串转成datetime
def string_toDatetime(string):
    return datetime.strptime(string, "%Y-%m-%d %H:%M:%S")

#把字符串转成时间戳timestamp
def str2timestamp(strtime):
	timeArray = time.strptime(strtime, "%Y-%m-%d %H:%M:%S")
	time1 = time.mktime(timeArray)
	print(type(timeArray), timeArray)
	print(type(time1), time1)
	return time1	

def time_diff_now(strtime):
	""" 计算时间差 """ 
	print("\n----time_diff_now------")
	now = datetime.datetime.now()
	print(type(now), now)

	old = datetime.datetime.strptime(strtime, "%Y-%m-%d %H:%M:%S")
	print(type(old), old)

	diff = now-old
	print(type(diff), diff)
	print("seconds:", diff.seconds)
	print("microseconds:", diff.microseconds)
	print("days:", diff.days)

# windows is ok
def time_clock_diff():
	cl1 = time.clock()
	print(type(cl1), cl1)
	time.sleep(1.3)

	cl2 = time.clock()
	print(type(cl2), cl2)
	time.sleep(0.8)

	cl3 = time.clock()
	print(type(cl3), cl3)

	diff = cl2-cl1
	print("cl2-cl1:", type(diff), diff)

def perf_counter_diff():
	cl1 = time.perf_counter()
	print(type(cl1), cl1)
	time.sleep(1.3)

	cl2 = time.perf_counter()
	print(type(cl2), cl2)
	time.sleep(0.8)

	cl3 = time.perf_counter()
	print(type(cl3), cl3)

	diff = cl2-cl1
	print("cl2-cl1:", type(diff), diff)

def test():
	strtime = "2017-02-16 15:43:42"
	tm = str2timestamp(strtime)
	time_diff_now(strtime)

	time_clock_diff()
	# perf_counter_diff()


if __name__=='__main__':
	test()
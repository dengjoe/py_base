#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test time module '

__author__ = 'Kevin deng'


import time
import datetime


def str2timestamp(strtime):
	timeArray = time.strptime(strtime, "%Y-%m-%d %H:%M:%S")
	time1 = time.mktime(timeArray)
	print("timeArray:", type(timeArray), timeArray)
	print("time1:", type(time1), time1)
	return time1	

def time_diff_now(strtime):
	# 计算时间差
	now = datetime.datetime.now()
	print(type(now), now)

	old = datetime.datetime.strptime(strtime, "%Y-%m-%d %H:%M:%S")
	print(type(old), old)

	print(now-old)
	print("seconds:", (now-old).seconds)
	print("days:", (now-old).days)


def test():
	strtime = "2017-02-16 15:43:42"
	tm = str2timestamp(strtime)
	time_diff_now(strtime)

if __name__=='__main__':
	test()
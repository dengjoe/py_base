#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a file test module '

__author__ = 'kevin deng'

import os
import csv

def write_file(fname):
	try:
		f = open(fname, 'w')
		if f:
			f.write("hello baby\n")
			f.write("world \n")		
	finally:
		if f:
			print("close file\n")
			f.close()

def read_file(fname):
	try:
		f = open(fname, 'r')
		if f:
			content = f.read()
			print(content)
	finally:
		if f:
			f.close()

# 不需try，也无需close的
def read_file2(fname):
	with open(fname, 'r') as f:
		for line in f.readlines():
			print(line.strip()) # 把末尾的'\n'删掉	

# 读取csv文件
def read_csv(fname):
	data = []
	with open(fname, "r", encoding='UTF-8') as csvfile:
		reader = csv.reader(csvfile) # 读取csv文件，返回的是迭代类型
		for item in reader:
			data.append(item)
	print(data)


if __name__ == '__main__':
	fname = "./test.txt"
	write_file(fname)
	read_file(fname)
	read_file2(fname)

	read_csv("./stocks.csv")

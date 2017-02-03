#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys
import getopt

def test():
	args = sys.argv
	print(args)

	if len(args)<5:
		print(args[0], '-i inputname -o outputname')
		return -1

	#getopt函数的第二个参数是短参数选项。"h"是一个开关选项；"i:"和"o:"则表示后面应该带一个参数。
	#getopt函数的第三个参数[, long_options]为可选的长选项参数.
	#getopt函数返回两个列表：opts和args。opts为分析出的格式信息。args为不属于格式信息的剩余的命令行参数。
	#	opts是一个两元组的列表。每个元素为：(选项串,附加参数)。如果没有附加参数则为空串''。
	#opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
	opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["version", "file="])
	input_file=""
	output_file=""
	print("opts:", opts)

	for op, value in opts:
		if op == "-i":
			input_file = value
		elif op == "-o":
			output_file = value
		elif op == "--version":
			print("version=10")
		elif op == "--file":
			print("file=", value)
		elif op == "-h":
			print("h")
			sys.exit()

	print("in:", input_file, ";out:", output_file)

# 测速命令，带长短参数： 
# python e01.py -o fiout -i finany --version --file=abd -h
if __name__=='__main__':
    test()
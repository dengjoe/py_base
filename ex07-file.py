#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a file test module '

__author__ = 'kevin deng'

import os

try:
	f = open('./test.txt', 'w')
	if f:
		f.write("hello ")
		f.write("world \n")		
finally:
	if f:
		print("close\n")
		f.close()


try:
	f = open('./test.txt', 'r')
	if f:
		content = f.read()
		print(content)
finally:
	if f:
		f.close()


# 不需try，也无需close的
with open('./test.txt', 'r') as f:
	print(f.read())

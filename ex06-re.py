#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a regex test module '

__author__ = 'Kevin deng'

import re

#正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。

# 1、识别:成功，则返回一个Match对象，否则返回None
print("\n====== match =====")

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.match(r'^\d{3}\-\d{3,8}$', '010+12345'))

# 2、查找
m = re.search(r'\d{3}', "010+234 iow 456")
if m:
	print(m)
	print(m.group())

# 3、查找子串。成功则返回list，包含所有子串
m = re.findall(r'\d{3}', "010+234 iow 456")
if m:
	print(m)


# 4、切分，生成list
print("\n====== split =====")

fname = "The Legend of 1900.1998.海上钢琴师.双语字幕.HR-HDTV.AC3.1024X576.x264.mkv"
print(fname.split('.'))
print(re.split(r'[\.\s]', fname))

# 5、分组。返回tuple
print("\n====== group =====")

m = re.match(r'([\w\s.\']+).(\d{4}).([\w]+)', fname)
print(m.groups())
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))

# 6、字符串替换
strall = "@123 023 中文@12345"
result = re.sub(r'\@\d{3}', "abc", strall)
print(result)

# 用regex对象
reobj = re.compile(r'\@\d{3}')
result = reobj.sub("aaa", strall)
print(result)



name = ["The Boat That Rocked.2009.海盗电台.BD中英双字.mp4",
        "All.Quiet.on.the.Western.Front.1930.西线无战事.BD.中英双字.rmvb",
        "12 monkey.2003.12只猴子.双语字幕.HR-HDTV.AC3.1024X576.x264.mkv",
        "12 monkey.12.2003.12只猴测试.双语字幕.HR-HDTV.AC3.1024X576.x264.mkv",
        "2012.2009.2012世界末日.双语字幕.HR-HDTV.AC3.1024X576.x264.mkv",
        "A.Bug's.Life.1998.虫虫特攻队.双语字幕.国粤英音轨.HR-HDTV.AC3.1024X576.X264-人人影视制作.mkv",
        "The Legend of 1900.1998.海上钢琴师.双语字幕.HR-HDTV.AC3.1024X576.x264-YYeTs人人影视.mkv",
        "2012.双语字幕.HR-HDTV.AC3.1024X576.x264.mkv"]

# 贪婪匹配，这个2012有问题，但海上钢琴师很好
print("\n====== greedy =====")

def test_pat(pat, msg):
	print(msg)
	m = pat.match(name[4])
	print(m.groups())
	m = pat.match(name[6])
	print(m.groups())

pat = re.compile(r'([\w\s.\']+).(\d{4}).([\w]+)')
test_pat(pat, "gredy:")
pat = re.compile(r'([\w\s.\']+?).(\d{4}).([\w]+)')
test_pat(pat, "shrink:")


# 非贪婪匹配 加?。
print("")
pat = re.compile(r'([\w\s.\']+?).(\d{4}).([\w]+)') #编译运行，提高效率
for val in name:
	m = pat.match(val)
	if m:
		print(m.groups())
	else:
		print("*:", val)

print("\n------ test @names in string --------")
msgs = ["@山长 清一 测试句子123","@0484吴庆可常州 测试句子123","@心灯不灭 测试句子123",
		 "@335王云兰河南 测试句子123","@0047 蒋有超 深圳 测试句子123","@0614张新 广州 测试句子123",
		 "@山长助理李菊英 测试句子123","@023+助李英+舞台上 测试句子123", "@汉中  吕丽 测试句子123"]
for sz in msgs:
	m = re.match(r'(@\d{0,4}[\+\s]?\w{2,10}[\+\s]{0,3}\w{0,6})\s(.+)', sz)
	if m:
		print(m.groups())
	else:
		print("err:", sz)

"""
萍子@爱旅行(44557248)
李冬（中天）(5458190)
御今学堂—李志强(108453172)
摩西<bing-.-xin@qq.com>
0224于凤菊威海<fly-02@qq.com>
ヤ_﹏.葉.(5354319)
La T'ao(757036415)
"""
print("\n------ test names/id --------")
names = ["(188799612)", "<tt6826@163.com>", "糖果~(190690962)",  
         "0712 李卫贞 广州(649308223)","张芸溪<tt6826@163.com>", "0138王利利济南(279200540)",
         "萍子@爱旅行(44557248)","摩西<bing-.-xin@qq.com>", "ヤ_﹏.葉.(5354319)",
         "御今学堂—李志强(108453172)","La T'ao(757036415)", "李冬（中天）(5458190)"]
for name in names:
	m = re.match(r'([\d\w\+\s\!\-\~\@]{0,20})[\(\<]([\w\d\~\.\@\-]+[\>\)]$)', name)
	if m:
		print(m.groups())
	else:
		print("err:", name)


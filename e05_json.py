#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a json test module '

__author__ = 'kevin deng'

import json

# dump & load string
di = dict(name="joe", age=21, score=88)
strdi = json.dumps(di, indent=4)
print(strdi, type(strdi))

di2 = json.loads(strdi)
print(di2, type(di2))

# load from file
with open(".\e05_json.json") as pf:
	confs = json.load(pf)
	print(confs, type(confs))

# 对象序列化为json
class MsgItem(object):
	def __init__(self, dic):
		self.__name = dic["name"]
		self.__uid  = dic["uid"]
		self.time = dic["time"]
		self.content = dic["content"]

	def __del__(self):
		print("MsgItem exit")

	def __str__(self):
		return "%s  %d  %s  %s" % (self.__name, self.__uid, self.time, self.content)

	def json(self):
		return {
		"name": self.__name,
		"uid": self.__uid,
		"time": self.time,
		"content": self.content
		}

	@property
	def uid(self):
		return self.__uid

	@uid.setter
	def uid(self, uid):
		self.__uid = uid


def dict2MsgItem(d):
    return MsgItem(d)

def MsgItem2json(msg):
	return msg.json()


def test_json_msg():
	""" msg object <--> json string demo """
	print("\nmsg object <--> json string:")

	json_str = '{"name": "joe", "uid": 4567, "time": "2017-05-12 12:30:21", "content": "hello world"}'
	msg = json.loads(json_str, object_hook=dict2MsgItem)
	print(msg, type(msg))

	msg.uid = 12345
	# 如果用此lambda函数使用对象的dict，则不要使用私有成员变量，以方便key名一一对应
	strmsg = json.dumps(msg, default=lambda msg1: msg1.__dict__)
	print(strmsg, type(strmsg))

	# 使用私有成员变量，则应该增加转换函数
	strmsg = json.dumps(msg, default=MsgItem2json)
	print(strmsg, type(strmsg))


if __name__ == '__main__':
	test_json_msg()
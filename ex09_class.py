#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Mycle(object):
	""" 自定义类的演示，包括构造、析构、字符串等通用api，和自定义属性。 """
	num_count = 0 # 相当于类静态变量
	def __init__(self, name, score):
		self.__class__.num_count += 1
		self.__name = name
		self.__score = score

	def __del__(self):
		self.__class__.num_count -= 1
		print("num_count:", self.__class__.num_count)

	def __str__(self):
		return "name:%s, score:%d" % (self.__name, self.__score)

	@property
	def score(self):
		return self.__score;

	@score.setter
	def score(self, score):
		self.__score = score


def test_mycle():
	print(Mycle.__doc__)
	print(Mycle.__dict__)

	ne = Mycle("hello", 123)
	print(ne)
	ne.score = 234
	print(ne)
	print(ne.__doc__)
	print(ne.__dict__)

	ne2 = Mycle("hello2", 456)
	print(ne2)


if __name__ == "__main__":
	test_mycle()
	ne3 = Mycle("hello3", 567)
	print(ne3)

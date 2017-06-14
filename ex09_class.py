#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Mycle(object):
	""" 自定义类的演示，包括构造、析构、字符串等通用api，和自定义属性。 """
	num_count = 0 # 相当于类静态变量
	def __init__(self, name, score):
		self.__class__.num_count += 1
		self._name = name
		self._score = score

	def __del__(self):
		self.__class__.num_count -= 1
		print("num_count:", self.__class__.num_count)

	def __str__(self):
		return "name:%s, score:%d" % (self._name, self._score)

	# 这是类似于C#的方式，称为String Formatting Method Calls
	# 惊叹号！后接a 、r、 s，声明是使用何种模式，分别为：acsii模式、引用__repr__ 或 __str__
	def __repr__(self):
		return 'Mycle({0._name!r}, {0._score!r})'.format(self)

	# 属性及设置
	@property
	def score(self):
		return self._score;

	@score.setter
	def score(self, score):
		self._score = score

	# 类方法
	@classmethod
	def new_Mycle(cls):
		# 相当于重载构造函数，给默认初始值
		return Mycle("None", 0)

	@classmethod
	def get_num_count(cls):
		return cls.num_count

	# 静态方法
	@staticmethod
	def who_am_i():
		print("I am a staticmethod")


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

	print("")
	ne3 = Mycle.new_Mycle()
	print(ne3)
	print(Mycle.get_num_count())
	Mycle.who_am_i()
	ne3.who_am_i()



# 测试使用type()函数动态创建类
def test_type_class():
	"""测试使用type()函数动态创建类。type()既可以返回一个对象的类型，又可以创建出新的类型"""
	# 先定义函数
	print("\ntest_type_class:")

	def fn(self, name='world'): 
		print('Hello, %s.' % name)

	# 创建Hello class。
	Hello = type('Hello', (object,), dict(hello=fn)) 
	h = Hello()
	h.hello()


if __name__ == "__main__":
	test_mycle()
	ne3 = Mycle("hello3", 567)
	print(ne3)

	test_type_class()

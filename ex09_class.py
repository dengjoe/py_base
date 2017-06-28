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


# 演示单体模式
class Singleton(type):
	def __init__(self, *args, **kwargs):
		self.__instance = None
		super().__init__(*args, **kwargs)

	def __call__(self, *args, **kwargs):
		if self.__instance is None:
			self.__instance = super().__call__(*args, **kwargs)
			return self.__instance
		else:
			return self.__instance

def test_singleton():
	class Spam(metaclass=Singleton):
		def __init__(self):
			print('Creating Spam')

	a = Spam()
	b = Spam()
	print(a==b)


# 可调用类
class Averager():
	"""可调用类，计算移动平均值"""
	def __init__(self):
		self.series = []

	def __call__(self, new_value):
		self.series.append(new_value)
		total = sum(self.series)
		return total/len(self.series)

def test_averager():
	print("")
	avg = Averager()
	print(avg.__class__.__name__)
	print(avg(10))
	print(avg(11))
	print(avg(12))


# 闭包:闭包是一种函数，它会保留定义函数时存在的自由变量的绑定，这样调用函数时，虽然定义作用域不可用了，但是仍能使用那些绑定。
def make_averager():
	"""计算移动平均值的高阶函数"""
	series = [] #series 是自由变量（free variable）。指未在本地作用域中绑定的变量

	def averager(new_value):
		series.append(new_value)
		total = sum(series)
		return total/len(series)

	return averager

def test_make_averager():
	avg = make_averager()
	print(avg.__code__.co_varnames, avg.__code__.co_freevars)
	print(avg(10))
	print(avg(11))
	print(avg(12))
	print(avg.__closure__[0].cell_contents)
	print("%r\n" % avg.__closure__)

#闭包的nolocal版
def make_averager2():
	count = 0
	total = 0

	def averager(new_value):
		nonlocal count, total #必须声明nolocal，否则会因为赋值而被认为是局部变量
		count += 1
		total += new_value
		return total / count

	return averager

def test_make_averager2():
	avg = make_averager2()
	print(avg.__code__.co_varnames, avg.__code__.co_freevars)
	print(avg(10))
	print(avg(11))
	print(avg(12))
	print(avg.__closure__[0].cell_contents, avg.__closure__[1].cell_contents)
	print("")


if __name__ == "__main__":
	test_mycle()
	ne3 = Mycle("hello3", 567)
	print(ne3)

	test_type_class()
	test_singleton()

	test_averager()
	test_make_averager()
	test_make_averager2()

# -*- coding:utf8 -*-

import collections

### tuple
print("\ntuple:")

t1 = ("a","c","f","d")
print("t1:", t1)
print("t1[1]:", t1[1])

for a in t1[:3]:
	print(a)

m1 = list(range(0,10,2))
m3 = m1[:3]
t1 = ("g","o","o","d", m3)
print("t1:", t1)
m3.reverse()
print("t1:", t1)


# generator
def test_generator():
	print("\ngenerator")
	ll = [x*x for x in range(10)]
	print(type(ll), ll)
	print("Iterator:", isinstance(ll, collections.Iterator))

	lli = iter(ll)
	print(type(lli), lli)
	print("Iterator:", isinstance(lli, collections.Iterator))


	gl = (x*x for x in range(10))
	print(type(gl), gl)
	print("Iterator:", isinstance(gl, collections.Iterator))
	print("next", next(gl))
	for val in gl:
		print(val)


	print(dir(ll))
	# print(dir(gl))


def test_tuples01():
	print("\ntuples01:")

	# 输出时格式运算符能自动匹配，另外支持占位符_
	traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),  ('ESP', 'XDA205856')]
	for passport in sorted(traveler_ids):
		print('%s/%s' % passport)

	for country, _ in traveler_ids:
		print(country)


def test_split_tuple():
	""" 元组拆包test """
	lax_coordinates = (33.9425, -118.408056)
	print(lax_coordinates)

	latitude, longitude = lax_coordinates
	print("latitude=%f, longitude=%f" %(latitude, longitude))

	city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

	# 用*来处理剩下的元素
	a, b, *c = range(5)
	print(a,b,c)

	a, *b, c = range(5)
	print(a,b,c)


def test_nested_tuple():
	metro_areas = [
		('Tokyo','JP',36.933,(35.689722,139.691667)),
		('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
		('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
		('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
		('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
		]

	# 格式化输出
	print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
	fmt = '{:15} | {:9.4f} | {:9.4f}'
	for name, cc, pop, (latitude, longitude) in metro_areas:
		if longitude <= 0:
			print(fmt.format(name, latitude, longitude))


def test_namedtuple():
	City = collections.namedtuple('City', 'name country population coordinates')
	tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

	print(tokyo)
	print(tokyo.name, tokyo.coordinates)

	print(City._fields)



if __name__ == '__main__':
	test_generator()

	test_tuples01()
	test_split_tuple()
	test_nested_tuple()
	test_namedtuple()

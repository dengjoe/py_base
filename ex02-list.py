# -*- coding:utf8 -*-

import collections

#list operation
vechiles = ["bike","motor","car"]

# iterable function
print("Iterable:", isinstance(vechiles, collections.Iterable))
print("Iterator:", isinstance(vechiles, collections.Iterator))
print("Iterable:", isinstance('abc', collections.Iterable))
print("Iterator:", isinstance('abc', collections.Iterator))
print(vechiles)

for i, value in enumerate(vechiles):
	print(i, value)

print("item 0:", vechiles[0])
print("item -1:", vechiles[-1]) # the last item

# item set
print("\nedit list:")
vechiles[2] = "bus"
print(vechiles)

# append
vechiles.append("boat")
print(vechiles)

# insert
vechiles.insert(2, "airplane")
print(vechiles)


# delete: del语句, pop(index)
print("\ndelete list:")
del vechiles[0]
print(vechiles)

vechiles.pop() # default pop from tail
print(vechiles)

vechiles.pop(1)
print(vechiles)

# remove(item) 
vechiles.append("boat")
vechiles.append("bus")
print(vechiles)

vechiles.remove("bus")
print(vechiles)


# reverse
print("\nreverse list:")
vechiles.reverse()
print(vechiles)


# sort
print("\nsort list:")
vechiles.sort()
print(vechiles)

vechiles.sort(reverse=True)
print(vechiles)

# temp sorted
print("\nsoretd: ", sorted(vechiles))
print(vechiles)

# sorted函数，对不同类型元素的排序时，使用key
l0 = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
print(sorted(l0, key=int))
print(sorted(l0, key=str))

# len
print("\nlist len:", len(vechiles))


## range 
print("\nrange:")
m1 = []
m1 = range(0,5)
print("m1:", m1) # attention: not a list
for value in range(0,5):
	print(value)
	#m1.append(value) #error 

# range to list
m2 = list(range(0,10,2)) # [0,10), step 2
print("m2:", m2)
print("min:", min(m2))
print("max:", max(m2))
print("sum:", sum(m2))


# 切片：切片可以用于list，tuple，str
print("m2[0:3]:", m2[0:3])
print("m2[-3:]:", m2[-3:])

print("m2[:2]:", m2[:2])
print("m2[2:]:", m2[2:])

# 切片的增量
print("m2[::2]:", m2[::2])
print("m2[::3]:", m2[::3])
print("m2[::-1]:", m2[::-1])

# 对切片赋值
m2[2:4] = [20,30,40]
print("m2:%r" % m2)
del m2[2:4]
print("m2:%r" % m2)

# copy list。切片为新队列
print("\ncopy:")
m3 = m2[:3]
m3.append("ok")
print("m3:", m3)
print("m2:", m2)

# 指针赋值，两个都变了
m4 = m3
m4.append("good")
print("m3:", m3)
print("m4:", m4)


# list的+，*运算
ll1 = list(range(3))
print(ll1)
ll2 = ll1+[2]
print(ll2)
ll3 = ll1*2
print(ll3)

weird_board = [['_'] * 3] * 3
print(weird_board)


# list to set(集合)
m5 = ["ball","circle","rectangle","ball"]
print("\n",m5)
print(set(m5))


### function
print("")

def show_content(lin):
	if lin:          #判断是否为空列表
		for i,val in enumerate(lin):
			print("lin[%d]:" % i, val)
		print("finish lin")
	else:
		print("empty lin")

m1 = []
show_content(m1)
show_content(m3)

# 构建
urls = ['http://www.baidu.com/s?wd={}'.format(i) for i in range(10)]
print(urls)
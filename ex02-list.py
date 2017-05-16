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

print("m2[0:3]:", m2[0:3])
print("m2[2:]:", m2[2:])
print("m2[:2]:", m2[:2])
print("m2[-3:]:", m2[-3:])


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

# list to set(集合)
m5 = ["ball","circle","rectangle","ball"]
print("\n",m5)
print(set(m5))

### tuple
print("\ntuple:")
t1 = ("a","c","f","d")
print("t1:", t1)
print("t1[1]:", t1[1])

for a in t1[:3]:
	print(a)

t1 = ("g","o","o","d", m3)
print("t1:", t1)
m3.reverse()
print("t1:", t1)
print("\nedit list:")

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


# generator
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
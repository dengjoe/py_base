# -*- coding:utf8 -*-

#list operation
vechiles = ["bike","motor","car"]

print("item 1:", vechiles[0])
print("item -1:", vechiles[-1]) # the last item
print(vechiles)

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
print("\ntemp soretd: ", sorted(vechiles))
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


# copy list
print("\ncopy:")
m3 = m2[:3]
m3.append("ok")
print("m3:", m3)
print("m2:", m2)

# only pointer
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


### function
print("")

def show_content(lin):
	if lin:          #判断是否为空列表
		for val in lin:
			print("val:", val)
		print("finish lin")
	else:
		print("empty lin")

m1 = []
show_content(m1)
show_content(m3)



# -*- coding: utf-8 -*-
## 

# generator
def iter01(name):
	i = 0
	print("hello", name, i)
	n = yield i

	i += 1
	print("hello", name, i, n)
	n = yield i

	i += 1
	print("hello", name, i, n)
	n = yield i


print("\n---------generator------------")
a = iter01("a")
print(type(iter01))
print(type(a))

for i in a:
	print(i)

b = iter01("b")
print(b.__next__())
print(b.__next__())
print(b.__next__())
#b.__next__() #StopIteration here

c = iter01("c")
print(c.send(None))  # can't send non-None value to a just-started generator
print(c.send(8))
print(c.send(9))
#c.send(10) #StopIteration here



# 生产者-消费者
def consumer():
    r = ''
    while True:
        n = yield r
        print("in", r, n)
        if not n:
            return

        print('[C] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None) #启动生成器
    n = 0
    while n < 5:
        n = n + 1
        print('[P] Producing %s...' % n)
        r = c.send(n)
        print('[P] Consumer return: %s' % r)
    c.close()

print("\n---------produce consumer------------")
c = consumer()
print("next produce")
produce(c)


# another field
def nread_file(fpath): 
    BLOCK_SIZE = 1024 
    with open(fpath, 'r', encoding='utf8') as f: 
        while True: 
            block = f.read(BLOCK_SIZE) 
            if block: 
                yield block 
            else: 
                return

n = 0
for cont in nread_file("C:\\Users\\kevin\\Desktop\\清粉对照.txt"):
	n += 1
	print(n)

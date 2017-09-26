#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## 

# 有yield的函数就是生成器，return a generator。生成器被调用时不会立即执行。
def iter01(name):
	i = 0                    # 第1次运行进入
	print("hello", name, i)
	n = yield i              # yield不但可以返回一个值，它还可以接收调用者发出的参数。

	i += 1                   # 第2次运行进入
	print("hello", name, i, n)
	n = yield i

	i += 1                   # 第3次运行进入
	print("hello", name, i, n)
	n = yield i


def test_yield():
    print("\n------test generator a------------")
    a = iter01("a")
    print(type(iter01))
    print(a)

    for i in a:
    	print(i)

    print("------test generator b:")
    b = iter01("b")
    print(b.__next__())  # next()在python3中会错误
    print(b.__next__())
    print(b.__next__())
    #b.__next__() #StopIteration here

    print("------test generator c:")
    c = iter01("c")
    print(c.send(None))  # can't send non-None value to a just-started generator
    print(c.send(8))     # 执行send方法会首先把上一次挂起的yield语句的返回值通过参数设定，从而实现与生成器方法的交互。
    print(c.__next__())
    # print(c.send(9))
    #c.send(10) #StopIteration here



# 生产者-消费者
def consumer():
    r = ''
    while True:
        n = yield r
        print("in", r, n)
        if not n:
            print("[C] Consumer Exit!") # 测试没走这里，一般都是close了，不走这里
            return

        print('[C] Consuming ...%s' % n)
        r = '200 OK'

def produce(c):
    c.send(None)                #启动生成器
    n = 0
    while n < 3:
        n = n + 1
        print('[P] Producing %d' % n)
        r = c.send(n)           # 发给生成器（消费者）处理
        print('[P] Consumer ret=%s' % r)
    c.close()                   #停止生成器


def test_produce_consumer():
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
                yield block       #需要循环读取、而不是一下子全取出来的时候，用生成器最好。
            else: 
                return

def test_nread_file(fpath):
    print("\n--------- test_nread_file ------------")
    n = 0
    for cont in nread_file(fpath):
    	n += 1
    	print(n)


if __name__ == '__main__':
    test_yield()
    test_produce_consumer()

    test_nread_file("C:\\Users\\kevin\\Desktop\\nicknames.txt")
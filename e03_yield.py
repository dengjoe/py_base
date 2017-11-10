#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## 

"""
Python中 yield 是一个关键词，它可以用来创建协程。
1.当调用 yield value 的时候，这个 value 就被返回出去了，CPU控制权就交给了协程的调用方。
  调用 yield 之后，如果想要重新返回协程，需要调用Python中内置的 next 方法。
2.当调用 y = yield x 的时候，x被返回给调用方。要继续返回协程上下文，调用方需要再执行协程的 send 方法。
  这时，给send方法的参数会被传入协程作为这个表达式的值(本例中，这个值会被y接收到)。

这意味着我们可以用协程来写异步代码，当程序等待异步操作的时候，只需要使用yield把控制权交出去就行了，
当异步操作完成了再进入协程继续执行。
"""


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
    print("\n------test generator a:")
    a = iter01("a")
    print(type(iter01))
    print(a)

    for i in a: # 用for...in方式遍历，比while循环简洁，不用管StopIteration
    	print(i)

    print("------test generator b:")
    b = iter01("b")
    while True:
        try:
            print(next(b))  
        except StopIteration:
            print("StopIteration in b")
            break


    print("------test generator c:")
    try:
        c = iter01("c")
        print(c.send(None))  # can't send non-None value to a just-started generator
        print(c.send(8))     # 执行send方法会首先把上一次挂起的yield语句的返回值通过参数设定，从而实现与生成器方法的交互。
        print(c.__next__())  # 没有c.next()，而next()调用此__next__()
        print(c.send(9))     # StopIteration here
        c.send(10)
    except StopIteration:
        print("StopIteration in c")



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


# test socket yield
import select
import socket
 
def coroutine_socket():
    sock = socket.socket()
    sock.setblocking(0)
    address = yield sock

    try:
        sock.connect(address)
    except BlockingIOError:
        pass
    
    data = yield
    size = yield sock.send(data)
    yield sock.recv(size)
 
 
def test_socket():
    coro = coroutine_socket()
    sock = coro.send(None)
    wait_list = (sock.fileno(),)
    coro.send(('www.baidu.com', 80))
    select.select((), wait_list, ())
    coro.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: Close\r\n\r\n')
    select.select(wait_list, (), ())
    print(coro.send(1024))


if __name__ == '__main__':
    test_yield()
    test_produce_consumer()

    test_nread_file("C:\\Users\\kevin\\Desktop\\nicknames.txt")

    test_socket()
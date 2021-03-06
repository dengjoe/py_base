# -*- coding: utf-8 -*-

import asyncio
import threading

# 3.5之后，新增async，await：
# 把@asyncio.coroutine替换为async；
# 把yield from替换为await

# 如果一个生成器内部需要遍历另一个生成器，并将数据返回给调用者，你需要遍历它并处理所遇到的异常；
# 而用了 yield from 后，则可以一行代码解决这些问题。

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 直接返回，并异步调用asyncio.sleep(1)，执行完后再返回
    r = yield from asyncio.sleep(1)
    print("Hello again!")

@asyncio.coroutine
def hello1():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


def test_hello(loop):
    # 执行coroutine
    loop.run_until_complete(hello())

    tasks = [hello1(), hello1()]
    loop.run_until_complete(asyncio.wait(tasks))


# wget
@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)

    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect     # await 连接
    
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()               # await 发送请求
    
    while True:
        line = yield from reader.readline() # await 读取响应
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


def test_wget():
    print("\n========== test_wget ============")

    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))




if __name__=='__main__':
    # 获取EventLoop:
    loop = asyncio.get_event_loop()

    test_hello(loop)
    test_wget()

    loop.close()


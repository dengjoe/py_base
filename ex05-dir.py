#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

# os.listdir(dirname)：列出dirname下的目录和文件，返回list
# os.getcwd()：获得当前工作目录
# os.curdir:返回当前目录（'.')
# os.chdir(dirname):改变工作目录到dirname
# os.path.isdir(name):判断name是不是一个目录，name不是目录就返回false
# os.path.isfile(name):判断name是不是一个文件，不存在name也返回false
# os.path.exists(name):判断是否存在文件或目录name
# os.path.getsize(name):获得文件大小，如果name是目录返回0
# os.path.abspath(name):获得绝对路径
# os.path.normpath(path):规范path字符串形式

# os.path.split(name):分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
# os.path.splitext(name):分离文件名与扩展名
# os.path.join(path,name):连接目录与文件名或目录
# os.path.basename(path):返回文件名
# os.path.dirname(path):返回文件路径 

def test_path_funcs(path):
    print("os.getcwd:", os.getcwd())

    print("\n--- path functions:")
    print("split:",    os.path.split("C:\data\今日网校\今日网校第三课 未来趋势前10题（1）.mp3"))
    print("splitext:", os.path.splitext("C:\data\今日网校\今日网校第三课 未来趋势前10题（1）.mp3"))
    print("basename:", os.path.basename("C:\data\今日网校\今日网校第三课 未来趋势前10题（1）.mp3"))
    print("dirname:",  os.path.dirname("C:\data\今日网校\今日网校第三课 未来趋势前10题（1）.mp3"))
    print("dirname:",  os.path.dirname("http://rec.owllive.cn:9002/live/stream/index.m3u8"))

    name = "C:\data\今日网校\今日网（1）.mp3 cmd prog dkdsd"
    print(os.path.basename(name))
    print(name)

    print("\n--- os.listdir:%s" % path)
    print(os.listdir(path))

    print("\n--- os.walk:")
    print(os.walk(path))

def list_path(dir):  
    for f in os.listdir(dir):  
        filepath = os.path.join(dir, f)  
        if os.path.isdir(filepath):  
            print("dir: " + filepath)
            list_path(filepath)  
        elif os.path.isfile(filepath):
            # sts = f.split('.')
            # print(sts)
            print(filepath)  

def list_path1(dir):
    print("\n----list_path1-----\n") 
    yid = os.walk(dir)
    for rootDir, pathList, fileList in yid:
        print("\nrootDir:", rootDir)
        print("pathList:", pathList)
        print("fileList:", fileList)
 
def list_path2(dir):  
    print("\n----list_path2-----\n") 
    yid = os.walk(dir)  
    for rootDir, pathList, fileList in yid:  
        for file in fileList:  
            print('file ' + os.path.join(rootDir, file))  
        for path in pathList:  
            print('path ' + os.path.join(rootDir, path))

def test_list_path(path):
    print("\n----list_path-----\n") 
    list_path(path)
    list_path1(path)
    list_path2(path)


if __name__ == '__main__':
    # path = "D:/data/books/编程/语言"  
    path = "C:/data/清一文档"

    test_path_funcs(path)
    test_list_path(path)

# 获取脚本文件的当前路径
print(sys.path)
print(sys.path[0])
print(os.getcwd())
print(os.curdir)

# 创建、删除目录(下面演示相对路径)
spath = "./fun_test"
os.mkdir(spath)
print(os.path.isdir(spath))
print(os.path.isfile(spath))
os.rmdir(spath)
print(os.path.isdir(spath))

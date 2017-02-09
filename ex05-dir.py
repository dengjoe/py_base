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

print("os.getcwd:", os.getcwd())

print("\n--- path functions:")
print("split:",    os.path.split("C:\data\今日网校\今日网校第三课 未来趋势前10题（1）.mp3"))
print("splitext:", os.path.splitext("C:\data\今日网校\今日网校第三课 未来趋势前10题（1）.mp3"))
print("basename:", os.path.basename("C:\data\今日网校\今日网校第三课 未来趋势前10题（1）.mp3"))
print("dirname:",  os.path.dirname("C:\data\今日网校\今日网校第三课 未来趋势前10题（1）.mp3"))

print(os.listdir("C:\data\今日网校"))

print("\n--- os.walk functions:")
yid = os.walk("C:\data\今日网校")
for rootDir, pathList, fileList in yid:
    print("\nrootDir:", rootDir)
    print("pathList:", pathList)
    print("fileList:", fileList)


def readfile(dir):  
    for f in os.listdir(dir):  
        filepath = os.path.join(dir, f)  
        if os.path.isdir(filepath):  
            print("dir: " + filepath)
            readfile(filepath)  
        elif os.path.isfile(filepath):
            sts = f.split('.')
            print(sts)
            print(filepath)  
  
def readfile2(dir):  
    yid = os.walk(dir)  
    for rootDir, pathList, fileList in yid:  
        for file in fileList:  
            print('file ' + os.path.join(rootDir, file))  
        for path in pathList:  
            print('path ' + os.path.join(rootDir, path))


# dir = 'C:\data\\xj'  
# readfile(dir)

print("\n---------\n") 
#readfile2("C:\data\今日网校")

# 获取脚本文件的当前路径
path = sys.path[0]
print(path)
if os.path.isfile(path):
    print(os.path.dirname(path))
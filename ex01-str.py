# -*- coding:utf8 -*-

import os

#print(,) 与 print(+)的区别：前者加入一个空格来分隔，后者没有
# str operation
message = " hello World! "
print(message + "|")
print(len(message))
print(len("\n"))

# 大小写
print("\n ")
print(message.title())
print(message.upper())
print(message.lower())

# 去空白
print("\nstrip:")
print(message.strip() + "|") #两头
print(message.lstrip()+ "|") #开头
print(message.rstrip()+ "|") #结尾

# 拼接str
print("\nadd string:")
m2 = message + "\t" + "I am in."
print(m2)

print("How are " + "you? " + m2)
print("How? ", message )

# 转为str
val = 5/2
print("val:", val)

m3 = "5/2=" + str(val)
print(m3)


print("\n-----------------------\n")

#去空格及特殊符号
s = " ded g, den, "
print(s.strip().lstrip().rstrip(',') + "|")

#复制字符串
#strcpy(sStr1,sStr2)
sStr1 = 'strcpy'
sStr2 = sStr1
sStr1 = 'strcpy2'
print(sStr2)

#连接字符串
#strcat(sStr1,sStr2)
sStr1 = 'strcat'
sStr2 = 'append'
sStr1 += sStr2
print(sStr1)

#查找字符
#strchr(sStr1,sStr2)
# < 0 为未找到
print("-----find char-----")

sStr1 = 'strchr'
#print("index of u:", sStr1.index("u")) #ValueError: substring not found
print("index of s:", sStr1.index("s"))

#比较字符串: python3没有cmp了，用==就行
#strcmp(sStr1,sStr2)
print("-----compare string-----")

sStr1 = 'strchr'
sStr2 = 'strch'
print("cmp all:", sStr1==sStr2)
#print(cmp(sStr1,sStr2))

#字符串指定长度比较。
#strncmp(sStr1,sStr2,n)
sStr1 = '12345'
sStr2 = '123bc'
n = 3
print("cmp part:", sStr1[0:n]==sStr2[0:n])
# print(cmp(sStr1[0:n],sStr2[0:n]))

#扫描字符串是否包含指定的字符
#strspn(sStr1,sStr2)
sStr1 = '12345678'
sStr2 = '456'
#sStr1 and chars both in sStr1 and sStr2
print("len:", len(sStr1 and sStr2))


#字符串长度
#strlen(sStr1)
sStr1 = 'strlen'
print("len:", len(sStr1))


#将字符串中的大小写转换
#strlwr(sStr1)
sStr1 = 'JCstrlwr'
print("upper:", sStr1.upper())
print("lower:", sStr1.lower())


#追加指定长度的字符串
#strncat(sStr1,sStr2,n)
sStr1 = '12345'
sStr2 = 'abcdef'
n = 3
sStr1 += sStr2[0:n]
print(sStr1)

#复制指定长度的字符
#strncpy(sStr1,sStr2,n)
sStr1 = ''
sStr2 = '12345'
n = 3
sStr1 = sStr2[0:n]
print(sStr1)

#将字符串前n个字符替换为指定的字符
#strnset(sStr1,ch,n)
sStr1 = '12345'
ch = 'r'
n = 3
sStr1 = n * ch + sStr1[3:]
print(sStr1)

#扫描字符串
#strpbrk(sStr1,sStr2)
sStr1 = 'cekjgdklab'
sStr2 = 'gka'
nPos = -1
for c in sStr1:
    if c in sStr2:
        nPos = sStr1.index(c)
        break
print(nPos)

#查找字符串
#strstr(sStr1,sStr2)
print("-----find string-----")
sStr1 = 'abcdefg'
print("find cde:", sStr1.find("cde"))
print("find fgh:", sStr1.find("fgh"))


#分割字符串
#strtok(sStr1,sStr2)
sStr1 = 'ab,cde,fgh,ijk'
sStr2 = ','
sStr1 = sStr1[sStr1.find(sStr2) + 1:]
print(sStr1)
#或者
s = 'ab,cde,fgh,ijk'
print(s.split(','))

#连接字符串
delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

#PHP 中 addslashes 的实现
def addslashes(s):
    d = {'"':'\\"', "'":"\\'", "\0":"\\\0", "\\":"\\\\"}
    return ''.join(d.get(c, c) for c in s)
 
s = "John 'Johny' Doe (a.k.a. \"Super Joe\")\\\0"
print(s)
print(addslashes(s))


#只显示字母与数字
def OnlyCharNum(s,oth=''):
    s2 = s.lower();
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for c in s2:
        if not c in fomart:
            s = s.replace(c,'');
    return s;
 
print(OnlyCharNum("a000 aa-b"))

 

#翻转字符串
#strrev(sStr1)
sStr1 = 'abcdefg'
sStr1 = sStr1[::-1]
print(sStr1)

#截取字符串

str = "0123456789"
print(str[0:3]) #截取第一位到第三位的字符
print(str[:])   #截取字符串的全部字符
print(str[6:])  #截取第七个字符到结尾
print(str[:-3]) #截取从头开始到倒数第三个字符之前
print(str[2])   #截取第三个字符
print(str[-1])  #截取倒数第一个字符
print(str[::-1])  #创造一个与原字符串顺序相反的字符串
print(str[-3:-1]) #截取倒数第三位与倒数第一位之前的字符
print(str[-3:])   #截取倒数第三位到结尾
print(str[:-5:-3]) #逆序截取，具体啥意思没搞明白？
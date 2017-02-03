#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk  
root = tk.Tk()  

fm = []  
#以不同的颜色区别各个frame  
for color in ['red','blue']:  
    #注意这个创建Frame的方法与其它创建控件的方法不同，第一个参数不是root  
    fm.append(tk.Frame(height = 200,width = 400,bg = color))  
#向下面的Frame中添加一个Label  
tk.Label(fm[1],text = 'Hello label').pack()  
fm[0].pack()  
fm[1].pack()  

# for lf in ['red','blue','yellow']:  
#     #可以使用text属性指定Frame的title  
#     LabelFrame(height = 200,width = 300,text = lf, bg = lf).pack()  

# 创建两个列表
li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = tk.Listbox(root)          #  创建两个列表组件
listb2 = tk.Listbox(root)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)

for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()

root.mainloop()  
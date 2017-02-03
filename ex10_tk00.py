#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk # import the Tkinter module
import tkinter.filedialog as filedialog
 

def hello():
	print("Hello")

def about():
	w = tk.Label(root,text="开发者感谢名单\nxuge\n\nhttp://www.xuanji.com网站")
	w.pack(side="top")


# 创建一个窗体
root = tk.Tk()               #创建一个 root window
root.title('Hello World')    #定义窗体标题
root.geometry('400x200')     #定义窗体的大小，是400X200像素


# 创建一个导航菜单
menubar = tk.Menu(root)

#创建下拉菜单File，然后将其加入到顶级的菜单栏中
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

#创建导航菜单项
menubar.add_command(label="Hello!", command=hello)
menubar.add_command(label="Quit!",command=root.quit)

#创建下拉菜单Help
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar) # 显示菜单


# 增加一个文本输入和相应的label、button。
class TextInput(object):
	def __init__(self, master):
		self.master = master
		frame = tk.Frame(master)
		frame.pack()				# 只有pack的组件实例才能显示

		label = tk.Label(frame, text="Input text:")
		label.pack(side="left")

		default_txt = tk.StringVar()
		default_txt.set('This is a default value')
		self.intext = tk.Entry(frame, width=30, textvariable=default_txt)
		self.intext.pack(side="left")

		self.btn = tk.Button(frame, text='Ok', command=self.show_input)
		self.btn.pack(side="right")

	def show_input(self):
		w = tk.Label(self.master,text=self.intext.get())
		w.pack(side="top")

	def get_input(self):
		return self.intext.get()


class FileDir(object):
	def __init__(self, master):
		self.master=master
		frame = tk.Frame(self.master,width=100)
		frame.pack()

		label = tk.Label(frame, text="Input filename:")
		label.pack(side="left")

		self.intext = tk.Entry(frame, width=32, text="c:/")
		self.intext.pack(side="left")

		self.btn = tk.Button(frame, text='Open file', command=self.findFile)
		self.btn.pack(side="right")


	def findFile(self):
		 # define options for opening or saving a file
		self.file_opt = options = {}
		options['defaultextension'] = '.txt'
		options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
		options['initialdir'] = 'C:\\'
		options['initialfile'] = '*.txt'
		options['parent'] = root  # self.master 一样
		options['title'] = '选择文件'
		dirname=filedialog.askopenfilename(**self.file_opt)   
		self.intext.insert(0, dirname)

# tkFileDialog.askdirectory      是用来获取目录的
# tkFileDialog.askopenfilename   是用来获取文件全路径的
# tkFileDialog.askopenfilenames  是用来获取多个文件的路径的

textin = TextInput(root)
artobject=FileDir(root)

# 窗体循环
root.mainloop() # create an event loop
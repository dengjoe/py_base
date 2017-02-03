#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

# 继承了tk.Frame
class Application0(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()

        self.btn_hello = tk.Button(self)
        self.btn_hello["text"] = "Hello World"
        self.btn_hello["command"] = self.say_hi
        self.btn_hello.pack(side="top")

        self.btn_quit = tk.Button(self, text="Quit", fg="red", command=root.destroy)
        self.btn_quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

# 组合
class Application1(object):
	def __init__(self, master=None):
		frame = tk.Frame(master)
		frame.pack()

		self.btn_hello = tk.Button(frame)
		self.btn_hello["text"] = "Hello World"
		self.btn_hello["command"] = self.say_hi
		self.btn_hello.pack(side="right")

		self.btn_destroy = tk.Button(frame, text="Destroy", fg="red", command=self.btn_hello.destroy)
		self.btn_destroy.pack(side="left")

		self.btn_quit = tk.Button(frame, text="Quit", fg="red", command=frame.quit)
		self.btn_quit.pack(side="left")

	def say_hi(self):
		print("hi there, everyone!")


root = tk.Tk()

def test0():
	global root
	app = Application0(master=root)
	app.mainloop()

def test1():
	global root
	app = Application1(master=root)
	root.mainloop()
	root.destroy()


if __name__=='__main__':
	#test0()	
	test1()
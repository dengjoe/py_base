#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Mycle(object):
	def __init__(self):
		self.name = ""
		self.score = 0

	def set_score(self, name, score):
		self.name = name
		self.score = score

	def get_score(self):
		return self.score;

	def print_score(self):
		print(self.name, self.score)


ne = Mycle()
ne.set_score("hello", 123)
ne.print_score()

print(ne.get_score())



# -*- coding:utf8 -*-

# input to list
def input2list():
	print("input to list test:")
	ll = []
	while 1:
		sin = input("What's your name?(ok to exit)")
		if sin=="ok":
			print("ok & out\n")
			break;
		ll.append(sin)

	print(ll)

	while "go" in ll:
		ll.remove("go")
	return ll

# input to dict
def input2dict():	
	"""input words to name:password dict"""
	dic = {}
	name = ""
	password = ""
	while True:
		name = input("you name(exit to exit):")
		if name == "exit":
			break;
		password = input("password:")
		dic[name] = password
	return dic

nps = input2dict()
print(nps)
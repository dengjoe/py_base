# -*- coding:utf8 -*-

#dict operation
dic = {"h1":"python","h2":"c"}
dic["h1"] = "ruby"
dic["h3"] = "python"
print(dic)

print("keys:", dic.keys())
print("values:", dic.values())
print("k-values:", dic.items())

for k,v in dic.items():
	print("my fav "+k+" is : " + v)

del dic["h1"]
print(dic)

# dict in list
worker = ["smith", "cat", dic]
print("\n",worker)


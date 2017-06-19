#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a xml test module '

__author__ = 'kevin deng'

import xml.etree.ElementTree as ET


# 直接加载文件
def load_xml_file1(fname):
	tree = ET.parse(fname)
	return tree.getroot()

def save_xml_file1(fname, tree):
	tree.write(fname)

# 由字符串加载
def load_xml_file2(fname):
	with open(fname, 'r', encoding='utf8') as f:
		return ET.fromstring(f.read())

def save_xml_file2(fname, root):
	with open(fname, 'wb') as f:
		strxml = ET.tostring(root, encoding='utf8')
		f.write(strxml)


def parse_xml_root(root):
	# 节点名字和属性
	print(root.tag, root.attrib)
	for child in root:
		print("  %r %r" % (child.tag, child.attrib))

	# 遍历所有子孙节点
	for neighbor in root.iter('neighbor'):
		print(neighbor.tag, neighbor.attrib)

	#只能遍历子节点
	for neighbor in root.findall('neighbor'):
		print(neighbor.attrib)

	for country in root.iter("country"):
		# 取指定属性
		name = country.get("name")
		# 取指定子节点
		rank = country.find("rank")
		year = country.find("year")
		gdppc = country.find("gdppc")	
		neighbor = country.find("neighbor")

		print("%s %s:\t %r %r %r %r" % (country.tag, name, year.text, rank.text, gdppc.text, neighbor.attrib))


def modify_xml(root):
	for url in root.iter('Url'):
		print(url.tag, url.attrib, url.text)
		# 修改内容
		url.text = "http://192.168.10.12:8880/down/xuanchuanpian/test01.m3u8"
		# 修改和新增属性
		url.set('updated', 'yes') 


def test_xml():
	root1 = load_xml_file1('./e05_xml.xml')
	root2 = load_xml_file2('./e05_xml.xml')

	parse_xml_root(root1)

	modify_xml(root2)
	# ET.dump(root2)

	save_xml_file2("./e05_xout.xml", root2)


if __name__ == '__main__':
	test_xml()
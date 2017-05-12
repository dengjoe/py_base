# -*- coding:utf8 -*-

# http://pythonhosted.org/six/
# Python 2.x & 3.x compatible
from distutils.log import warn as printf
printf('Hello World!')


try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

# 在Python2中，iterator版本是itertools.izip()。这个函数在Python3中被重命名替换成了zip()
try:
    from itertools import izip as zip
except ImportError:
    pass

# 在Python3中，Unicode是默认的string类型。
# 如果你做任何和网络相关的操作，你不得不用ASCII/字节字符串来操作，所以代替StringIO，你要io.BytesIO
try:
    from io import BytesIO as StringIO
except ImportError:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO

import xml

g = urlopen('http://python.jobbole.com/81091/')
f = StringIO(g.read())
g.close()

tree = xml.etree.ElementTree.parse(f)
f.close()

for elmt in tree.getiterator():
    if elmt.tag == 'title' and not elmt.text.startswith('Top Stories'):
        printf('- %s' % elmt.text)

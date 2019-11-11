#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("*****Movie*****")
            title = attributes["title"]
            print("Title:", title)

    # 元素结束事件处理
    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print("Stars:", self.stars)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""

    # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


"""
Python 对 XML 的解析
常见的 XML 编程接口有 DOM 和 SAX，这两种接口处理 XML 文件的方式不同，当然使用场合也不同。
Python 有三种方法解析 XML，SAX，DOM，以及 ElementTree:
1.SAX (simple API for XML )
Python 标准库包含 SAX 解析器，SAX 用事件驱动模型，通过在解析XML的过程中触发一个个的事件并调用用户定义的回调函数来处理XML文件。
2.DOM(Document Object Model)
将 XML 数据在内存中解析成一个树，通过对树的操作来操作XML。
3.ElementTree(元素树)
ElementTree就像一个轻量级的DOM，具有方便友好的API。代码可用性好，速度快，消耗内存少。
注：因DOM需要将XML数据映射到内存中的树，一是比较慢，二是比较耗内存，而SAX流式读取XML文件，比较快，占用内存少，但需要用户实现回调函数（handler）。
"""
"""
python使用SAX解析xml
SAX是一种基于事件驱动的 API。
利用SAX解析XML文档牵涉到两个部分: 解析器和事件处理器。
解析器负责读取XML文档，并向事件处理器发送事件，如元素开始跟元素结束事件。
而事件处理器则负责对事件作出响应，对传递的XML数据进行处理。
1、对大型文件进行处理；
2、只需要文件的部分内容，或者只需从文件中得到特定信息。
3、想建立自己的对象模型的时候。
在python中使用sax方式处理xml要先引入xml.sax中的parse函数，还有xml.sax.handler中的ContentHandler。
ContentHandler类方法介绍
characters(content)方法
调用时机：
从行开始，遇到标签之前，存在字符，content 的值为这些字符串。
从一个标签，遇到下一个标签之前， 存在字符，content 的值为这些字符串。
从一个标签，遇到行结束符之前，存在字符，content 的值为这些字符串。
标签可以是开始标签，也可以是结束标签。
startDocument() 方法
文档启动的时候调用。
endDocument() 方法
解析器到达文档结尾时调用。
startElement(name, attrs)方法
遇到XML开始标签时调用，name是标签的名字，attrs是标签的属性值字典。
endElement(name) 方法
遇到XML结束标签时调用。
"""
"""
make_parser方法
以下方法创建一个新的解析器对象并返回。
xml.sax.make_parser( [parser_list] )
参数说明:
parser_list - 可选参数，解析器列表
parser方法
以下方法创建一个 SAX 解析器并解析xml文档：
xml.sax.parse( xmlfile, contenthandler[, errorhandler])
参数说明:
xmlfile - xml文件名
contenthandler - 必须是一个ContentHandler的对象
errorhandler - 如果指定该参数，errorhandler必须是一个SAX ErrorHandler对象
parseString方法
parseString方法创建一个XML解析器并解析xml字符串：
xml.sax.parseString(xmlstring, contenthandler[, errorhandler])
参数说明:
xmlstring - xml字符串
contenthandler - 必须是一个ContentHandler的对象
errorhandler - 如果指定该参数，errorhandler必须是一个SAX ErrorHandler对象

"""

if (__name__ == "__main__"):
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    # parser.parse("movies.xml")
    parser.parse("/home/jiayachong/PycharmProjects/python_test/pythonbase/test20_XML/movies.xml")

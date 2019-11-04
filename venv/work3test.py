
import os
import sys
import logging
import json
import glob
import re
import pathlib
from fastavro import writer, reader, schema
# １
# Python 中的标识符是区分大小写的。
# 以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入。
# 以双下划线开头的 __foo 代表类的私有成员，以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
# Python 可以同一行显示多条语句，方法是用分号 ;

# ２
# IndentationError: unindent does not match any outer indentation level错误表明，你使用的缩进方式不一致，有的是 tab 键缩进，有的是空格缩进，改为一致即可。
#
# 如果是 IndentationError: unexpected indent 错误, 则 python 编译器是在告诉你"Hi，老兄，你的文件里格式不对了，可能是tab和空格没对齐的问题"，所有 python 对格式要求非常严格。
#
# 因此，在 Python 的代码块中必须使用相同数目的行首缩进空格数。
#
# 建议你在每个缩进层次使用 单个制表符 或 两个空格 或 四个空格 , 切记不能混用

path_avro_file='/data/test/classifier/new-type'
files = os.listdir(path_avro_file)
scan_result_lst = []
for file in files:
    file_name = os.path.splitext(file)[0]
    if file_name.count('cell_decision') > 0:
        print(file_name)
        avro_reader = reader(open(file_name, "rb"))
    else:
        avro_reader = None

    print(avro_reader)
    for scan_result in avro_reader:
        scan_result_lst.append(scan_result)

    print(os.path.splitext(file)[0])

    # if os.path.isfile(file):
    #     file_name = os.path.splitext(file)[0]
    #
    #
w=0
e=3
q=w+e
print(q)
print("""
---------1---------文件IO-----------------输入输出-------------------------------------------
输出方法:例如print()
""")
#!/usr/bin/python
# -*- coding: UTF-8 -*-
print("---多参数打印－－－拼接成一个支付窜打印－－－－")
print("Python 是一个非常棒的语言，不是吗？","3333","eddf","ggggfffffffffffffffddddddd")


print("""
输入方法：
raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）：
input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
""")


#!/usr/bin/python
# -*- coding: UTF-8 -*-
print("""
命令行执行：
－－－－－－－－－－－－－－－
str = raw_input("请输入：")
print("你输入的内容是: ", str)
－－－－－－－－－－－－－－－－－－－－
>>> input("请输入:")
请输入:[x*5 for x in range(2,10,2)]
[10, 20, 30, 40]
>>> 
""")

print("""
------2-------------------读写实际的数据文件－－－－－－－－－－－－－－－－－－－－－－－
open 函数：
你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写
file object = open(file_name [, access_mode][, buffering])

""")
#!/usr/bin/python
# -*- coding: UTF-8 -*-

print("------------打开一个文件-------------------")
fo = open("/home/jiayachong/avrome/tmp/test.txt", "a+")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)
# print("末尾是否强制加空格 : ", fo.softspace)

print("""
File 对象的 close（）方法刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入
""")
print("""--------------------------open函数－－－－－－－－－－－－－－－－－
file object = open(file_name [, access_mode][, buffering])
1.file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
2.access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
3.buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

access_mode:
t	文本模式 (默认)。
x	写模式，新建一个文件，如果该文件已存在则会报错。
b	二进制模式。
+	打开一个文件进行更新(可读可写)。
U	通用换行模式（不推荐）。
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。


""")


print("---write-----")
fo.write(" test write method !!!")


print("""
---------------read()  方法－－－－－－fileObject.read([count])－－－－－－－－－－
如果没有传入count，它会尝试尽可能多地读取更多的内容，很可能是直到文件的末尾。被传递的参数是要从已打开文件中读取的字节计数

""")
str=fo.read()
print(str)
fo.close()

fo2 = open("/home/jiayachong/avrome/tmp/test.txt", "r+")
print(fo2.read(66))
print("------------------------文件定位－－－－－－－－－－－－－－－－－－－－－－－")

print("""
---------------tell() 方法方法告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后。＝＝＝
－－－－－－－－－seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。

""")

# 打开一个文件
fo = open("/home/jiayachong/avrome/tmp/test.txt", "r+")
str = fo.read(10)
print("读取的字符串是 : ", str)

# 查找当前位置
position = fo.tell()
print("当前文件位置 : ", position)

# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read(10)
print("重新读取字符串 : ", str)
# 关闭打开的文件
fo.close()

print("""----------------os.rename(current_file_name, new_file_name)-------
-----------new_file_name文件和current_file_name文件不在一个文件夹中，则复制－－－－
－－－－－－－new_file_name文件和current_file_name文件在一个文件文件中，则是重命名－－－－
----""")

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

# 重命名文件test1.txt到test2.txt。
os.rename( "/home/jiayachong/avrome/tmp/test.txt", "/home/jiayachong/avrome/test.txt" )

# os.remove("/home/jiayachong/avrome/tmp/test2.txt")


print("""----------------------python中的目录－－－－－－－－－－－－－－－－－－－－－－－－－－－－
所有文件都包含在各个不同的目录下，不过Python也能轻松处理。os模块有许多方法能帮你创建，删除和更改目录。
""")

# os.mkdir("/home/jiayachong/avrome/tmp/testmakdir")

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

# 将当前目录改为"/home/newdir"
# os.chdir("/home/newdir")

print("""
getcwd()方法：
getcwd()方法显示当前的工作目录。
""")
print(os.getcwd())


print("""
chdir()方法
可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。
""")


print("""----------------------删除目录－－－在删除这个目录之前，它的所有内容应该先被清除。－－－－－－－
rmdir()方法
rmdir()方法删除目录，目录名称以参数传递。
在删除这个目录之前，它的所有内容应该先被清除。
""")
# os.rmdir('/home/jiayachong/PycharmProjects/python_test/pythonlearn/testdir/test1')

print(""" ------------------删除文件－－－－－－os.remove() 方法用于删除指定路径的文件。如果指定的路径是一个目录，将抛出OSError－－－－
os.remove(path)
""")


print("""
File 对象和 OS 对象提供了很多文件与目录的操作方法           
""")

print("---------------调整当前所在的文件件为指定的目录下－－－－－－－－－－")
print(os.getcwd())
#　指定的目录必须是已经存在的目录，否则会报错－－－
# os.chdir("/home/jiayachong/PycharmProjects/python_test/pythonlearn/testdir/test1")
print(os.getcwd())


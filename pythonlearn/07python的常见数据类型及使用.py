print("==1======================列表（序列）的特征===============================================================")
print(""" ---------Python有6个序列的内置类型，但最常见的是列表和元组-------------
----------------Python已经内置确定序列的长度以及确定最大和最小的元素的方法----------
1.有序有下标
2.序列都可以进行的操作包括索引，切片，加，乘，检查成员。
3.数据类型可不同
－－－－－－－－创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可－－－－－－－－－
""")


# 访问列表中的值
# 使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符，如下所示：
#
# 实例(Python 2.0+)
#!/usr/bin/python

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print("------------序列的值如何获取--------1.通过下标----2.通过截取获取子序列")
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])


print("------------序列的值如何添加元素--------append-----")
print("------------删除元素--------del(list1[2])-----")

#!/usr/bin/python

list1 = ['physics', 'chemistry', 1997, 2000]

print(list1)
del(list1[2])
print("After deleting value at index 2 : ")
print(list1)

print("------------------序列的加乘操作符,判断是否存在,迭代-------------------------------------")
print("""
Python 表达式	结果	       描述
len([1, 2, 3])	3	长度
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合
['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
3 in [1, 2, 3]	True	元素是否存在于列表中
for x in [1, 2, 3]: print x,	1 2 3	迭代
""")

print("===================列表截取=================================")
print("""
L[2]	'Taobao'	读取列表中第三个元素
L[-2]	'Runoob'	读取列表中倒数第二个元素
L[1:]	['Runoob', 'Taobao']	从第二个元素开始截取列表
""")

print("==================列表函数&方法===================")
print("""=========Python包含以下函数:============
1	cmp(list1, list2)
比较两个列表的元素
2	len(list)
列表元素个数
3	max(list)
返回列表元素最大值
4	min(list)
返回列表元素最小值
5	list(seq)
将元组转换为列表
""")
print("""===========Python包含以下方法:======
1	list.append(obj)
在列表末尾添加新的对象
2	list.count(obj)
统计某个元素在列表中出现的次数
3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素
9	list.sort(cmp=None, key=None, reverse=False)
对原列表进行排序
""")

print("===2=====================元组===============================================================")
print("""
1.元组使用小括号，列表使用方括号。
2.元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

""")
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
print(tup3)

tup4 = (50,)
print(tup4)
print("元组中只包含一个元素时，需要在元素后面添加逗号")
tuperr=(50) #不是元组
print(tuperr)


print("--------------访问元组－－－－－－－－－")
#!/usr/bin/python

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

print("-----------元组中元素不可修改－－但可以对元组进行链接组合－－")
#!/usr/bin/python
# -*- coding: UTF-8 -*-

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

print("----------元组中的元素不可删除－－－－－元组可以删除－－－－－－－－－")
#!/usr/bin/python

tup = ('physics', 'chemistry', 1997, 2000)

print(tup)
del(tup)
print("After deleting tup : ")
# print(tup)

print("""----------------加减，判断，迭代－－可以组合和复制，运算后会生成一个新的元组－
与字符串一样，元组之间可以使用 + 号和 * 号进行运算。
Python 表达式	结果	描述
len((1, 2, 3))	3	计算元素个数
(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接
('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
3 in (1, 2, 3)	True	元素是否存在
for x in (1, 2, 3): print x,	1 2 3	迭代
""")

print("""
-----------------------------元组索引，截取------------------
Python 表达式	结果	描述
L[2]	'SPAM!'	读取第三个元素
L[-2]	'Spam'	反向读取，读取倒数第二个元素
L[1:]	('Spam', 'SPAM!')	截取元素
""")

#!/usr/bin/python
print("""
无关闭分隔符
任意无符号的对象，以逗号隔开，默认为元组，如下实例：
""")
print('abc', -4.24e93, 18+6.6j, 'xyz')
x, y = 1, 2
print("Value of x , y : ", x,y)

print("------------------元组内置函数----------------------")
print("""
1	cmp(tuple1, tuple2)
比较两个元组元素。
2	len(tuple)
计算元组元素个数。
3	max(tuple)
返回元组中元素最大值。
4	min(tuple)
返回元组中元素最小值。
5	tuple(seq)
将列表转换为元组。
""")


print("===３========字典============================================================================")
print("""
格式：
    每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 
特点：
键唯一，如果定义重复，后面的会替换掉前面的--------同一个键被赋值两次，后一个值会被记住
dict={"a":"11","b":"22","b":"23"}
dict[b]
""")
dict={"a":"11","b":"22","b":"23","b":"24"}
print(dict["b"])
print("===================")#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# print("dict['Alice'?]: ", dict['Alice'])

#!/usr/bin/python
print("---------更新和添加，有则更新，无则添加------")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8 # 更新
dict['School'] = "RUNOOB" # 添加
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])


print("""---------删除－－－－－－
能删单一的元素也能清空字典，清空只需一项操作。
显示删除一个字典用del命令，如下实例：
""")
#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name']  # 删除键是'Name'的条目
print("dict['Age']: ", dict['Age'])
# print("dict['School']: ", dict['School'])

print("--------清空字典所有条目--------")
dict.clear()      # 清空字典所有条目
print(dict)

print("--------删除-----字典--------")
del dict          # 删除字典
print(dict)

print("--------------键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行，如下实例：-----")

#!/usr/bin/python
# dict = {['Name']: 'Zara', 'Age': 7}
# print("dict['Name']: ", dict['Name'])
# print(dict["Name"])
print("---键是数字－－－")
dictww = {'Age': 7,8:999}
print(dictww[8])

print("----内置函数＆方法－－－－－")
print("""
1	cmp(dict1, dict2)
比较两个字典元素。
2	len(dict)
计算字典元素个数，即键的总数。
3	str(dict)
输出字典可打印的字符串表示。
4	type(variable)
返回输入的变量类型，如果变量是字典就返回字典类型。
""")


print(str(dictww))

print(type(dictww))     # --打印出来字典类型　　－－<class 'dict'>

print("""
Python字典包含了以下内置方法：

序号	函数及描述
1	dict.clear()
删除字典内所有元素
2	dict.copy()
返回一个字典的浅复制
3	dict.fromkeys(seq[, val])
创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
4	dict.get(key, default=None)
返回指定键的值，如果值不在字典中返回default值
5	dict.has_key(key)
如果键在字典dict里返回true，否则返回false
6	dict.items()
以列表返回可遍历的(键, 值) 元组数组
7	dict.keys()
以列表返回一个字典所有的键
8	dict.setdefault(key, default=None)
和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	dict.update(dict2)
把字典dict2的键/值对更新到dict里
10	dict.values()
以列表返回字典中的所有值
11	pop(key[,default])
删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
12	popitem()
返回并删除字典中的最后一对键和值。
""")


print(dictww.copy())

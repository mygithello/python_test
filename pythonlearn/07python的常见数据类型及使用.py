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
print("=======================================================================================")
print("=======================================================================================")
print("=======================================================================================")
print("=======================================================================================")
print("=======================================================================================")
print("=======================================================================================")
print("=======================================================================================")
print("=======================================================================================")
print("=======================================================================================")
print("=======================================================================================")
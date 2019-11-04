# 实例(Python 2.0+)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from cursor import cursor

print("-----------通过【：】的取子窜的用法")
var1 = 'Hello World!'
print("输出 :- ", var1[:6] + 'Runoob!')

print("======================Python 转义字符＝＝＝＝＝＝＝＝")

# 在需要在字符中使用特殊字符时，python 用反斜杠 \ 转义字符。如下表：
#
# 转义字符	描述
#    \(在行尾时)	续行符
#  \\	反斜杠符号
#     \'	单引号
#     \"	双引号
#     \a	响铃
#     \b	退格(Backspace)
#     \e	转义
#     \000	空
#     \n	换行
#     \v	纵向制表符
#     \t	横向制表符
#     \r	回车
#     \f	换页
# \oyy	八进制数，yy代表的字符，例如：\o12代表换行
# \xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
# \other	其它的字符以普通格式输出


print("========================字符窜运算符========================================")
# Python字符串运算符
# 下表实例变量 a 值为字符串 "Hello"，b 变量值为 "Python"：
#
# 操作符	描述	实例
print("""
+	字符串连接
>>>a + b
'HelloPython'
*	重复输出字符串
>>>a * 2
'HelloHello'
[]	通过索引获取字符串中字符
>>>a[1]
'e'
[ : ]	截取字符串中的一部分
>>>a[1:4]
'ell'
in	成员运算符 - 如果字符串中包含给定的字符返回 True
>>>"H" in a
True
not in	成员运算符 - 如果字符串中不包含给定的字符返回 True
>>>"M" not in a
True
r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
>>>print r'\n'
\n
>>> print R'\n'
\n
%	格式字符串	请看下一章节
""")
print("----------------------------test -----------------")

#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if( "H" in a) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")

if( "M" not in a) :
    print("M 不在变量 a 中")
else :
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')

print("""
Python 字符串格式化
Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。

在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。

如下实例：
""")


#!/usr/bin/python
print("-------前后数量一致，字符窜用％ｓ,数字用％ｄ-------------------")
print("My name is %s and weight is %d kg!%d" %('Zara',2122,333) )
print("""
python 字符串格式化符号:

    符   号	描述
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %F 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
""")

print("""
格式化操作符辅助指令:

符号	功能
*	定义宽度或者小数点精度
-	用做左对齐
+	在正数前面显示加号( + )
<sp>	在正数前面显示空格
#	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0	显示的数字前面填充'0'而不是默认的空格
%	'%%'输出一个单一的'%'
(var)	映射变量(字典参数)
m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
""")

s2="dddaaa"
s2.format()#-----------------?????????????

print("""==============三引号===============================================================

三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。

一个典型的用例是，当你需要一块HTML或者SQL时，这时当用三引号标记，使用传统的转义字符体系将十分费神。
""")

errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
cursor.execute('''
CREATE TABLE users (  
login VARCHAR(8), 
uid INTEGER,
prid INTEGER)
''')
print("""-------------１----------------------python 标准异常－－－－－－－－－－－－－－－－－－－－－－－
异常名称	描述
BaseException	所有异常的基类
SystemExit	解释器请求退出
KeyboardInterrupt	用户中断执行(通常是输入^C)
Exception	常规错误的基类
StopIteration	迭代器没有更多的值
GeneratorExit	生成器(generator)发生异常来通知退出
StandardError	所有的内建标准异常的基类
ArithmeticError	所有数值计算错误的基类
FloatingPointError	浮点计算错误
OverflowError	数值运算超出最大限制
ZeroDivisionError	除(或取模)零 (所有数据类型)
AssertionError	断言语句失败
AttributeError	对象没有这个属性
EOFError	没有内建输入,到达EOF 标记
EnvironmentError	操作系统错误的基类
IOError	输入/输出操作失败
OSError	操作系统错误
WindowsError	系统调用失败
ImportError	导入模块/对象失败
LookupError	无效数据查询的基类
IndexError	序列中没有此索引(index)
KeyError	映射中没有这个键
MemoryError	内存溢出错误(对于Python 解释器不是致命的)
NameError	未声明/初始化对象 (没有属性)
UnboundLocalError	访问未初始化的本地变量
ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError	一般的运行时错误
NotImplementedError	尚未实现的方法
SyntaxError	Python 语法错误
IndentationError	缩进错误
TabError	Tab 和空格混用
SystemError	一般的解释器系统错误
TypeError	对类型无效的操作
ValueError	传入无效的参数
UnicodeError	Unicode 相关的错误
UnicodeDecodeError	Unicode 解码时的错误
UnicodeEncodeError	Unicode 编码时错误
UnicodeTranslateError	Unicode 转换时错误
Warning	警告的基类
DeprecationWarning	关于被弃用的特征的警告
FutureWarning	关于构造将来语义会有改变的警告
OverflowWarning	旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning	关于特性将会被废弃的警告
RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
SyntaxWarning	可疑的语法的警告
UserWarning	用户代码生成的警告
""")



print("""-------------------------2------------------------------异常概念－－－－－－－－－－－－－
异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。
一般情况下，在Python无法正常处理程序时就会发生一个异常。
异常是Python对象，表示一个错误。
当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行。
""")


print("""------------------3-----------------捕获异常的语法－－－－－－－－－
捕捉异常可以使用try/except语句。
""")

print("""

try:
    <语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
""")

import os
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# chmod -w testfile   #去除当前文件的写权限
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    os.remove("testfile")
    fh.close()

print("""-------4-----------except 不带任何异常，默认接收所有的异常类型－－－－－
使用except而不带任何异常类型
eg:

try:
    正常的操作
   ......................
except:
    发生异常，执行这块代码
   ......................
else:
    如果没有异常执行这块代码
""")

print("""-----------5--------------------try-finally 语句----一定会执行的代码-------------------------
try-finally 语句无论是否发生异常都将执行最后的代码。退出try时总会执行

try:
<语句>
finally:
<语句>    #退出try时总会执行
raise　　　　#Python中的raise 关键字用于引发一个异常，基本上和C#和Java中的throw关键字相同，如下所示：
""")

#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
finally:
    print("－－－－会定会执行－－－finally---代码")
    fh.close()


print("""
----------------------6--------try 块的嵌套使用－－－－－－－－－－－－－－－－－－
""")

#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile", "r")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print("关闭文件------------------------")
        fh.close()
except IOError:
    print("Error: 没有找到文件或读取文件失败")

print("""
-----------7--------使用except而带多种异常类型-----------------同时匹配多个异常，执行相同的一块代码
发生以上多个异常中的一个，执行这块代码
""")
def ThrowErr(i):
    if i>2:
        print("---通过raise新建了一个异常－－－－－")
        raise Exception("这个是个测试raise和测试fianlly的异常参数－－－－－－")
    else:
        print("---通过raise新建了一个异常－－－2－－")
        raise NameError("这个是个测试raise和测试fianlly的异常参数－－－2－－－","3332222")

try:
    ThrowErr(3)
except (NameError,Exception):  #通过as的方法，接收到异常的参数
    print("-----------测试捕获到该异常了－－－－－except(Exception1[, Exception2[,...ExceptionN]]]):－－－－－－－－－－－－")


print("""
-----------8------定义接收异常参数-------------------------------------------

""")

try:
    ThrowErr(3)
except Exception as para:
    print("this is para: "+str(para))


print("""
----------9-------------------创建异常--------------------------------------------
异常应该是典型的继承自Exception类，通过直接或间接的方式
""")
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

# 触发自定义的异常
try:
    raise Networkerror("Bad hostname")
except Networkerror as e:
    print(e.args)


#删除测试文件
fh = open("testfile", "w")
os.remove("testfile")
fh.close()
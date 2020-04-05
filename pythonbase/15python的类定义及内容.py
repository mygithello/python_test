#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)
"""
empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。
第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
"""

"""
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
"""
print("------1----------根据类创建对象－－－－－－类的实例化类似函数调用方式－－需要注意参数－－－－－－－－－－")
print("=======测试类变量的效果========")
e =Employee("xiaoming",19)
e.displayCount()
print("------创建的对象调用方法－－－－－－－－")
e =Employee("xiaoming2",13)
e.displayCount()

print("------访问累变量－通过类名/实例－－进行访问－－－")
print(e.empCount)
print(Employee.empCount)


print("------------------修改类的属性－－－－－－－")
print("----添加")
e.age = 7  # 添加一个 'age' 属性
print(e.age)

e.age = 8  # 修改 'age' 属性

print(e.age)
# del e.age  # 删除 'age' 属性
# print(e.age)


print("""-----－－---通过python的内置函数访问类的属性---------------------------------
getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) : 检查是否存在一个属性。getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) : 检查是否存在一个属性。
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) : 删除属性。
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) : 删除属性。
""")
emp1=e
print("--------------")
print(hasattr(emp1, 'age'))    # 如果存在 'age' 属性返回 True。
print(getattr(emp1, 'age'))    # 返回 'age' 属性的值
print(setattr(emp1, 'age', 8)) # 添加属性 'age' 值为 8
delattr(emp1, 'age')    # 删除属性 'age'


print("""
-------------２-------------python的内置类属性－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）

""")
emp1.age=99
print("--------------------打印类的属性－－－－－－－－－－－")
print(emp1.__dict__)
print(emp1.__doc__)
print(emp1.__module__)


print("-------------３---------------------python对象销毁－－－－－垃圾回收－－－－－－－－－－－－－")
"""
记录对象有多少引用－－－－－－
一个内部跟踪变量，称为一个引用计数器
"""
a = 40      # 创建对象  <40>
b = a       # 增加引用， <40> 的计数
c = [b]     # 增加引用.  <40> 的计数

del a       # 减少引用 <40> 的计数
b = 100     # 减少引用 <40> 的计数
c[0] = -1   # 减少引用 <40> 的计数

print("""－－－－－－４－－－－－－－－－－－_del_－－方法的调用－－－－－－－－－－－－－－－－－－－－
析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行：
""")
#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Point:
    def __init__( self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "销毁")
pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))# 打印对象的id
del pt1
del pt2
del pt3

print("""
---------４--------继承－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
继承创建的新类称为子类或派生类，被继承的类称为基类、父类或超类。
class 派生类名(基类名)

在python中继承中的一些特点：
1、如果在子类中需要父类的构造方法就需要显示的调用父类的构造方法，或者不重写父类的构造方法。详细说明可查看：python 子类继承父类构造函数说明。
2、在调用基类的方法时，需要加上基类的类名前缀，且需要带上 self 参数变量。区别在于类中调用普通函数时并不需要带上 self 参数
3、Python 总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。
class SubClassName (ParentClass1[, ParentClass2, ...]):

""")

#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Parent:        # 定义父类
    parentAttr = 100
    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性 :", Parent.parentAttr)

class Child(Parent): # 定义子类
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print('调用子类方法')

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法 - 设置属性值
c.getAttr()          # 再次调用父类的方法 - 获取属性值


print("""
class A:        # 定义类 A
.....
class B:         # 定义类 B
.....
class C(A, B):   # 继承类 A 和 B
.....
""")
class A:
    def testA(self):
        print("this is testA!!!")

    def testB(self):
        print("this is testB!!!A")
class B:
    def testB(self):
        print("this is testB!!!B")
class C(B,A):
    def testC(self):
        print("this is testC!!!!")

c=C()
c.testA()
c.testB()

print("""
--------------5-----------------------类中基本构造方法-------------------------------------------
序号	方法, 描述 & 简单的调用
1	__init__ ( self [,args...] )
构造函数
简单的调用方法: obj = className(args)
2	__del__( self )
析构方法, 删除一个对象
简单的调用方法 : del obj
3	__repr__( self )
转化为供解释器读取的形式
简单的调用方法 : repr(obj)
4	__str__( self )
用于将值转化为适于人阅读的形式
简单的调用方法 : str(obj)
5	__cmp__ ( self, x )
对象比较
简单的调用方法 : cmp(obj, x)
""")

print("""
------------6---------------运算符重载-----------------------------------------
""")
#!/usr/bin/python

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)
v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1 + v2)

print("""
--------------7------------类的属性和方法-----------------------------------------
类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
类的方法
在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数
类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用 self.__private_methods
""")


# !/usr/bin/python
# -*- coding: UTF-8 -*-

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)
        return self.__secretCount

counter = JustCounter()
counter.count()

print(counter.publicCount)
print(counter.count())
# print(counter.__secretCount)
  # 报错，实例不能访问私有变量


#!/usr/bin/python
# -*- coding: UTF-8 -*-
print("""
Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName（ 对象名._类名__私有属性名 ）访问属性
""")
class Runoob:
    __site = "www.runoob.com"

runoob = Runoob()
print(runoob._Runoob__site)

print("""
单下划线、双下划线、头尾双下划线说明：
__foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
_foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
__foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
""")

# super()
#在⼦类的⽅法⾥调⽤⽗类的⽅法，使⼦类的⽅法可以在继承⽗类⽅法的基础上进⾏扩展































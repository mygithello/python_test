

class A:
    pass

class B(A):
    pass

print(isinstance(A(), A))    # returns True
print(type(A()) == A)       # returns True
print(isinstance(B(), A))    # returns True
print(type(B()) == A)      # returns False


"""
isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。

isinstance() 与 type() 区别：
type() 不会认为子类是一种父类类型，不考虑继承关系。
isinstance() 会认为子类是一种父类类型，考虑继承关系。
如果要判断两个类型是否相同推荐使用 isinstance()。

isinstance(object, classinfo)

object -- 实例对象。
classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。
返回值
如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False。

"""
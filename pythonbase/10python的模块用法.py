from imp import reload

print("=====１===模块的概念及规里面的内容=============")
print("---模块能定义函数，类和变量，模块里也能包含可执行的代码---")

print("========模块=====如何导入模块============")
print("-----import module1[, module2[,... moduleN]]------")

print("---from modname import name1[, name2[, ... nameN]]－－－－－")

print("""
from…import* 语句
把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
""")


print("=====2===模块======引入模块后，是如何查找到用到的文件的====程序搜索查找的顺序=======")
print("""
当你导入一个模块，Python 解析器对模块位置的搜索顺序是：
1、当前目录
2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。
模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录
""")


print("""
-------3----------------命名空间和作用域-------------------局部命名空间和全局命名空间－－－－－－－－－－－－－－－－－
1.则局部变量会覆盖全局变量。
2.类的方法的作用域规则和通常函数的一样
3.如果要给函数内的全局变量赋值，必须使用 global 语句

""")

#!/usr/bin/python
# -*- coding: UTF-8 -*-
print("---global VarName 的表达式会告诉 Python， VarName 是一个全局变量，这样 Python 就不会在局部命名空间里寻找这个变量了---")
Money = 2000
def AddMoney():
    # 想改正代码就取消以下注释:
    global Money #操作全局变量
    Money = Money + 1

print(Money)
AddMoney()
print(Money)


print("----4-------dir()函数------查看模块下的变量和函数－－－－－－－－－－－－－－－")

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 导入内置math模块
import math

content = dir(math)

print(content);

print("在这里，特殊字符串变量__name__指向模块的名字，__file__指向该模块的导入文件名。")


print("""----5－－－－查看指定位置能访问的全局命名空间的名字或局部命名空间的名字-------------globals() 和 locals() 函数------------
根据调用地方的不同，globals() 和 locals() 函数可被用来返回全局和局部命名空间里的名字。
如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。
如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。
两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取。
""")


print("""－－6－－－－－－重新加载模块－－－－－－－－reload(module_name)－－－－－－－
""")

reload(math)





print("-------7-----------python中的包，－－python的应用环境－－一个由模块及子包，和子包下的子包等组成－---------------")
print(""""
------简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。__init__.py 用于标识当前文件夹是一个包
""")
print("""-----包结构
test.py
package_runoob
|-- __init__.py
|-- runoob1.py
|-- runoob2.py
""")

print(""" ----------定义自定义的包－－－－－－test_package－－－－
只在每个文件里放置了一个函数，但其实你可以放置许多函数。你也可以在这些文件里定义Python的类，然后为这些类建一个包
""")

#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 导入 引入自定义的 包

print("--------引入自定义的包----------------------")

# 导入 Phone 包
from test_package.test_file1 import method_test1
from test_package.test_file2 import method_test2
print("--------调用自定义的包----------------------")
method_test1()
method_test2()




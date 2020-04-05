print("""
--------１----------------------定义一个函数-------------------------------------
你可以定义一个由自己想要功能的函数，以下是简单的规则：
函数的特点：
1.函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
2.任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
3.函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
4.函数内容以冒号起始，并且缩进。
5.return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
""")

print("""
常用函数使用：

""")

# def functionname( parameters ):
#     "函数_文档字符串"
#     function_suite
#     return [expression]

def printme( str ):
    "打印传入的字符串到标准显示设备上"
    print(str)
    return
print("--------------2-----------调用函数-------------------------")
printme("my printme test!")


print("""
--------------3------------在 python 中，类型属于对象，变量是没有类型的：-------------------------

a=[1,2,3]
 
a="Runoob"
以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是 List 类型对象，也可以指向 String 类型对象。
""")

print("""--------------------------------值传递还是引用传递－－－即－－－传不可变对象和传可变对象－－－－－－－－－－
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象
""")

#!/usr/bin/python
# -*- coding: UTF-8 -*-
print("----------------不可变传递－－－－－－－－")
def ChangeInt( a ): #当接受到参数，是接受到一个值，用一个方法内飞引用指向这个值，此处是对个这个方法内的引用的值赋值
    a = 10

b = 2
ChangeInt(b)
print(b) # 结果是 2

print("------------------可变对象传递实例－－－－－－")

#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 可写函数说明
def changeme( mylist ):#此列接收的参数是个引用，当做修改时，直接是对引用对应的值进行了修改
    "修改传入的列表"
    mylist.append([1,2,3,4]);
    print("函数内取值: ", mylist)
    return

# 调用changeme函数
mylist = [10,20,30];
changeme( mylist );
print("函数外取值: ", mylist)

print("----参数1－－－调用参数必须和声明的参数一样－－－－也就是小括号里面声明的参数－")
print("----参数2－－－键字参数允许函数调用时参数的顺序与声明时不一致－－－－也就是才调用的时候指明参数名和参数值－")



print("--------------------默认参数－－－－方法形参内定义参数名和默认值，如果没有接收到该参数，方法就使用事先定义的默认值－－－－－－－－－－－－－－－－－－")
#!/usr/bin/python
# -*- coding: UTF-8 -*-

#可写函数说明
def printinfo( name, age = 35 ):
    "打印任何传入的字符串"
    print("Name: ", name);
    print("Age ", age);
    return;

#调用printinfo函数
printinfo( age=50, name="miki" );
printinfo( name="miki" );

print("""
－－－－－－－－－－－－－－－不定长参数－－－－能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数－－－－－－－－－－－－
""")

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print("输出: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return;

# 调用printinfo 函数
printinfo( 10 );
printinfo( 70, 60, 50 );

print("---------------------匿名函数－－－－－－－－－－－－")
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 可写函数说明
print("---lambda 语法只包含一个语句－－－－－－lambda [arg1 [,arg2,.....argn]]:expression")
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print("相加后的值为 : ", sum( 10, 20 ))
print("相加后的值为 : ", sum( 20, 20 ))
print("----------------------------------------------------")



#!/usr/bin/python
# -*- coding: UTF-8 -*-
print("-------------------return 语句接受返回值－－－－－－－－")
# 可写函数说明
def sum( arg1, arg2 ):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total;

# 调用sum函数
total = sum( 10, 20 );

print("函数外：　"+str(total))

print("---------变量的作用域－－－局部变量和全局变量－－－－－－－－")
#!/usr/bin/python
# -*- coding: UTF-8 -*-

total = 0; # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2; # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total;

#调用sum函数
sum( 10, 20 );
print("函数外是全局变量 : ", total)



print("python　的数据类型转换函数：str(),int(),float(),list()")

print(float(3.43))
print(type(float(3.43)))

a='list()函数的使用，把数据转换成列表类型'
print(list(a))
print(type(list(a)))





















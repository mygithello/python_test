# 指定任何非0和非空（null）值为true，0 或者 null为false。

#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 例2：elif用法

num = 5
if num == 3:            # 判断num的值
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num < 0:           # 值小于零时输出
    print('error')
else:
    print ('roadman')    # 条件均不成立时输出

#!/usr/bin/python
# -*- coding: UTF-8 -*-
print("""
# 例3：if语句多个条件
由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
""")


num = 9
if num >= 0 and num <= 10:    # 判断值是否在0~10之间
    print('hello')
# 输出结果: hello

num = 10
if num < 0 or num > 10:    # 判断值是否在小于0或大于10
    print('hello')
else:
    print('undefine')
# 输出结果: undefine

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print('hello')
else:
    print('undefine')
# 输出结果: undefine



#!/usr/bin/python
# -*- coding: UTF-8 -*-

var = 100

if ( var  == 100 ) : print("变量 var 的值为100")

print("Good bye!")

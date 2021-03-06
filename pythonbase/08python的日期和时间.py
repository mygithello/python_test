# 时间间隔是以秒为单位的浮点小数

print("==============time 和 calendar 模块可以用于格式化日期和时间==================")

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time;  # 引入time模块

ticks = time.time()
print("当前时间戳为:", ticks)
print("---时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年。----")


print("""---------------时间元组标示时间－－－－－－－－－－
上述也就是struct_time元组。这种结构具有如下属性：
序号	属性	值
0	tm_year	2008
1	tm_mon	1 到 12
2	tm_mday	1 到 31
3	tm_hour	0 到 23
4	tm_min	0 到 59
5	tm_sec	0 到 61 (60或61 是闰秒)
6	tm_wday	0到6 (0是周一)
7	tm_yday	1 到 366(儒略历)
8	tm_isdst	-1, 0, 1, -1是决定是否为夏令时的旗帜
""")

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)


print("""
----------------------获取格式化的时间-------------
可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
""")
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

localtime = time.asctime( time.localtime(time.time()) )   #----转换成常见的可读格式
print("本地时间为 :", localtime)

print("""-----------------时间在不同格式间的转换－－－－－－－－－－－－－
用 time 模块的 strftime 方法来格式化日期，
""")

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))


print("""
------------------python中时间日期格式化符号：-------------
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
""")

print("""
-------------------------获取某月日历---------------------------------
Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历
""")
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import calendar

cal = calendar.month(2016, 2)
print("以下输出2016年1月份的日历:")
print(cal)

print("=======================================================================================")
print("=======================================================================================")
print("=======================================================================================")
print("=======================================================================================")
print("=======================================================================================")
print("=======================================================================================")
print("=======================================================================================")
print("=======================================================================================")



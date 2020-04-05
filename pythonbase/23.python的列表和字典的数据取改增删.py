

#1.python可列表取值：

listv = ['松','竹','梅']
print(listv[1])

#2.python的列表元素的修改

listv[0] = '松树'
print(listv)

#3.python的列表元素的增加
listv.append('梅')
print(listv)

#4.python列表中元素的删
del listv[0]
print(listv)

#5.列表的切⽚（即列表层⾯的提取，⼀次提取若⼲个元素）   x:y    取　　x <= m < y
print(str(5)+':')
print(listv[:])
print(listv[:1])
print(listv[1:2])

#6.列表的修改
#同样是使⽤赋值语句，注意是对列表的
listv[:]=['新修改']
print(listv)

print('7:')
#7.列表的增加
list1 = ['松']
list2 = ['竹']
list3 = ['梅']
list４ = list1 + list2 +list3
print(list４)

#8.列表的删除(通过列表的切片删除切面列表内容)
del list４[:2]
print(list４)

print("＝＝＝＝＝＝＝列表　上=========================================================字典　　下＝＝＝＝")
#9.字典数据的提取(通过字典的key取值)
group = {'师父':'唐三藏', '大师兄':'孙行者', '二师兄':'猪八戒', '沙师弟':'沙和尚'}
print(group['师父'])


#10.字典数据的修改(通过字典的key赋值)
group['师父']='唐玄奘'
print(group)

#11.字典数据的增加(直接定义字典新增的key 和value)
group['白龙马']='敖烈'
print(group)

print("12:")

#12.字典数据的删除
del group['白龙马']
print(group)

#13.dict.keys(),dict.values(),dict.items()
#提取字典中所有的键,值,键值对. #这几种转换，其结果都是元组类型

print("13:")
group = {'师父':'唐三藏', '大师兄':'孙行者', '二师兄':'猪八戒', '沙师弟':'沙和尚'}
keys=group.keys()
print(keys)
#通过list()函数将元组转化为列表的形式
print(list(keys))

print(list(group.values()))
print(list(group.items()))


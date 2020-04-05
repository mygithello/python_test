import sys

from pip._vendor.distlib.compat import raw_input

print("""
break 语句	在语句块执行过程中终止循环，并且跳出整个循环
continue 语句	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
pass 语句	pass是空语句，是为了保持程序结构的完整性。
""")
#* queen problem with recurison
BOARD_SIZE = 8

def under_attack(col, queens):
    left = right = col
    for r, c in reversed(queens):
        #左右有冲突的位置的列号
        left, right = left - 1, right + 1

        if c in (left, col, right):
            return True
    return False

def solve(n):
    if n == 0:
        return [[]]

    smaller_solutions = solve(n - 1)

    return [solution+[(n,i+1)]
            for i in range(BOARD_SIZE)
            for solution in smaller_solutions
            if not under_attack(i+1, solution)]
for answer in solve(BOARD_SIZE):
    print(answer)


def deduplication(self, nums):#找出排序数组的索引
    for i in range(len(nums)):
        if nums[i]==self:
            return i
    i=0
    for x in nums:
        if self>x:
            i+=1
    return i
print("#查找列表里面是否有给指定的元素，有则返回改元素的首次下标，没有则返回小于给定值的元素个数")
print(deduplication(3, [1,3,5,6]))

print("-------------------------------------------")
for ss in range(BOARD_SIZE):
    print(ss)

print("=========while=========list.pop()===============test===每次取出一个元素=======")
list =[1,2,3,4,5,3,3,9]
while len(list)>0:
    item=list.pop()
    print("取出元素"+str(item))
    print(list)

# print("无限循环－－－－－－－－－－－")
# var = 1
# while var == 1 :  # 该条件永远为true，循环将无限执行下去
#     num = raw_input("Enter a number  :")
#     print("You entered: ", num)
# print("Good bye!")

print("# continue 和 break 用法")

i = 1
while i < 10:
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print(i)         # 输出双数2、4、6、8、10
print("---------------")
i = 1
while 1:            # 循环条件为1必定成立
    print(i)     # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break

print("--------for-----------循环＝＝＝遍历元素＝＝＝＝＝# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。＝＝＝＝＝＝＝＝＝＝＝＝")
# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
#
# 语法：
#
# for循环的语法格式如下：
#
# for iterating_var in sequence:
#     statements(s)

#!/usr/bin/python
# -*- coding: UTF-8 -*-

for letter in 'Python':     # 第一个实例
    print('当前字母 :', letter),

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
    print('当前水果 :', fruit)

print("Good bye!")


print("============循环嵌套==========print的几个参数=================")

for num in range(10,20):  # 迭代 10 到 20 之间的数字
    for i in range(2,num): # 根据因子迭代
        if num%i == 0:      # 确定第一个因子
            j=num/i          # 计算第二个因子
            print('%d 等于 %d * %d' % (num,i,j))
            break            # 跳出当前循环
    else:                  # 循环的 else 部分
        print(num, '是一个质数',sep="--",end="\n",file=sys.stdout,flush=False)


print("""Python pass 是空语句，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句。

Python 语言 pass 语句语法格式如下：""")

# 输出 Python 的每个字母
for letter in 'Python':
    if letter == 'h':
        pass
        #print('这是 pass 块')
    print('当前字母 :', letter)

print("Good bye!")


print("-------------#字典的三种遍历方法-------------------")

print('－－－－－－－－－－－－－－遍历字典key')
#for…in dict:#遍历字典key
group = {'师父':'唐三藏', '大师兄':'孙行者', '二师兄':'猪八戒', '沙师弟':'沙和尚'}
for i in group:
    print(i)
print('－－－－－－－－－－－－－－遍历字典value')
#for…in dict.values():#遍历字典value
for j in group.values():
    print(j)
print("－－－－－－－－－－－－－－键值对遍历")
for k,v in group.items():
    print(k+" : "+v)


print("===========while 循环=================================")
# while循环和for循环的区别：
# #for擅⻓处理固定次，⾃动遍历各序列
# #while处理不定次数的循环，条件为False便停⽌
#当条件为真时，执⾏循环语句，只要条件为真，便会⼀直运行下去

# while 循环
#     else　关键字用法
#⽆论是否进⼊循环，最后都会执⾏esle语句，除⾮执⾏break语句跳出循环
count = 3
while count >2:
    print('while 循环')
    count = count -1
else: #无论是否进入循环都
    print('else　关键字用法')
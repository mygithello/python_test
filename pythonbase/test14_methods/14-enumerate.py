seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list0=list(enumerate(seasons))
print(list0)
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list2=list(enumerate(seasons, start=1))       # 下标从 1 开始
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
print(list2)

for index,record in list0:
    print(index)
    print(record)
    print("------------")

"""
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

enumerate(sequence, [start=0])
sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置
"""

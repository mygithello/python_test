print("""
GadFly
mSQL
MySQL
PostgreSQL
Microsoft SQL Server 2000
Informix
Interbase
Oracle
Sybase
你可以访问Python数据库接口及API查看详细的支持数据库列表。

不同的数据库你需要下载不同的DB API模块，例如你需要访问Oracle数据库和Mysql数据，你需要下载Oracle和MySQL数据库模块。

DB-API 是一个规范. 它定义了一系列必须的对象和数据库存取方式, 以便为各种各样的底层数据库系统和多种多样的数据库接口程序提供一致的访问接口 。

Python的DB-API，为大多数的数据库实现了接口，使用它连接各数据库后，就可以用相同的方式操作各数据库。

Python DB-API使用流程：

引入 API 模块。
获取与数据库的连接。
执行SQL语句和存储过程。
关闭数据库连接。

""")

print("""---------------------------------连接ｍysql-------------------------------------------""")
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# coding:utf-8
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306,
                     user='root', passwd='123456', db='mytest', charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


print("""-------------------------------------execute  SELECT VERSION();--------------------------""")
cursor.execute("SELECT VERSION();")
# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
print("Database version : %s " % data)

print("""-------------------------------------execute  show databases;--------------------------""")
cursor.execute("show databases;")
list=cursor.fetchall()
for i in list:
    print(i)

print("""-------------------------------------execute  show tables;--------------------------""")
cursor.execute("show tables;")
tables=cursor.fetchall();
for t in tables:
    print(t)

print("""---------------------------------execute  create table  ---------------------------------""")


# # 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE;")
#
# # 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT );"""
#
cursor.execute(sql)
print(cursor.fetchone())


print("""--------------------------------insert data into table-----------------------""")
# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
print("------------sql的％取值写法-------------")
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
       LAST_NAME, AGE, SEX, INCOME)
       VALUES ('%s', '%s', %d, '%s', %d )"""%('小米', 'Mohan2', 20, 'M', 2000)
print(sql)
'''
The formatting using % is similar to that of ‘printf’ in C programming language.
%d – integer
%f – float
%s – string
%x – hexadecimal
%o – octal
'''
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()





# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()

'''
执行事务
事务机制可以确保数据一致性。

事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。

原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。
'''

print("""

错误处理
DB API中定义了一些数据库操作的错误及异常，下表列出了这些错误和异常:

异常	描述
Warning	当有严重警告时触发，例如插入数据是被截断等等。必须是 StandardError 的子类。
Error	警告以外所有其他错误类。必须是 StandardError 的子类。
InterfaceError	当有数据库接口模块本身的错误（而不是数据库的错误）发生时触发。 必须是Error的子类。
DatabaseError	和数据库有关的错误发生时触发。 必须是Error的子类。
DataError	当有数据处理时的错误发生时触发，例如：除零错误，数据超范围等等。 必须是DatabaseError的子类。
OperationalError	指非用户控制的，而是操作数据库时发生的错误。例如：连接意外断开、 数据库名未找到、事务处理失败、内存分配错误等等操作数据库是发生的错误。 必须是DatabaseError的子类。
IntegrityError	完整性相关的错误，例如外键检查失败等。必须是DatabaseError子类。
InternalError	数据库的内部错误，例如游标（cursor）失效了、事务同步失败等等。 必须是DatabaseError子类。
ProgrammingError	程序错误，例如数据表（table）没找到或已存在、SQL语句语法错误、 参数数量错误等等。必须是DatabaseError的子类。
NotSupportedError	不支持错误，指使用了数据库不支持的函数或API等。例如在连接对象上 使用.rollback()函数，然而数据库并不支持事务或者事务已关闭。 必须是DatabaseError的子类。

""")
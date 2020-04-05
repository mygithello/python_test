print("""
－－－－－－－－－－－－－－－－－－－－内置函数－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
参考：　　https://www.runoob.com/python/python-built-in-functions.html

内置函数
bool(),int(),str(),input()

=============================================================================	
abs()	divmod()		open()	staticmethod()
all()	enumerate()		ord()	
any()	eval()	isinstance()	pow()	sum()
basestring()	execfile()	issubclass()	print()	super()
bin()	file()	iter()	property()	tuple()
filter()	len()	range()	type()
bytearray()	float()	list()	raw_input()	unichr()
callable()	format()	locals()	reduce()	unicode()
chr()	frozenset()	long()	reload()	vars()
classmethod()	getattr()	map()	repr()	xrange()
cmp()	globals()	max()	reverse()	zip()
compile()	hasattr()	memoryview()	round()	__import__()
complex()	hash()	min()	set()	
delattr()	help()	next()	setattr()	
dict()	hex()	object()	slice()	
dir()	id()	oct()	sorted()	exec 内置表达式

""")

#1.bool()函数，检验数值的真假（值为假：False,0,"",【】,{},None） 其他都为真
print(bool(False))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))
print(bool({}))

#2.input()

para=input("请输入：")
print(para+"是笨蛋")
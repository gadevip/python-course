'''
for .... else
else:适用于for执行完或者没有循环数据时，需要做的事情
for i in 范围
	有数据执行的语句
else:
	没有数据执行的语句

pass 空语句
只要有缩进而缩进的内容还不确定的时候，此时为了保证语法的正确性，就可以使用pass占位。
不会报出语法错误。

'''
num = int(input('请输入需要的馒头数量:'))

for i in range(num):	#2
	print('{}很饿，正在吃第馒头'.format(name,i+1))
else:
	print('还没有给我馒头，{}饿哭啦.....'.format(name))

print( '---------------')


# pass 

if 10<7:
	print( '10是大的')
else:
	pass
print( '-----判断结束-----')

for i in range(3):
	pass

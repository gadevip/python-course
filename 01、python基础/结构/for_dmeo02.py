'''
循环：吃5个馒头

'''
# 方式一：
# name = '赵飞'

# for i in range(5):
# 	print('{}很饿，正在吃第{}馒头'.format(name, i + 1))

# print('{}说：终于吃饱了！'.format(name))

# 方式二：
# name = '赵飞'

# for i in range(1,6):
# 	print('{}很饿，正在吃第{}馒头'.format(name, i))

# print('{}说：终于吃饱了！'.format(name))

# range(n)  ---> 0~n-1
# range(m,n)  ---> m~n-1

'''
吃馒头:在第三个馒头上抹了一点鹤顶红
'''

# 方式一
print('*' * 30)
name ='张无忌'
for i in range(1,6):
 	# 判断i的值是多少，i==3 别吃
	if i == 3:
		print("{}赶快扔掉这个馒头，有剧毒:'鹤顶红'!!!".format(name))
	else:
		print('{}很饿，正在吃第{}馒头'.format(name, i))

# 方式二
print('*' * 30)
name ='张无忌'
for i in range(1,6):
 	# 判断i的值是多少，i==3 别吃
	if i == 3:
		print("{}赶快扔掉这个馒头，有剧毒:'鹤顶红'!!!".format(name))
		continue
	print('{}很饿，正在吃第{}馒头'.format(name, i))

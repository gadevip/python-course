# 条件判断语句

'''
if 条件:
	条件成立执行的语句
'''

username='admin'	# 没有登录
username=''	# 没有登录
username=0	# 没有登录
username=None	# 没有登录
#  python:判断的变量是''  0  None 默认是False
#  python:如果变量有值'abc', 'kkk'认为是True

if username: 	#'admin'!=''  True 如果条件运算结果是True则进人内层
	print('嘿嘿!我登录啦!')
	print('-------------')

'''
如果年龄大于18并且输人le姓名，则打印xxx今年xxx岁
'''
# age = int(input('输入年龄:'))
# username=input('输入用户名')
# if age>18 and username:		# True and False --->False
# 	print('{}今年{}岁了!'.format(username,age))
# 	print( '---game over---- ')




# 用户的账号密码登录而且只能登录三次，如果三次未成功账户锁定
# break关键字

for i in range(3):
	username  = input('请输人用户名:')
	password  = input('请输人密码:')
	#·验证用户名和密码
	if username == 'gs' and password == '123456':
		print('欢迎!用户:0 '.format(username))
		print( ' -------轻松购物吧---------')  # 登录成功
		break
	else:
		print('用户名或者密码有误!')
else:
	print('账户被锁定，需要重新激活!') # 三次输入错误的时候


# 练习：
for i in range(3):  # 0 1 2
	if i==2:
		print('我吃的第{}个馒头有质量问题!这家店是黑店，等着关门吧!'.format(i+1))
		break				#跳出循环结构
		print( 'abcd ')		#即使有语句也不会执行，干脆别写!
	else:
		print('我吃的第{}个馒头真香啊!要多吃几个呀!'.format(i+1))

#  range的范围正常执行完毕，而没有异常break跳出。就可以执行else,
#  只要有break执行了就不会执行else

else:
 	print( ' ---->进入消协大门')


# range()的参数
for i in range(1, 20, 5):
	print('----->', i)
# java常量定义：final
# python：命名的时候，名字是大写的

NAME = 'Jack'
print(NAME)

print('hello') # 输出的是字符串

value = 'hello' 
print(value)

value ='python'
print(value)

value ="python1905班"
print(value)

# 字符串表示:1、单引号''  2、双引号""   3、三引号'''  '''

message = '[淘宝]你正在使用验证码登录，\n验证码是:8906，\n涉及个人的账户安全，请保密。'
print(message)

message1 = '''
[淘宝]
你正在使用验证码登录，
验证码是:8906,
涉及个人的账户安全,请保密。
'''

print(message1)

# 邮箱格式输出，按照下面要求进行输出

# 三引号的作用：1、原样输出字符串  2、作为多行注释使用
'''
亲爱的XX用户：
	你注册的用户还没有激活，请点击下方链接激活用户，
	请点击：激活用户
	激活用户后可以使用此软件

  from:app team

    date:2022-03-02
'''

email_message = '''    
亲爱的XX用户：
	你注册的用户还没有激活，请点击下方链接激活用户，
	请点击：激活用户
	激活用户后可以使用此软件

  from:app team

    date:2022-03-02
'''

print(email_message)


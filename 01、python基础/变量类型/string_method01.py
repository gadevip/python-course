# 案例:验证码案例
s='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnme987654321'
print(len(s))		#求字符串长度 len(str),返回值是一个整型的数值

# 四个随机数
code = ''

import random

# IndexError: string index out of range  下表超范围
# index: O~len(s)-1   O~61

for i in range(4):
	ran = random.randint(0, len(s)-1)

	code += s[ran]

print('随机验证码：' + code)

# 提示用户输入验证码

user_input = input('请输入验证码：')

if user_input.lower() == code.lower():
	print('验证码输入正确！')
else:
	print('验证码错误！')
'''
多层条件判断:
if 100-90:
	优+
elif 90-80:
	优-
elif 80-70:
	良
elif 70-60:
	及格
else:
	不及格
'''

age = int(input('请猜猜年龄:'))
if age <= 18 and age>0:
	print( '(o°v°)o☆[BINGO!]太有眼光啦!')
elif age>18 and age<=30:
	print('人家还是宝宝呢..... ')
elif age>30 and age<=40:
	print('长得太年轻了吧!!!! ')
else:
	print('输入错误!')

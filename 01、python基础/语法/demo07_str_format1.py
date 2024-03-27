name='赵飞'
print('姓名是:'+name) # str + str
age=18
#str(int) ---> (int ->str)强制类型的转换
print( '年龄是:'+str(age))  # 'aaa' int --->str
print('年龄是:%s'% age)     # %s -->str   简写  底层:强制转换 str(age) --->'18'
isMarry=False				#布尔:True, False
print('结婚否?回答:%s' % isMarry) 	# str(False) --->'False'

#%d  digit  数字
print('年龄是：%d' % age)


# age = '18岁'    # TypeError: %d format: a number is required, not str
age = 18.5    # int(18.5) --> 18   取整
print('年龄是：%d' % age)   

print('年龄是：%.1f' % age)

# %f 小数点后面的位数 而且是四舍五入
salary = 11500.6898
print('我的薪水是：%.2f' % salary)


# 练习
'''
约起来去楼上看电影，下订单:movie='大侦探皮卡丘'
ticket =45.9
count= 35

格式:
电影:XXXX
人数:xXX
单价:xXX
总票价:XXx
(小数点后面保留1位)

ticket = 78
total = ticket * count
'''

movie='大侦探皮卡丘'
ticket =45.9
count= 35
total = ticket*count
message='''
电影:%s
人数:%d
单价:%.1f
总票价:%.1f
''' % (movie, count,ticket,total)
print(message)


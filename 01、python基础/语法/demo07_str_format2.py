# 字符串的格式化输出
# 方式：1、使用站位符 %s %d %f  2、format() 函数


#  format是一个字符串对象中的函数   ''.format()   此处的'.' 是调用字符串对象中的format函数
name = 'Gs'
age = 2
str_s = '已经上'
message = '我是{},今年{}岁了,{}幼儿园！'.format(name,age,str_s)
print(message)


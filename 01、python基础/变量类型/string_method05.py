# join() : '-'.join( 'abc ')  将abc用-连接构成一个新的字符串

new_str = '-'.join( 'abc ')
print(new_str)


# python  列表  list =[ 'a','v','o' , '9']  数组
list1 =['a' ,'v' , 'o' , '9']
result = ''.join(list1)		
print(result)

result = ' '.join(list1)
print(type(result))


# lstrip  rstrip strip
s = '   hello   '
# s= s.lstrip()
# 去除字符串左侧的空格
# print(s+'8')
# S= s.rstrip()#去除右侧的空格
# print(s+'8 ')

s = s.strip()
print(s +'8')

# split(‘分隔符,，次数）分割字符串,将分割后的字符串保存到列表中
print('split-->')
s = 'hello world hello kitty'
# result = s.split(' ')
result = s.split(' ',2)			# 表示按照空格作为分隔符，分割字符串2次
print(result)

n = s.count(' ')				# count(args）求字符串中指定args的个数
result = s.split(' ', n)
print('个数:',n)
print(result)
# ////////////////////////////////////////////////////////
s = 'hfdsjkhfdf;lksd;fk'
print(s.count(';'))
print(s.split(';', s.count(';')))


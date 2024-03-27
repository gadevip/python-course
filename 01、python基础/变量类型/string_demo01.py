#字符串:
s1 = 'abc'
s2 = "abc"
s3 ='''abc
'''
print(id(s1),id(s2),id(s3)) # '''三引号占用的内存空间与单双引号的不同
							# （前提:'''的内容不在一行)

print(s1 == s2)		# 比较的是内容
print(s1 is s2)		# 比较的是地址

print(s2 ==s3)
print(s2 is s3)


s1 = input('请输入: ')
s2 = input('请输入:')

# 常量赋值is是True，input输入底层做了处理所以最后的地址是不一样的
print(s1 == s2)		
print(s1 is s2)

#字符串的运算符:+*
s1 = 'abc'
s2 = "abc"
s3 = s1 + s2			# ＋相当于拼接符
s4 = s1 * 5			# 倍数
print(s3)
print(s4)			

# in在...里面
name ='steven'

result = 'st' in name		#返回值是布尔类型 True False
print(result)

result = 'tv' not in name 	#返回值是布尔类型 True False
print(result)


# % 字符串的格式化
print( '%s说:%s'% (name, '大家好好学习!'))

# r保留原格式,有r则不发生转义,没有r则发生转义（例如:\')

print(r'%s说:\'哈哈哈!\'' % name)


# [] [start : end]
filename = 'picture.png'

# 位置都是从0开始,位置也会称作下标或者索引
print(filename[5]) 	# 通过[] 可以结合位置 获取字母 特点:只能获取一个字母

#range(1,10)--类似-->[1:10]

print(filename[0:7])	# 包前不包后
print(filename[3:7])	# 截取字符串

# 省略
print(filename[3:])		# 只要省略的是后面的，表示一直取到字符串的末尾
print(filename[:7])		# 只要省略的是前面的，表示从0开始取值

# 负数
print('负数')
print(filename[8:-1])  	# pn
print(filename[:-2])	# picture.p
print(filename[-1:])	# g
print(filename[-5:-1])	# e.pn
print('---->',filename[10:0])  # ---->

#[::-1]倒叙
print('倒叙')
str1 = 'abcdefg'
print (str1[-1:-5:-1])	# gfed
print(str1[5:0:-1])		# fedcb
print('---->',str1[5:0:1]) 
print(str1[::-1]) 		# gfedcba

'''
str[start:end:方向和步长]
方向:1 表示从左向右0,1,2,3,4,5。。。
	-1 表示从右向左

	注意数值的顺序
	比如:正向: 5:0就不行了
		 反向: 5:0就可以取到值
'''

# 练习:hello world
# 逆序输出world: ---> dlrow#正向输出hello
# 逆序输出整个hello world#打印获取oll
# 打印1lo wo

'''
答案
s1 = 'hello world'
print(s1[-1:-6:-1])
print(s1[:5])
print(s1[::-1])
print(s1[4:1:-1])
print(s1[2:-3])		# s1[2:8]
#
print(s1[::-3])
'''

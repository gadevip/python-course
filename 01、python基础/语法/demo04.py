#print函数
#1.用法
print('hello world!')
name ='小白'
print(name)
#2.用法:print(name, age, gender)
age =18
gender ='boy'

print(name,age,gender)  #sep默认的分割是空格

#3.用法:print(value, value, value, . . .,sep=' " ,end="\n')
print(name, age,gender,sep='-')    # sep=f*'sep= '$' sep='-'

#转义字符: \n换行
print('helloinkitty')
print('AAA',end="")   #'AAA\n'---> 'AAA'
print('BBB',end="")   #'BBB\n' --->'BBB'
print( 'ccc',end="")  #'CCC\n' --->'ccc'


# 练习（使用一个print函数实现）：
'''
	亲爱的xxx:
	   请点击链接激活用户：激活用户
'''
print()

print('亲爱的xxx:\n','\t请点击链接激活用户：激活用户')

# 转义字符： \n 换行   \t 制表符  \'   \"   \r 回车 \\
print('琼脂说：\'雨露！！\'')
print("琼脂说：\"雨露！！\"")

#''''  "''"  '""'

print('琼脂说："雨露！！"')
print("琼脂说：'雨露！！'")

print(r'hello\py\thon')  #  r"  raw 原样输出字符串的内容，即使有转义字符也不会转义

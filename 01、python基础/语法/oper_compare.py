n1 = int(input('请输入第一个数：'))
n2 = int(input('请输入第二个数：'))

# 判断n1与n2

result = n1 > n2  # 结果False  True

print('n1>n2', result)

result = n1 == n2
print('n1==n2', result)

# ==
m1 = 'hello'
m2 = 'hello'
print(id(m1),id(m2))

result = m1 == m2
print('m1==m2', result)

# != 不等于
username = input('输入用户名：')
uname = 'admin'

print(username != uname)

# is 用户对象的比较（对象内存地址）
age = 20
age1 = 20
print( id(age))
print(id(age1))
print(age is age1)

money = 2000000
salary = 2000000
print(id(money))
print(id(salary))
print(money is salary)

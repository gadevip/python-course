#  赋值运算
# 所谓赋值 就是把内存的指向改变

# 1. =
name = 'admin'

#将'admin'的值赋给变量name

name1 = name
print(id(name) ,name)
print(id(name1),name1)

name2=name
print(id(name2),name2)

# id()
print(name == name1)

name1='admin1'
print(id(name1), name1)
print(id(name), name)

name = 'admin2'
print(id(name), name)

name3 = name
print(id(name3), name3)

#扩展后的赋值符号  +=  -=   *=    /=  ...
# -=  *=   /= 只是可以应用在数值，字符串不支持

num = 8
num +=5   #num = num + 5    此时+数学加号
print(num)
a='abc'
a += 'ff'   # 等价于:a=a +'ff'  此时‘+‘就是连接符 包含两个动作：1、连接  2、连接后的结果赋值
print(a)  


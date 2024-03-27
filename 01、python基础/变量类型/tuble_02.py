# 1、拆包
t1 = (4, 7, 3)
# a, b = t1  # ValueError: too many values to unpack(拆包) (expected(期望) 2)
# x,y,z = (6,) # ValueError: not enough values to unpack (expected 3, got 1)
a, b, c = t1
print(a, b, c)

a = t1
print(a)

# 2、使用'*'操作符:
# 元组的*操作
t1 = (2, 5, 8, 9, 7)  # 变量个数与元组个数不一致
# 在参数名之前加星号，让变量接受任意多参数
# '*'操作符的作用是将元组“拆包”,
a, *b, c = t1
print(a, c, b)

a, c, *b = t1
print(a, c, b)

t1 = (9,)
# a, b = t1  # ValueError: not enough values to unpack (expected 2, got 1)
a, *b = t1
print('---->', a, b)  # *b表示未知个数0~n,   0对应的是--->空列表 []

# 3、字符串与列表的 *操作
# 字符串使用*进行拆包  x,y,*z
x, y, *z = 'hello'
print(x, y, z)

# 列表使用*进行拆包
x, y, *z = ['hello', 'mn', 'op', 'nc']
print(x, y, z)

# 4、*操作符的底层实现
t1 = (9, 4, 8, 6)
x, *y = t1  # 在本身的赋值过程中，底层先进行拆包，所以拆包后是 9,4,8,6
print(x)  # 先给x赋值  x = 9
print(*y)  # 再给*y赋值 所以*y = 4,8,6
# 赋值：装包过程(*y-->y)：装入到列表中
# 现在把散列的4,8,6赋值给*y，此时系统底层发现*后，所以会准备一个空列表[]容器
# 把4,8,6装包到[]中， 所以y = [4,8,6]
print(y)  # y = [4,8,6]
# 打印：拆包过程(y-->*y)：从列表中拆除
# 系统底层在[4, 8, 6]列表前面发现*，所以进行拆包
print(*[4, 8, 6])  # 4 8 6


# 补充部分
# 元组的快速赋值
a, b, c = (2, 5, 7)
print(a, b, c)

# 使用元组 实现快速交换
a, b = b, a
print(a, b)
'''
字符串中可以使用的符号: +  =  *  in    not in   is   not is   []

列表支持的符号: +   *    in
'''
l1 = [1, 2, 3]
l2 = [5, 6, 7]
l3 = l1 + l2
print(l3)

l4 = [5, 8] * 3
print(l4)

result = 3 in [1, 2, 3, 4]
print(result)

result = [3] in [1, 2, [3], 4, 5]
print(result)
'''
列表中的元素:
整型
字符串类型
浮点型
列表
元组
字典
对象
'''
# 列表的嵌套
result = [3, 2] in [1, 2, [3, 2, 1], 4, 5]
print(result)

# [1,2,3, 'aa', 'bb',[1,2], [6,8,9,0]]
# [[1,2],[6,8,9,0]]     #二维

l5 = [[1, 2], [3, 2, 1], [4, 5], [7, [2, 3], 1]]
print(len(l5))
e = l5[2]
print(e, type(e))  # [4,5]
print(e[1])
print(l5[1][1])
print(l5[3][1][1])

# 关于list()：  将指定的内容转换成列表，可迭代的内容放到list中

# 1、list对range()的转换  range()会返回一个对象  list()将此对象的值存储到列表中
print(list(range(1, 10, 3)))  # [1,4,7]

# 2、list对字符串的转换  字符串拆分后分别存储到列表中
s = 'abc'
print(list(s))  # ['a', 'b', 'c']

# 3、iterable 可迭代的   可以在for ... in 里面循环的就是可迭代的
# 'abcdef'  ----->  a  b  c
'''
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
'''
# result = list(10)   # 10 是不可迭代的
# print(result)  # TypeError: 'int' object is not iterable


a = [7, 3, 4]
# list.sort()
# a.sort(reverse=True)  #  a.sort()主要是在原有的列表上进行降序或者升序排列
# print(a)

#  sorted(list, reverse=True)
print(sorted(a, reverse=True))  # sorted(a)的方法则是排序后返回一个新列表

# list.reverse()
a.reverse()  # 翻转数组
print(a)


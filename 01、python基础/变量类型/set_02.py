'''
1.产生10个1～20的随机数，去除里面的重复项
2.键盘输人一个元素,将此元素从不重复的集合中删除
'''
import random

list1 = []
set1 = set()
# 方式1： 没有保证10个数字
# for i in range(10):
#     ran = random.randint(1, 20)
#     list1.append(ran)
#
# set1.update(list1)
# print(list1)
# print(set1)

# 方式二：
for i in range(10):
    ran = random.randint(1, 20)
    set1.add(ran)
print(set1)

# num = int(input('输入一个数字：'))
# set1.discard(num)
# print('删除之后结果:', set1)

# 方式三: 使用while 保证10个随机数

print('------------------------------------------')
# 其他：符号操作
# 支持 in   not in  ==  !=  is
# 不支持 +  *
print(6 in set1)

set2 = {2, 5, 8, 12, 11}
set3 = {2, 5, 8, 12, 11}
print(set2 == set3)  # 比较内容
print(id(set2))
print(id(set3))
print(set2 is set3)  # 比较地址

# 差集
# set4 = set3 - set2和函数difference()效果一样
set3 = {2, 5, 7, 8, 12, 11}
set2 = {2, 5, 8, 12, 11}
set4 = set3 - set2
set5 = set3.difference(set2)
print(set4)
print(set5)

# & 交集 intersection()
set6 = set3 & set2
print(set6)
set7 = set3.intersection(set2)
print(set7)

# |  并集 union() 联合
set8 = set3 | set2
print(set3.union(set2))
print(set8)


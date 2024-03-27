'''
1、元组的概念：
类似于列表(当成容器)
特点：
1、定义的符号：（）
2、元组中的内容不可修改
3、关键字：tuple
4、元组的单个存放：必须后面加逗号 ,
        列表          元组
        []              ()
        [1]             (1)
元组:
1.符号:(1,2,3)  tuple
2.关键字:tuple
3.元组的元素只能获取,不能增删改
符号:
+  *
is not
in not in

系统函数:
max()  min()  sum()  len()
sorted() ---->排序，返回的结果就是列表
tuple(） ---->元组类型的强制转换
元组自带函数:
index()
count()

拆装包:
x,*y =(1,2,3,4,5)
print(y)
print(*y)
'''
t1 = ()
print((type(t1)))  # <class 'tuple'>

t2 = ('hello',)
print((type(t2)))

t3 = ('aa', 'aa')
print(type(t3))

t4 = (11, 2, 3, 5, 6, 7, 20)

# 2、元组的赋值
import random

list1 = []
for i in range(10):
    ran = random.randint(1, 20)
    list1.append(ran)
print(list1)
t5 = tuple(list1)
print(t5)

# 3、元组的符号
t2 = (4, 5) + (1, 2)
print(t2)
t3 = (3, 4) * 2
print(t3)

print(t2 is t3)
print(3 not in t3)

# 4、元组中的系统函数
# 元组的操作---查询（根据下标index)  获取切片 [:]
print(list1[0:10])
print(t5[0:len(t5)])

# 最值
print(max(t5))
print(min(t5))
# 求和
print(sum(t5))
# 求长度
print(len(t5))
# sorted()  ---> 排序，返回的结果是列表
print('sorted-t2->', sorted(t2))
print(tuple(sorted(t2)))

# 元组自带的函数：index()   count()
print(t5.count(3))  # 数字3在t5元组中出现的个数
print(t5.index(3))  # 从t5这个元组中找到数字3 的下标位置，没有报错:ValueError: tuple.index(x): x not in tuple

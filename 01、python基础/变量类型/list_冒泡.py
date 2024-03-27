# enumerate():枚举函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列

l1 = ['a', 'abc', 'jk', ' opop']
for index, value in enumerate(l1):  # 可以获取下标index
    print(index, value)

for index, value in enumerate('happy'):
    print(index, value)

# 算法
# 冒泡排序1
numbers = [5, 7, 8, 9, 2, 0, 6, 4, 9]
numbers = sorted(numbers)
print(numbers)

numbers.sort(reverse=True)
print(numbers)
print(' ---------------升序排列---------------------')
numbers = [8, 5, 9, 7]
# 自定义排序
# 升序排列
for i in range(len(numbers)):
    # numbers[i]=5
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            # 快速交换
            numbers[i], numbers[j] = numbers[j], numbers[i]
            print(numbers)
    print(' ------------>', i)
print(' ---------------降序排列---------------------')
# 降序排列
for i in range(len(numbers)):
    # numbers[i]=5
    for j in range(i + 1, len(numbers)):
        if numbers[i] < numbers[j]:
            # 快速交换
            numbers[i], numbers[j] = numbers[j], numbers[i]
            print(numbers)
    print(' ------------>', i)

# 冒泡排序2
print(' ---------------冒泡排序2---------------------')
myList = [4, 1, 7, 0]
length = len(myList)
for i in range(len(myList) - 1):
    for j in range(0, len(myList) - 1 - i):
        # 交换
        if myList[j] > myList[j + 1]:
            tmp = myList[j]
            myList[j] = myList[j + 1]
            myList[j + 1] = tmp
print(myList)

print(' ---------------冒泡排序3---------------------')
myList = [4, 1, 7, 0]
for i in range(len(myList) - 1):
    # 每一轮的比较,注意range的变化,这里需要进行length-1-长的比较,
    # 注意-i的意义(可以减少比较已经排好序的元秦)
    for j in range(0, len(myList) - 1 - i):
        # 交换
        if myList[j] > myList[j + 1]:
            myList[j], myList[j + 1] = myList[j + 1], myList[j]
print(myList)
# 总结
'''
总结列表:list
1．定义
l=[]空列表
l= [aaa']

2.符号:
+ ----》合并[+[]
*----->[]*n
in ----> a in[] False True
not in ---->
is地址是否相等
not is

3.系统中给列表用函数:
len(list) ----> int
sorted(list)---->排序
max()最大值
min()最小值
list() 强制转换成列表类型
enumerate(list)枚举  index value

4.列表自身函数:
添加元素:
    append()    末尾添加
    extend()    末尾添加一组元素
    insert()    指定位置插入
删除:
    del list1[index]
    remove(obj)删除指定的元素，如果指定的元素不存在则报异常
    pop() 队列  FIFO 栈  FILO 默认删除的是最后一个元素
    clear(）清空元素

其他:
    count() 指定元素的个数
    sort()  排序
    reverse()   翻转  [4,6,8,9,0] --->[0,9,8,6,4]
算法:
    选择排序
    冒泡排序
'''

# 练习
'''
=====通讯录管理系玩=====
1.增加姓名和手机
2.删除姓名
3.修改手机
4.查询所有用户
5.根据姓名查找手机号
6.退出
===========================
'''
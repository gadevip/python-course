# 集合:set  无序的不重复的元素
# 作用：不重复特点
list1 = [13, 5, 6, 8, 2, 5, 8, 2, 6, 3, 2, 1, 9]

# 声明集合：set
s1 = set()  # 创建空集合，只能使用set()

# 字典：{key:value, key:value,...}
# 集合：{元素1,元素2,....}
s2 = {1, 2, 6}
print(type(s1))
print(type(s2))

# 将列表快速的去除重复项,使用集合
s3 = set(list1)
print(s3)  # 去除重复，对数字还进行了排序

# 集合的增删改查

# 1.增加
# add()  添加一个元素
s1.add('hello')
s1.add('小猪')
s1.add('lucy')
print(s1)  # 无序  不重复

# update() 添加多个元素（列表、元组）
t1 = ('林志玲', '言承旭', '小猪')
s1.update(t1)
print(s1)

s1.add(t1)  # 把元组作为一个整体添加到s1中
print(s1)  # {'小猪', ('林志玲', '言承旭', '小猪'), 'hello', '言承旭', '林志玲', 'lucy'}

# 2、删除
# remove()  如果元秦存在则删除,不存在则报错keyError
s1.remove('言承旭')
print(s1)
# s1.remove('道明寺')  # KeyError: '道明寺'
# print(s1)

# pop()     随机删除(一般删除第一个元素)
s1.pop()
print(s1)

# clear()  清空
# s1.clear()
print(s1)  # set()

# discard()  类似remove()
s1.discard('道明寺')
print(s1)




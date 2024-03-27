# 增 改 查 （key唯一性)
# 删除：del dict[key]
dict1 = {'张三': 100, '李四': 100, '王五': 89, '赵柳': 99}
del dict1['王五']
print(dict1)
# del dict1['ha']  # KeyError

# 字典的内置函数：删除
# pop(key) -> 根据key删除字典中对应的值_VT，并返回_VT
result = dict1.pop('李四')
print(result)
# pop(key[,default]) ->在删除的时候没有找到key，则返回default默认值
result = dict1.pop('小小', 20)
print(result)
print(dict1)

# popitem()  随机删除字典中键值对（一般是从末尾删除元素）
dict1 = {'张三': 100, '李四': 100, '王五': 89, '赵柳': 99}
# 移除并返回(key, value)对保存为一个元组；
# 如果字典为空，则引发KeyError: 'popitem(): dictionary is empty'
print(dict1)
for i in range(len(dict1)):
    result = dict1.popitem()
    print(result)

# clear() 清空 返回一个空{}
dict1.clear()
print(dict1)

# 其他内置函数:update()   fromkeys()
# update()  更新字典，合并两个字典，合并过程中重复部分省略
dict1 = {0: 'tom', 1: 'jack', 2: 'lucy'}
dict2 = {0: 'lily', 3: 'ruby'}
result = dict1.update(dict2)  # 返回值是None
print(result)
print(dict1)

# 注意：字典不支持 + 操作
# dict1 = dict1 + dict2  # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# print(dict1)

# fromkeys(seq[,value])
# 创建一个新字典，其中的键key来自参数1（可迭代对象seq），参数2设置为value的值。
# 没有指定value则设置为None
# dict1 = {0: 'tom', 1: 'jack', 2: 'lucy'}
# dict2 = {0: 'lily', 3: 'ruby'}
list1 = ['aa', 'bb', 'cc']
new_dict = dict.fromkeys(list1)  # {'aa': None, 'bb': None, 'cc': None}
new_dict = dict.fromkeys(list1, 10)  # {'aa': 10, 'bb': 10, 'cc': 10}
print(new_dict)

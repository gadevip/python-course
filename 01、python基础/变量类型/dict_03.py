'''
增加元素对比:
list1 =[]
list1.append(element)

dict1 ={}
dict1[key]=value

修改:
list1 [index]=newvalue
dict1[key]=newvalue

查询元秦:
list1[index]---->element
dict1[key] --->value
取值:字典都是根据key获取value值

'''
list1 = [3, 5, 8, 7]
print(list1[2])  # 列表中找元素根据下标

dict1 = {'1': '张三', '2': '李四', '3': '王五'}

print(dict1['2'])  # 字 典中找元素根据key

dict2 = {'张三': 100, '李四': 100, '王五': 89, '赵柳': 99}
print(dict2['王五'])  # key

# 考试分数大于90分的人名
print('------考试分数大于90分的人名------')
# 尝试对字典遍历
# 方式一：
for key in dict2:
    # print(key)  # 遍历的结果：就是字典的key
    # print('{}-->{}'.format(key, dict2[key]))
    if dict2[key] > 90:
        print('{}-->{}'.format(key, dict2[key]))

# 使用字典的函数  items()  values()  keys()
# 方式二
# 1、items() 把字典转换成列表形式保存，把字典中成对的key:value存入到元组中。
print(dict2.items())  # dict_items([('张三', 100), ('李四', 100), ('王五', 89), ('赵柳', 99)])

for i in dict2.items():
    print(i)  # ('张三', 100), ('李四', 100), ('王五', 89), ('赵柳', 99)

for key, value in dict2.items():
    # print('{}-->{}'.format(key, value))
    if value > 90:
        print(key)

# 2、values:取出字典中所有值，保存到列表中
result = dict2.values()  # dict_values([100, 100, 89, 99])
print(result)

# 练习：求所有学生考试成绩平均分
sum = 0
for value in dict2.values():
    sum += value
avg = sum / len(dict2)
# print(len(dict2))
print(avg)

# 3、keys():取出字典中所有的key，保存到列表中
dict2 = {'张三': 100, '李四': 100, '王五': 89, '赵柳': 99}
print(dict2.keys())  # dict_keys(['张三', '李四', '王五', '赵柳'])

# 4、in 在字典中的使用  和key匹配
print('王五' in dict2)  # True

'''
1.根据key获取值,如果key在字典中没有存在则报出keyError
    dict[key] ---->, value
2.字典的内置函数:
    get(key) ---->value如果取不到值则个会报错，则返口None
    get(key ,default) --->value 
    如果能够取到值则返回字典中的值,如果取不到则返回default的值,但原字典没有增加。
    
    items()   keys()  values()
'''
dict2 = {'张三': 100, '李四': 100, '王五': 89, '赵柳': 99}
# print(dict2['赵云'])  # KeyError: '赵云'
print(dict2.get('赵云', 98))
print(dict2)

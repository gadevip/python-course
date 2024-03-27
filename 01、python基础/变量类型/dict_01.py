'''
08、dictionary 字典
 特点：
 1、符号: {}
 2、关键字：dict
 3、保存的元素： key:value   key在字典中是唯一的
 4、键必须是不可变的，如字符串，数字或元组

'''
# 定义
# 方式一：
dict1 = {}  # 空字典
dict2 = {'ID': '894699546583', 'name': 'lucky', 'age': 18}

# 方式二：
dict3 = dict()  # 空字典  list1 = list() 空列表 tuple1 = tuple() 空元组

# 错误一：ValueError: dictionary update sequence element #0 has length 4; 2 is required
# dict4 = dict(('name', 'lucky'))  # {'name': xxx, 'lucky':xxx}

# dict([(),(),()])   或者 dict(  ( (),() )  )  或者  dict([],[],[])
dict4 = dict([('name', 'lucky'), ('age', 18), ('gender', '男')])  # 'name': 'lucky', 'age': 18
dict4 = dict([['name', 'lucky'], ['age', 18], ['ID', '656896576321']])
print(dict4)

# 错误2：ValueError: dictionary update sequence element #0 has length 3; 2 is required
# dict5 = dict([(1, 2, 3), (2, 2)])

# 注意：list可以转成字典 但是前提：列表中元素都要成对出现


# 字典的增删改查

# 注意:list可以转成字典但是前提:列表中元素都要成对出现
# #字典的增删改查:
# 增加:格式:dict6[key]=value
# 特点:按照上面的格式，如果在字典中存在同名的key,
# 则发生值的覆盖（后面的值覆盖原来的)。
# #如果没有同名的key，则实现的添加功能（key:value添加到字典中)
dict6 = {}
dict6['brand'] = 'huawei'
print(dict6)  # {'brand' : 'huawei'}
dict6['brand'] = 'mi'
print(dict6)
dict6['type'] = 'p30 pro'
dict6['price'] = 9000
dict6['color'] = '黑色'
dict6[1] =2
print(dict6)


# list列表的添加:
# 临时（存储在内存中）小数据库:list

# 创建一个空列表
girls = ['杨幂']
# quit 表示退出
# 列表的函数使用:append  extend  insert

# append()  末尾追加
while True:
    name = input('请输人你心目中的名字:')
    if name == 'quit':
        break
    girls.append(name)
print(girls)

# extend  类似于列表的合并
name = input('请输人你心目中的美女名字:')
names = ['黑嘉嘉', '孙俪', '巩俐', '王丽坤']
girls.extend(name)  # 输入的内容拆开后再合并
girls.extend(names)
print(girls)

#  符号 +  也可以用于列表的合并
girls = girls + names
print(girls)

# insert 插入
# ['杨幂','黑嘉嘉','孙俪','巩俐','王丽坤']
#   0       1       2      3       4
# append 末尾追加
# insert 指定位置添加
# extend —次添加多个元秦
girls.insert(1, '刘涛')
print(girls)

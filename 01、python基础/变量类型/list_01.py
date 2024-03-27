#声明
names = [ 'jack' , 'tom' , 'lucy' , 'superman' , 'ironman'] #列表

computer_brands = []

# 增删改查

# 地址
print(id(names))
print(id(computer_brands))

# 列表的查询

# 元素获取使用:下标索引
print(names[0])
print(names[1])

# 获取最后一个元素
print(names[-1])

print(len(names))

print(names[len(names)-1])

# 获取第一个元素
print(names[-5])

# 结合循环
# for i in 'hello':
# 	print(i)

print('*' * 10)
for name in names:
	print(name)

# 查询names里面有没有保存超人
for name in names:
	if name == 'superman':
		print('存在超人')
		break
else:
	print('没有超人')

# 简便方式
if 'superman' in names:
	print('有超人') 
else:
	print('没有超人')
# 字符串切片操作
# s = 'abcdefg'  s[2:5] --->cde

# 标号:
list1 = ['杨超越', '热巴', '佟丽娅', '杨幂', '赵丽颖', '刘亦菲', '黑嘉嘉', 100, 99.9]
print(list1)
print(list1[3])
# 列表也是支持切片
print(list1[3:6])  # 将截取的结果再次保存在一个列表中['杨幂','赵丽颖','刘亦菲
print(list1[-3:-1])
print(list1[::2])  # 步长
print(list1[-5:-1:2])

# 反方向  从右向左
print(list1[-1::-1])
print(list1[-1::-2])

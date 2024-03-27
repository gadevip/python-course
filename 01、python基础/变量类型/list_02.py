# 列表的修改

brands = ['hp', 'dell', 'thinkpad', '华为', 'lenovo', 'mac', '神州']
print(brands)
print(brands[-1])

brands[-1] = 'HASEE'  # 赋值 步骤：1、找到（使用下标） 2、通过 = 赋值 3、新的值覆盖原有数值
print(brands)

# print('*' * 30, '错误的方式')
# for brand in brands:
#     if '华为' in brand:
#         brand = 'HUAWEI'
# print(brands)

print('-' * 30)
for i in range(len(brands)):
    # i是 0,1,2,3,....----> i就是下标
    if '华为' in brands[i]:
        brands[i] = 'HUAWEI'
        break
print(brands)

# 删除 del (delete的缩写)
del brands[2]
print(brands)

#  删除 hp，mac都要删除
#  注意删除的时候'列表'的长度
# print("-" * 30, '方式一--错误删除：')
# for i in range(len(brands)):    #  len(brands) 固定为7
#     if 'hp' in brands[i] or 'mac' in brands[i]:
#         del brands[i]
# print(brands)

print("-" * 30, '方式二--删除：')
l = len(brands)
i = 0
while i < l:
    if 'hp' in brands[i] or 'mac' in brands[i]:
        del brands[i]
        l -= 1
    i += 1
print(brands)



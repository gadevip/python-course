# 产生10个随机数，将其保存到列表中
'''
步骤
1.如何产生随机数
2.产生10个数字
3.将产生的随机数放到列表中
4.打印列表
'''
import random

random_list = []
for i in range(10):
    ran = random.randint(1, 50)
    random_list.append(ran)
print(random_list)

# 产生10个不同的随机数,将其保存到列表中
print('方式一：产生10个不同的随机数,将其保存到列表中')
# 错误方式：
random_list = []
for i in range(10):
    ran = random.randint(1, 50)
    # if ran in random_list:
    #     pass
    # else:
    #     random_list.append(ran)
    if ran not in random_list:
        random_list.append(ran)
print(random_list, '个数不一定是10个')  # 个数不一定是10个

print('方式二：产生10个不同的随机数,将其保存到列表中')
random_list = []
i = 0
while i < 10:
    ran = random.randint(1, 20)
    if ran not in random_list:
        random_list.append(ran)
        i += 1
print(random_list, '产生10个不同随机数')

# 找出列表中的最大值   max(list) ----->  列表中的最大值
print('找出列表中的最大值：')
print(max(random_list))
print(min(random_list))
print('-------------自定义求最值----------------')
mvalue = random_list[0]
minvalue = random_list[0]

for value in random_list:
    if value > mvalue:
        mvalue = value
    if value < minvalue:
        minvalue = value
print('最大值是：', mvalue)
print('最小值是：', minvalue)

# 求和
sum_value = 0
for value in random_list:
    sum_value += value
print(sum_value)
print('调用系统sum函数求和：=', sum(random_list))

# 排序:sorted  排序  默认是升序
# sorted(list) ---> 默认是升序   1,2,3,4,5,6
# sorted(list, reverse=True) ----> 降序  6,5,4,3,2,1
new_list = sorted(random_list, reverse=True)
print('排序后列表：', new_list)

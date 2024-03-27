person = '大哥'
address = '东莞市寮步镇'
phone = '1555658757'
num = 5

print('订单的收件人是：'+person+',收货地址是：'+address+',联系方式:'+phone)
# 字符串 + int 报错：TypeError: can only concatenate str (not "int") to str
# print('订单的收件人是：'+person+',收货地址是：'+address+',联系方式:'+phone+',商品数量是：'+num)

# %s 占位符
print('订单的收件人是：%s,收货地址是：%s,联系方式:%s' %(person,address,phone))

print('订单的收件人是：%s,收货地址是：%s,联系方式:%s,商品数量是：%s' %(person,address,phone,num))

'''
1.
个人信息简介:
名字
年龄
班级

我的名字:xxx，今年n岁了，现在在x班级

2.
个人信息简介:
我的名字:xXX
今年n岁
现在在xxx班级

'''

name = 'admin'
age = 18
clazz = 'python5-6'

msg = '''
个人信息简介：
我的名字是：%s
今年%s岁
现在在%s班级
''' % (name,age,clazz)

print(msg)


#and  or  not
#and 逻辑与 
# or 逻辑或
# not 逻辑非
#逻辑运算符的运算结果也是返回True False


'''
True and True ---->True 其他情况
True and False --->False
False and True ---->False
False and False ---->False

8>10 and 6<8
False and True ---->False

'admin' == 'admin123' and ' 123456'== '123456' ---->False
        False                        True
'''

n1 = 8
n2 = 5
n3 = 3
result = n1>=(n2+n3) and n1>n2

'''
步骤:
1. n1>=(n2+n3)  8>= 8 True
2. n1>n2  8>5 True
3. True and True
4．结果:True
'''
n2=n2+n3
result = n1>=n2 and n1==n3
#          True      False 

'''
or:或者
手机号  或者  账户名
只要有一边为真True，结果即为真True
True or True ---- >True
True or False ---->True
False or True ---->True
False or False ---->False
'''

#判断是否存在用户
username = ''

email ='63478364@qq.com'
result = username== 'admin123' or email =='63478364@qq.com'
print(result)


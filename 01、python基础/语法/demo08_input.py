# input()输入函数

# name = input('请输入姓名：')    # 阻塞式

# print('您的游戏人物名称是：{}'.format(name))

'''
练习:
游戏:捕鱼达人
输入参与游戏者用户名:输人密码:
充值:500
'''
print('''
*********************
捕鱼达人
*********************
''')

username = input('输入参与游戏者用户名:')
password = input('输入密码：')

print('%s请充值才能加人游戏!' % username)
coins = int(input('请充值;'))

print('%s充值成功! 当前游戏币是:%d' % (username,coins))



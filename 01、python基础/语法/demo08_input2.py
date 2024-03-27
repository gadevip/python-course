'''
游戏:英雄联盟
输人角色:XXX
输人拥有的装备:XXX
输人想购买装备:XXX
输人付款金额:XXX
XXXX拥有XX×x装备,花了xx×钱
知识点: input()输入函数    格式化输出print()  format()函数
'''


print('''
*********************
英雄联盟
*********************
''')
role = input('输入角色:')
equipment = input('输人拥有的装备:')
upgrade_equipment = input('输入想购买装备:')
pay = input('输入付款金额:')

#变量的赋值替换
equipment = upgrade_equipment

print('{}拥有{}装备，购买此装备花了{}钱'.format(role,equipment,pay))

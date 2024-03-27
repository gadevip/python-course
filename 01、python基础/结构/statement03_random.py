#  随机数
import random

# print(random.randint(1, 10))
'''
猜大小
步骤:
1.系统产生一个随机数
2．键盘输人一个数
3．将系统产生的与键盘输人的进行比较
4．猜对了，中大奖 猜错啦拜拜下次再来
'''

ran = str(random.randint(1,10)) # 8
num = input('请输人(1-10)之间的随机:')  #‘8'

# print(8 =='8')
if ran == num:
	print('恭喜中大奖啦!奖品是:笔记本')
else:
	print('很遗憾你猜错啦!与奖品擦肩而过~~')
print('公布中奖号码：', ran)
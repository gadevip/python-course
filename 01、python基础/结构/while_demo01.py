i = 0
while i <= 10:
	i+=1
	print(i)

print('Game Over')


# 打印1-30之间的所有3的倍数
# 方式1
print('方式一：','*' * 30)
n = 1 

while n <= 30:
	if n%3 == 0:
		print('----->',n)
	#  改变n
	n += 1

# 方式2
print('方式二：','*' * 30) 
n = 3
while n <= 30:
	print('--->', n)
	n += 3

# 方式3:注意while的条件只要为假 就会结束循环
print('方式三：','*' * 30) 
n = 1
while n <= 30 and n%3 == 0:     # while后的条件 为假 循环结束
	print('--->', n)
	n += 1


# 打印1-30之间的所有3和5的倍数
print('打印1-30之间的所有3和5的倍数：') 
n = 1
while n <= 30:     
	if n%3 == 0 and n%5 == 0:
		print('--->', n)
	n += 1
print('game over')
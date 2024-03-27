'''
    if和in  只是作为一个条件表达式:
        if 'a' in 'abc':
            pass
        if 'a' in [ 'a', 'b','c']:
            pass
    但是:
    for ... in  是一种循环

    for 变量 in 字符串|列表:
        pass
'''

if 'good' == ' good ':  # == 比较的是内容'good' 'good'
    print('相等')
if 'good' in 'goods':  # in运算符应用在字符串判断中 也可以用在列表[]
    print('相等或者包含')

i = 1
if 'good' in ['goods ', 'good ', 'abc', 'aaaa']:
    print('包含.....', i)
    i += 1
# A.1  B,2  c.1,2  D:以上都对

for w in ['goods ', 'good ', 'abc', 'aaaa']:
    # w = goods ,  w = good ,  w = abc ,  w = aaaa
    print('------->', i, end='')  # True  True  False  False
    print('good' in w)
    i += 1

# 练习
'''
 ['hello' , 'goods' , 'gooo' , 'world' , 'digot' , 'alphago']
  提示输入一个单词比如:hello，如果输入的单词在列表中则删除
  最后打印删除后的列表
'''

words = ['hello', 'goods', 'gooo', 'world', 'digot', 'alphago']
w = input('请输入一个单词:')
i = 0  # 表示下标
l = len(words)  # 5
while i < l:  # i<5
    if w in words[i]:
        del words[i]
        l -= 1
        # i-= 1
        continue
    i += 1
print(words)







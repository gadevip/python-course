# 字符串的内建函数:声明一个字符串，默认可以调用内建函数（系统准备好的一些函数)

# 第一部分:大小写相关的
# capitalize() title() istitle() upper() isupper() lower() islower ()
message = 'zhaorui is a beautiful girl !'

msg = message.capitalize()  #将字符串的第一个字符串转成大写的标识形式
print(msg)
msg = message.title()   #返回的是每个单词的首字母大写的字符串print(msg)

result = message.istitle()  #返回的结果是布尔类型的，True False
print(result)

msg = message.upper()   #将字符串全部转成大写的表示形式
print(msg)

result = msg.lower()   #将大写全部转小写
print(result)

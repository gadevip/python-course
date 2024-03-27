# https://www.baidu.com/s?wd=中文记录
# https://www.baidu.com/s?wd=%E4%B8%AD%E6%96%87%E8%AE%B0%E5%BD%95

# 字符串内建函数:encode 编码 decode 解码
# 编码: 网络应用
msg ='上课啦!认真听课!'  # 中文 

# gbk 中文 gb2312 简体中文  unicode
result =msg.encode('utf-8')
print(result)   # 转换成字节  b 二进制形式
# b'\xe4\xb8\x8a\xe8\xaf\xbe\xe5\x95\xa6!\xe8\xae\xa4\xe7\x9c\x9f\xe5\x90\xac\xe8\xaf\xbe!'

# 解码
m = result.decode('utf-8')
print(m)

# 字符串内建函数: startswith() endswith()返回值都是布尔类型True False
# startswith判断是否是以xxx开头的，
# 或者 endswith判断是否是以xxx结尾的

filename ='笔记.doc'
result = filename.endswith('doc')  #  filename是否是以txt结尾的
print(result)

s = 'hello'
result = s.startswith('he')
print(result)

# 应用:文件上传只能上传图片(jpg, png, bmp ,gif)

path = input('请选择文件:') # 输入 C:\foo\bar\desk_background.jpg

# 分析:要上传的文件的路径path----》文件名-----》通过文件名再判断是否是图片类型
p = path.rfind('\\')
filename = path[p+1:]   # 通过切片截取出来文件名
print(filename)         # desk_background.jpg

#判断是否是图片类型?
if filename.endswith('jpg') or filename.endswith('png') or filename.endswith('bmp'):
	print('是图片允许上传!')
else:
	print('不是图片格式，只能上传图片!')

'''
练习:
	给定一个路径,上传文件(记事本txt或者是图片jpg, png)
	如果不是对应格式的，允许重新指定上传文件，
	如果符合上传的规定则提示上传成功
'''
while True:
	path = input('请选择文件:') # 输入 C:\foo\bar\desk_background.jpg

	p = path.rfind('\\')
	filename = path[p+1:]   # 通过切片截取出来文件名
	print(filename)         # desk_background.jpg

	#判断是否是图片类型?
	if filename.endswith('jpg') or filename.endswith('png') or filename.endswith('txt'):
		print('允许上传,上传成功!')
		break
	else:
		print('不是图片和文本格式，上传失败!')

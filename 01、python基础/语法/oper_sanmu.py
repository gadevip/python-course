#三目运算符

#格式:表达式?真:假
#result =(8>10)?真’:假’
#print(result)


#python的格式:结果 if 表达式 else 结果
a = 6
b = 5
result = (a+b)  if a>b else (b-a)
'''
判断表达式是True还是False
如果是True则将if前面的内容进行运算，并将结果赋值成result
如果是False则将else后面的内容运算结果，并将结果赋值成result
'''
print(result)


# 运算符的优先级

'''
	排序：
	**  幂
	~   取反
	+ - （符号预算符） 
	* /  //  %
	+  -
	<<  >>
	&
	^
	|
	==  !=  >  >= <  <=
	is  is not
	not
	and
	or
'''
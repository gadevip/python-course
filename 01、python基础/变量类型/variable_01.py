# 可变和不可变
# 不可变:对象所指向的内存中的值是不可以改变
# 不可变的类型:int str float  元组tuple
num = 10
s1 = 'abc'
print(id(s1))
s1 = 'abcd'
print(id(s1))
t1 = (3, 5, 6)
print(id(t1))
t1 = (3, 5)
print(id(t1))

# 可变的:对象所指向的内存中的值是可以改变
# 可变类型:字典dict   列表list  集合 set
list1 = [1, 2, 3, 4, 5]
print(list1, id(list1))
list1.pop()
print(list1, id(list1))
dict1 = {1: 'aa', 2: ' bb'}
print(dict1, id(dict1))
dict1.pop(1)
print(dict1, id(dict1))

set1 = {2, 5, 8, 12}
print(set1, id(set1))

set1.pop()
print(set1, id(set1))

set1.discard(5)  # 从集合中移除一个元素
print(set1)

fset = frozenset(set1)  # frozenset冻结集合 不可变集合 没有add()  remove()方法
print(fset)

fset = frozenset({3, 6})
print(fset)

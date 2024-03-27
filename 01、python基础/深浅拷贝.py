'''
Python 直接赋值、浅拷贝和深度拷贝解析
直接赋值：其实就是对象的引用（别名）。
浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。
'''

# 字典浅拷贝实例
a = {1: [1, 2, 3]}
b = a   # 地址引用
b = a.copy()  # 地址引用
print(a, b)  # {1: [1, 2, 3]} {1: [1, 2, 3]}
a[1].append(4)  # {1: [1, 2, 3, 4]} {1: [1, 2, 3, 4]}
print(a, b)

# 深度拷贝需要引入 copy 模块：
import copy

c = copy.deepcopy(a)
print(a, c)     # {1: [1, 2, 3, 4]} {1: [1, 2, 3, 4]}
a[1].append(5)
print(a, c)     # {1: [1, 2, 3, 4, 5]} {1: [1, 2, 3, 4]}

# 实例
import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象

b = a  # 赋值，传对象的引用
c = copy.copy(a)  # 对象拷贝，浅拷贝
d = copy.deepcopy(a)  # 对象拷贝，深拷贝

a.append(5)  # 修改对象a
a[4].append('c')  # 修改对象a中的['a', 'b']数组对象

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)
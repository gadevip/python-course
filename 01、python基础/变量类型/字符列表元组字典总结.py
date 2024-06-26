'''
回顾:
数据类型:
字符串:
声明：
    ''    ""    ''''''

符号:
    +   *  in  not in   is   not is  []

获取字符串元素:
s = 'hello'
s[0] ~ s[len(s)-1]

切片:
s[start:end[:step]]     包前不包后

内置函数:
lower() upper() replace()
split()
find()  rfind()     lfind()
strip() lstrip()    rstrip()
join()
isalpha()
isdigit()


容器:
列表:list
    特点:保存多个元素，元秦有顺序。可以通过下标找到对应的元素。
            可以增加，删除，修改元素，查询

    内置函数:
        append extend insert
        remove  pop clear   del
        sort reverse index  count

元组:tuple 
    特点:保存多个元素。不可以增加，删除，修改元素。但是可以查询元素
    内置函数:index count
    支持下标操作:t = (1,2,3)  t[0]   t[1:]

字典:dict
    特点:键值对保存元素。键是唯一的，而值不唯一。可以支持对键值对的增删改查
    内置函数:
        增加(修改)键值对:dict1={}  dict1[key]=value
        删除键值对:dict1.pop()   dict1.popitem() dict1.clear()
        查询:items()  values()keys()

集合：set


可变元素和不可变元素
'''
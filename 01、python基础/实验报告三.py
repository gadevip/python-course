'''
实验报告三
列表和字典的操作
第1题
（1）	按照前面“由评委组的十名评委打分”的描述，
需要找一个列表记录每个评委的分数，此时列表中的元素是没有顺序的。
（2）	找出列表中的最高分和最低分，也就是先使用sort()方法按从低到高的顺序排列列表元素，
此时列表中位于开头的元素为最低分，位于结尾的元素为最高分。
（3）	去掉最高分和最低分就相当于删除列表的头尾元素，
可借助remove()方法删除列表的首位元素，借助pop()方法删除列表的尾部元素，此时列表中的元素是计算得分需要的列表。
（4）	计算得分操作也就是遍历列表求和、求平均数。
	熟练地创建列表并访问列表元素
	熟练地添加、删除、排列列表元素
# 评分列表
    score_li = []
# 总分
    total_score = 0

第2题
本案例要求编写程序，接收选手的姓名和票数，输出排序后的成绩。
掌握以下知识或技能：
	熟练创建字典和访问字典元素
	熟练列表的基本操作

2.	实例分析  key=value
（1）上面描述的选手的姓名与票数是一一对应的关系，因此可通过字典保存像这种关系的数据。
（2）按“选择的票数越多，排名越靠前”描述，此处需要比较字典中保存的票数，票数最高的选手位列第1名，票数最少的选手位列最后一名，可借助列表的sort()方法进行排序。
    player_info = {}  --->  字典{name:score}    {(name:score),(name:score)}
    name--->姓名
    player_info[name]  -->添加票数
    score --> 票数 浮点类型
    player.items ---> 对items 遍历 j
    li.append([j[1], j[0]])
    li = []  ---->    [[67.0, 'cc'], [68.0, 'aa'], [99.0, 'bb']]
    li.sort()


练习3
本案例要求编写程序，实现具备添加、查看、修改以及删除联系人信息功能的手机通讯录。
1.	实例目标
通过完成本实例，读者应掌握以下知识或技能： [{}, {}]
[{'姓名': 'gs', '手机号': '1222', '电子邮箱': '22@111.com', '联系地址': '活动后来'},
{'姓名': 'yy', '手机号': '125', '电子邮箱': '125@qq.com', '联系地址': 'adwa'}]
	熟练创建列表和操作列表元素
	熟练创建字典和操作字典元素
2.	实例分析
手机通讯录通常包含多个联系人，每个联系人都包含姓名、手机号、邮箱、地址等基本信息，且这些信息之间是相互对应的，因此这里可将联系人视为包含4个键值对的字典，将通讯录视为一个包含多个字典的数组，将通讯录中新增联系人、删除联系人、修改联系人、查看联系人的功能视为字典的增删改查操作。
根据以上分析可整理出以下基本实现思路：
（1）创建一个空列表，使用该列表存储联系人信息；
（2）打印通讯录的功能菜单；
（3）创建一个空字典，使用该字典存储联系人的姓名、手机号、邮箱和地址信息。
（4）接收用户输入的功能序号，并根据输入的序号执行相应的操作：用户输入“1”执行增加字典元素的操作；用户输入“2”执行查看字典的操作；用户输入“3”执行删除字典元素的操作；用户输入“4”执行修改字典元素的操作；用户输入“5”执行遍历字典元素的操作；用户输入“6”执行结束程序的操作。



'''

# score_li = []
# # 总分
# total_score = 0
# for i in range(1, 11):
#     score = float(input(f"请第{i}位评委输入评分：\n"))
#     score_li.append(score)
# score_li.sort()
# print(f"去掉最低分：{score_li[0]}")
# print(f"去掉最高分：{score_li[len(score_li) - 1]}")
# # 去掉最低分
# score_li.remove(score_li[0])
# # 去掉最高分
# score_li.pop()
# for j in score_li:
#     total_score += j
# print(f'选手最终得分为：{total_score / (len(score_li))}')

# player_info = {}
# li = []
# print('输入quit表示选手成绩录入完毕')
# while True:
#     name = input("请输入选手名称：\n")
#     if name == 'quit':
#         break
#     score = float(input("请输入选手票数：\n"))
#     player_info[name] = score
# items = player_info.items()
# print(items)
# for j in items:
#     li.append([j[1], j[0]])
# # 转换为list类型，进行排序
# li.sort()
# # print(li)
# # 获取选手索引
# count = len(li) - 1
# # 输出排名
# for i in range(1, len(li) + 1):
#     print(f"第{i}名：{li[count][1]},成绩为{li[count][0]}分")
#     count -= 1

person_info = []
print("=" * 20)
print('欢迎使用通讯录：')
print("1.添加联系人")
print("2.查看通讯录")
print("3.删除联系人")
print("4.修改联系人信息")
print("5.查找联系人")
print("6.退出")
print("=" * 20)
while True:
    per_dict = {}
    fun_num = input('请输入功能序号:')
    if fun_num == '1':
        per_name = input('请输入联系人的姓名：')
        phone_num = input('请输入联系人的手机号：')
        per_email = input('请输入联系人的邮箱：')
        per_address = input('请输入联系人的地址：')
        # 判断输入的是否为空
        if per_name.strip() == '':
            print('请输入正确信息')
            continue
        else:
            per_dict.update({'姓名': per_name,
                             '手机号': phone_num,
                             '电子邮箱': per_email,
                             '联系地址': per_address})
            person_info.append(per_dict)  # 保存到列表中
            print('保存成功')
    elif fun_num == '2':
        if len(person_info) == 0:
            print('通讯录无信息')
        for i in person_info:
            for title, info in i.items():
                print(title + ':' + info)
    elif fun_num == '3':  # 删除
        if len(person_info) != 0:
            del_name = input('请输入要删除的联系人姓名：')
            for i in person_info:
                if del_name in i.values():
                    person_info.remove(i)
                    print(person_info)
                    print('删除成功')
                else:
                    print('该联系人不在通讯录中')
        else:
            print('通讯录无信息')
    elif fun_num == '4':  # 修改
        if len(person_info) != 0:
            modi_info = input('请输入要修改联系人姓名：')
            for i in person_info:
                if modi_info in i.values():
                    # 获取所在元组在列表中的索引位置
                    index_num = person_info.index(i)
                    dict_cur_perinfo = person_info[index_num]
                    for title, info in dict_cur_perinfo.items():
                        print(title + ':' + info)
                    modi_name = input('请输入新的姓名：')
                    modi_phone = input('请输入新的手机号：')
                    modi_email = input('请输入新的邮箱：')
                    modi_address = input('请输入新的地址：')
                    dict_cur_perinfo.update(姓名=modi_name)
                    dict_cur_perinfo.update(手机号=modi_phone)
                    dict_cur_perinfo.update(电子邮箱=modi_email)
                    dict_cur_perinfo.update(联系地址=modi_address)
                    print(person_info)
        else:
            print('通讯录无信息')
    elif fun_num == '5':  # 查找
        if len(person_info) != 0:
            query_name = input('请输入要查找的联系人姓名：')
            for i in person_info:
                if query_name in i.values():
                    index_num = person_info.index(i)
                    for title, info in person_info[index_num].items():
                        print(title + ':' + info)
                    break
            else:
                print('该联系人不在通讯录中')
        else:
            print('通讯录无信息')
    elif fun_num == '6':
        print('退出')
        break
# 退出

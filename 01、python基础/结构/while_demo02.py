"""

掷骰子
1.欢迎进入xxxx游戏
2.输入用户名，默认用户是没有币
3.提示用户充值买币（100块钱30币，充值必须是100的倍数，充值不成功可以再次充值）
4.玩一局游戏币扣除2个币，猜大小（系统用随机数投掷骰子产生值）
5.只要猜对了奖励一个币，可以继续玩（想不想继续玩，也可以没有币自动退出）

"""
import random
print("*" * 50)
print("欢迎进入XX游乐城")
print("*" * 50)

username = input("请输入游客大名：")
money = 0                               # 金币数量  全局变量
answer = input("确定进入游戏吗（y/n）?")

while answer == "y":
    # 游戏币是否充足
    while money < 2 and answer == "y":
        # print("剩余金币{}".format(money))
        # if ansewer == "y"
        n = int(input("金币不足，请充值（10块钱2币，充值必须是10的倍数，充值不成功可以再次充值）："))
        # 充值金币判断
        if (n % 10 == 0) and (n > 0):
            money = (n // 10) * 2 + money          # 后面剩余的金币也要重新累加
        else:
            print("充值必须是10的倍数，充值不成功!")
            break

        print("当前拥有{}个币，玩一局游戏扣除2个币".format(money))

        print("进入游戏......")

        while True:  # 实现反复玩
            # 模拟骰子，产生骰子的值
            t1 = random.randint(1, 6)
            t2 = random.randint(1, 6)
            money -= 2
            # 两个骰子的值大于6 ----> 否则就是小
            print("系统骰子完毕，请猜大小")
            guess = input("请输入（大/小）：")
            print("开奖骰子大小结果：{}".format(t1 + t2))
            if ((t1 + t2) > 6 and guess == "大") or ((t1 + t2) <= 6 and guess == "小"):
                print("恭喜{}猜中了,本局游戏奖励1个游戏币".format(username))
                money += 1
                print("剩余金币{}".format(money))
            else:
                print("很遗憾猜错了！")
                print("剩余金币{}".format(money))

            answer = input("是否再来一局游戏，要扣除2个游戏币(y/n)：")
            if answer != "y" or money < 2:
                print("退出游戏")
                print("剩余金币{}".format(money))
                break
            else:
                print("继续开始新的游戏")
                continue


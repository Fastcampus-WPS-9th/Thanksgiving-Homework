import random
from .userinfo import *

class MakeMoney:

    def __init__(self, name):
        self.name = name

    def dice_game(self):
        print()
        print("------ 주사위 게임 ------\n")
        print("게임비 : -{}원".format(100))
        print("승  리 : +{}원".format(300))
        print("무승부 :  +{}원".format(50))


        start = input("\n게임을 시작하시겠습니까? (Y/N) ")
        if start == 'Y' or start == 'y':
            UserInfo.money -= 100

            comNum1 = random.randint(1, 6)
            comNum2 = random.randint(1, 6)
            comResult = comNum1 + comNum2

            userNum1 = random.randint(1, 6)
            userNum2 = random.randint(1, 6)
            userResult = userNum1 + userNum2

            print("")
            print("※ 컴퓨터")
            print("┌━─┐       ┌━─┐")
            print("│ %d│       │ %d│" % (comNum1, comNum2))
            print("└──┘       └──┘")

            print("")
            print("※ {}".format(self.name))
            print("┌━─┐       ┌━─┐")
            print("│ %d│       │ %d│" % (userNum1, userNum2))
            print("└──┘       └──┘")
            print("")

            if comResult > userResult:
                print("컴퓨터가 %d점 차이로 이겼습니다." %(comResult - userResult))
                print("보유금액: {}원".format(UserInfo.money))
                for _ in range(12):
                    print('=', end='')
                print()
            elif comResult < userResult:
                print("{}님이 {}점 차이로 이겼습니다.".format(self.name,(userResult - comResult)))
                UserInfo.money += 300
                print("보유금액: {}원".format(UserInfo.money))
                for _ in range(12):
                    print('=', end='')
                print()
            else:
                print("컴퓨터와 {}님이 비겼습니다.".format(self.name))
                UserInfo.money += 50
                print("보유금액: {}원".format(UserInfo.money))
                for _ in range(12):
                    print('=', end='')
                print()
        else:
            print("게임을 종료하겠습니다.")
            print("============")

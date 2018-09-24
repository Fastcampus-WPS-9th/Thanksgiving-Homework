import random
from .userinfo import *

class Upgrade:
    def __init__(self, name):
        self.name = name

    def basic_up(self):
        print()
        print("{0:-^16}\n".format(' 기본강화 '))
        print("무기 레벨이 +1씩 증가합니다.")
        print("(일정 확률로 +2 증가)")
        print("강화비: {}원".format(100))
        print("성공률: {}%".format(100))
        print()
        start = input("강화를 하시겠습니까? (Y/N) ")
        if start == 'Y' or start == 'y':
            UserInfo.money -= 100
            percent = random.randint(1, 201)
            if percent <= 5:
                print("찬란한 빛이 검 주위를 감싸고 있습니다.")
                UserInfo.level += 2
            else:
                print("\n{0:-^16}".format(" 강화 성공 "))
                UserInfo.level += 1
        else:
            print("강화를 종료합니다.")
            print("============")

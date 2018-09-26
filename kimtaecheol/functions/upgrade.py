import random
from .userinfo import *

class Upgrade:
    def __init__(self, name):
        self.name = name

    def basic_up(self):
        cost_table = {
        1: 100, 2: 100, 3: 100, 4: 110, 5: 130,
        6: 150, 7: 150, 8: 200, 9: 200, 10: 200,
        11: 230, 12: 250, 13: 250, 14: 300, 15: 300,
        16: 330, 17: 330, 18: 350, 19: 370, 20: 400,
        21: 400, 22: 400, 23: 430, 24: 430, 25: 450,
        26: 470, 27: 480, 28: 500, 29: 550, 30: 600,
        31: 800, 32: 1000, 33: 1400, 34: 1800, 35: 2000,
        36: 3000, 37: 3500, 38: 4000, 39: 4500, 40: 5000,
        41: 6000, 42: 6500, 43: 7000, 44: 8500, 45: 10000,
        }
        rate_table = {
        1: 100, 2: 100, 3: 97, 4: 95, 5: 95,
        6: 93, 7: 92, 8: 91, 9: 90, 10: 90,
        11: 87, 12: 85, 13: 83, 14: 80, 15: 77,
        16: 75, 17: 72, 18: 69, 19: 67, 20: 65,
        21: 63, 22: 60, 23: 57, 24: 55, 25: 50,
        26: 49, 27: 48, 28: 47, 29: 46, 30: 45,
        31: 40, 32: 39, 33: 38, 34: 35, 35: 30,
        36: 20, 37: 17, 38: 14, 39: 10, 40: 5,
        41: 4, 42: 3, 43: 3, 44: 2, 45: 1
        }
        print()
        print("{0:-^16}\n".format(' 기 본 강 화 '))
        print("무기 레벨이 +1씩 증가합니다")
        print("(일정 확률로 +2 증가)")
        print("강화비: {} 페나".format(cost_table[UserInfo.level]))
        print("성공률: {}%".format(rate_table[UserInfo.level]))
        print()
        start = input("강화를 하시겠습니까? (Y/N) ")
        if start == 'Y' or start == 'y':
            UserInfo.money -= cost_table[UserInfo.level]
            rate = random.randint(1, 100)
            if rate <= rate_table[UserInfo.level]:
                plus_2 = random.randint(1, 200)
                if plus_2 <= 3:
                    print("-- 찬란한 빛이 검 주위를 감싸고 있습니다 --")
                    print("+2 증가했습니다")
                    UserInfo.level += 2
                else:
                    print("\n{0:-^16}".format(" 강 화 성 공 "))
                    print("+1 증가했습니다")
                    UserInfo.level += 1
            else:
                print()
                print("{0:-^16}".format(" 강 화 실 패 "))
                print()
                print("============")
        else:
            print("강화를 종료합니다")
            print("============")

    def random_up(self):
        cost_table = {
        1: 100, 2: 100, 3: 100, 4: 110, 5: 130,
        6: 150, 7: 150, 8: 200, 9: 200, 10: 200,
        11: 230, 12: 250, 13: 250, 14: 300, 15: 300,
        16: 330, 17: 330, 18: 350, 19: 370, 20: 400,
        21: 400, 22: 400, 23: 430, 24: 430, 25: 450,
        26: 470, 27: 480, 28: 500, 29: 550, 30: 600,
        31: 800, 32: 1000, 33: 1400, 34: 1800, 35: 2000,
        36: 3000, 37: 3500, 38: 4000, 39: 4500, 40: 5000,
        41: 6000, 42: 6500, 43: 7000, 44: 8500, 45: 10000,
        }

        print()
        print("{0:-^16}\n".format(' 랜 덤 강 화 '))
        print("무기 레벨이 5 증가 또는 감소합니다")
        print("(일정 확률로 레벨이 1이 될 수 있습니다)")
        print("강화비: {} 페나".format(int(cost_table[UserInfo.level]) * 2))
        print()
        start = input("강화를 하시겠습니까? (Y/N) ")
        if start == 'Y' or start == 'y':
            UserInfo.money -= int(cost_table[UserInfo.level] * 2)
            rate = random.randint(0, 200)
            if rate == 0:
                UserInfo.level = 1
                print("레벨이 1로 초기화 되었습니다")
            elif rate < 11:
                UserInfo.level -= 5
                print("-5 감소했습니다")
                if UserInfo.level < 1:
                    UserInfo.level = 1
            elif rate < 21:
                UserInfo.level -= 4
                print("-4 감소했습니다")
                if UserInfo.level < 1:
                    UserInfo.level = 1
            elif rate < 41:
                UserInfo.level -= 3
                print("-3 감소했습니다")
                if UserInfo.level < 1:
                    UserInfo.level = 1
            elif rate < 71:
                UserInfo.level -= 2
                print("-2 감소했습니다")
                if UserInfo.level < 1:
                    UserInfo.level = 1
            elif rate < 110:
                UserInfo.level -= 1
                print("-1 감소했습니다")
                if UserInfo.level < 1:
                    UserInfo.level = 1
            elif rate < 155:
                UserInfo.level += 1
                print("+1 증가했습니다")
                if UserInfo.level > 45:
                    UserInfo.level = 45
            elif rate < 180:
                UserInfo.level += 2
                print("+2 증가했습니다")
                if UserInfo.level > 45:
                    UserInfo.level = 45
            elif rate < 190:
                UserInfo.level += 3
                print("+3 증가했습니다")
                if UserInfo.level > 45:
                    UserInfo.level = 45
            elif rate < 197:
                UserInfo.level += 4
                print("+4 증가했습니다")
                if UserInfo.level > 45:
                    UserInfo.level = 45
            else:
                UserInfo.level += 5
                print("+5 증가했습니다")
                if UserInfo.level > 45:
                    UserInfo.level = 45
        else:
            print("강화를 종료합니다")
            print("============")

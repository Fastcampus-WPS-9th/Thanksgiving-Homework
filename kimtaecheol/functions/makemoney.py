import random
from .userinfo import *

class MakeMoney:

    def __init__(self, name):
        self.name = name

    def dice_game(self):
        print()
        print("------ 주사위 게임 ------\n")
        print("참가비 : -{} 페나".format(100))
        print("승  리 : +{} 페나".format(300))
        print("무승부 :  +{} 페나".format(50))
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
                print("컴퓨터가 %d점 차이로 이겼습니다" %(comResult - userResult))
                print("보유 페나: {} 페나".format(UserInfo.money))
                for _ in range(12):
                    print('=', end='')
                print()
            elif comResult < userResult:
                print("{}님이 {}점 차이로 이겼습니다".format(self.name,(userResult - comResult)))
                UserInfo.money += 300
                print("보유 페나: {} 페나".format(UserInfo.money))
                for _ in range(12):
                    print('=', end='')
                print()
            else:
                print("컴퓨터와 {}님이 비겼습니다".format(self.name))
                UserInfo.money += 50
                print("보유 페나: {} 페나".format(UserInfo.money))
                for _ in range(12):
                    print('=', end='')
                print()
        else:
            print("게임을 종료하겠습니다")
            print("============")

    def guess_num(self):
        prize_table = {
        1:100000,
        2:70000,
        3:30000,
        4:10000,
        5:5000,
        6:2500,
        7:1000,}
        print()
        print("{0:-^16}".format("숫자 맞히기"))
        print(" 1 ~ 100 중에서 숫자 하나를 맞히는 게임")
        print("참가비: {:,} 페나".format(2000))
        print()
        print(" 시도 횟수    상 금")
        print(" ---------    -----")
        print("     1       {:,}".format(prize_table[1]))
        print("     2        {:,}".format(prize_table[2]))
        print("     3        {:,}".format(prize_table[3]))
        print("     4        {:,}".format(prize_table[4]))
        print("     5         {:,}".format(prize_table[5]))
        print("     6         {:,}".format(prize_table[6]))
        print("     7         {:,}".format(prize_table[7]))
        print("   그 외         500")
        start = input("\n게임을 시작하시겠습니까? (Y/N) ")
        if (start == 'Y' or start == 'y') and UserInfo.money < 2000 :
            print("보유하신 페나가 부족하여 게임을 할 수 없습니다")
            print("============")
        elif (start == 'Y' or start == 'y') and UserInfo.money >= 2000:
            UserInfo.money -= 2000
            comNum = random.randint(1, 100)
            tryCount = 0
            while True:
                for _ in range(20):
                    print('-',end='')
                print()
                userInput = int(input("숫자를 입력하세요: "))
                tryCount += 1

                if userInput < 1 or userInput > 100:
                    print("1 ~ 100 범위 내에서 입력해 주세요")
                    continue
                if userInput < comNum:
                    print("큰 숫자를 입력하세요")
                elif userInput > comNum:
                    print("작은 숫자를 입력하세요")
                elif userInput == comNum:
                    if tryCount > 7:
                        print("정답입니다. 시도 횟수 {}번 상금 500 페나입니다".format(tryCount))
                        print("============")
                        UserInfo.money += 500
                        break
                    elif tryCount <= 7:
                        print("정답입니다. 시도 횟수 {}번 상금 {:,} 페나입니다".format(tryCount, prize_table[tryCount]))
                        print("============")
                        UserInfo.money += prize_table[tryCount]
                        break
        else:
            print("게임을 종료하겠습니다")
            print("============")

    def lotto(self):
        print("한 줄에 {:,} 페나".format(1000))
        print("최대 5줄까지 가능")
        print()
        earn_money = 0
        prize_table = {
        1:100000000,
        2:50000000,
        3:10000000,
        4:3000000,
        5:500000,}
        print(" 시도 횟수    상 금")
        print(" ---------    -----")
        print("     1       {:,}".format(prize_table[1]))
        print("     2        {:,}".format(prize_table[2]))
        print("     3        {:,}".format(prize_table[3]))
        print("     4         {:,}".format(prize_table[4]))
        print("     5           {:,}".format(prize_table[5]))
        start = input("\n게임을 시작하시겠습니까? (Y/N) ")
        if start == 'Y' or start == 'y':
            # 금액에 따라 1 ~ 5줄 자동 생성
            while True:
                print("{0:-^26}".format(''))
                money = int(input("페나를 입력해 주세요: "))
                print("{0:-^26}".format(''))
                if (money < 1000) or (money > 5000) or (money % 1000 != 0):
                    print("1000 ~ 5000 페나를 입력해 주세요")
                    continue
                else: break
            if UserInfo.money < money:
                print("보유하신 페나가 부족하여 게임을 할 수 없습니다")
                print("============")
            else:
                UserInfo.money -= money
                # 당첨 번호
                win_lotto = random.sample(range(1, 46), 6)
                # 중복 확인 작업
                while True:
                    bonus_num = random.randint(1, 45)
                    if bonus_num in win_lotto:
                        continue
                    else:
                        break
                win_lotto.sort()
                i = 0
                num = 0
                if money == 1000:num = 1
                elif money == 2000: num = 2
                elif money == 3000: num = 3
                elif money == 4000: num = 4
                else: num = 5
                print()
                print()
                print("          나눔 Lotto 1/45     ")
                print("{0:-^34}".format(''))
                for _ in range(num):
                    count = 0
                    lotto = random.sample(range(1, 46), 6)
                    lotto.sort()
                    print(chr(65 + i) + "  자  동  " + ( ' %02d ' * 6 ) % tuple(lotto) )
                    # 자동 번호와 당첨 번호 비교
                    for j in range(len(lotto)):
                        for k in range(len(lotto)):
                            if lotto[j] == win_lotto[k]:
                                count += 1
                            else: continue
                    if count == 6:
                        earn_money += prize_table[1]
                    elif (count == 5) and (bonus_num in lotto):
                        earn_money += prize_table[2]
                    elif count == 5:
                        earn_money += prize_table[3]
                    elif count == 4:
                        earn_money += prize_table[4]
                    elif count == 3:
                        earn_money += prize_table[5]
                    i += 1
                UserInfo.money += earn_money
                print("{0:-^34}".format(''))
                print("페    나                  ￦ {:,}".format(money))
                print("{0:=^34}".format(''))
                print("당 첨 번 호" + ( ' %02d ' * 6 ) % tuple(win_lotto))
                print("보너스 번호 " + '{0:02}'.format(bonus_num))
                print("{0:-^34}".format(''))
                print("당 첨 페 나 {0:>22}".format(earn_money,','))
                print("{0:-^34}".format(''))
        else:
            print("게임을 종료하겠습니다")
            print("============")

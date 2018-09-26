from functions import *
import string
import re

def start():
    printable = string.printable
    printable = re.findall('\D', printable)
    for _ in range(40):
        print()
    for _ in range(20):
        print("=", end='')
    print()
    print()
    print("{0:^20}".format("Strong Sword"))
    print()
    for _ in range(20):
        print('=', end='')
    print()
    print()
    print("{0:^17}".format("[1] 새 게 임"))
    print("{0:^17}".format("[2] 명예전당"))
    print("{0:^17}".format(" [3] 종    료"))
    print()
    for _ in range(20):
        print('-', end='')
    print()
    while True:
        choice = input("   선택해주세요: ")
        if (choice in printable):
            continue
        if int(choice) == 1:
            return make_id()
        elif int(choice) == 2:
            return show_record()
        elif int(choice) == 3:
            print("   게임을 종료합니다")
            break
        elif (int(choice) < 1) or (int(choice) > 2):
            continue

def make_id():
    while True:
        print()
        for _ in range(30):
            print('-', end='')
        print()
        char_name = input("캐릭터명을 입력해주세요: ")
        user = UserInfo(char_name)
        for _ in range(30):
            print('-', end='')
        print()
        if char_name:
            return main(user)

def main(user):
    printable = string.printable
    printable = re.findall('\D', printable)
    while True:
        if UserInfo.money < 100:
            print("{}님께서 보유하신 페나가 부족하여\n더 이상 게임을 진행할 수 없습니다".format(user))
            break
        elif UserInfo.level == 45:
            print("{0:-^50}".format(" 축 하 합 니 다 "))
            print("{}님은 최종 레벨 달성하여 데스나이트 검을 얻으셨습니다".format(user))
            print("{0:-^55}".format(''))
            break
        print()
        print(" [1] 내 정 보")
        print(" [2] 돈 벌 기")
        print(" [3] 강    화")
        print(" [4] 종    료")
        print()
        print("{0:=^12}".format(''), end='')
        choice = input(" 선택해주세요: ")
        # 문자 입력 시 다시 입력
        if  (choice in printable):
            print("1 ~ 4 입력해주세요")
            print("============")
            continue
        # 숫자 입력 시 실행. 범위를 넘어서면 다시 입력
        if int(choice) == 1:
            print(user.show_info)
        elif int(choice) == 2:
            return makemoney_list(user)
        elif int(choice) == 3:
            return upgrade_item(user)
        elif int(choice) == 4:
            return print("게임을 종료합니다")
        elif (int(choice) < 1) or (int(choice) > 4):
            print("1 ~ 4 입력해주세요")
            print("============")
            continue

def makemoney_list(user):
    printable = string.printable
    printable = re.findall('\D', printable)
    while True:
        if UserInfo.money < 100:
            print("{}님께서 보유하신 페나가 부족하여\n더 이상 게임을 진행할 수 없습니다".format(user))
            break
        print()
        print(" [1] 주  사  위")
        print(" [2] 숫자맞히기")
        print(" [3] 로      또")
        print(" [4] 뒤 로 가 기")
        print()
        print("{0:=^12}".format(''), end='')
        choice = input(" 선택해주세요: ")
        # 문자 입력 시 다시 입력
        if  choice in printable:
            print("1 ~ 4 입력해주세요")
            print("============")
            continue
        # 숫자 입력 시 실행. 범위를 넘어서면 다시 입력
        if int(choice) == 1:
            game = MakeMoney(user)
            game.dice_game()
        elif int(choice) == 2:
            game = MakeMoney(user)
            game.guess_num()
        elif int(choice) == 3:
            game = MakeMoney(user)
            game.lotto()
        elif int(choice) == 4:
            return main(user)
        elif (int(choice) < 1) or (int(choice) > 4):
            print("1 ~ 4 입력해주세요")
            print("============")
            continue

def upgrade_item(user):
    printable = string.printable
    printable = re.findall('\D', printable)
    while True:
        if UserInfo.money < 100:
            print("{}님께서 보유하신 페나가 부족하여\n더 이상 게임을 진행할 수 없습니다".format(user))
            break
        elif UserInfo.level == 2:
            print("{0:-^50}".format(" 축 하 합 니 다 "))
            print("{}님은 최종 레벨을 달성하여 데스나이트 검을 얻으셨습니다".format(user))
            print("{0:-^55}".format(''))
            write_record(user)
            break
        print()
        print(" [1] 기 본 강 화")
        print(" [2] 랜 덤 강 화")
        print(" [3] 뒤 로 가 기")
        print()
        print("{0:=^12}".format(''), end='')
        choice = input(" 선택해주세요: ")
        # 문자 입력 시 다시 입력
        if  choice in printable:
            print("1 ~ 3 입력해주세요")
            print("============")
            continue
        # 숫자 입력 시 실행. 범위를 넘어서면 다시 입력
        if int(choice) == 1:
            upgrade = Upgrade(user)
            upgrade.basic_up()
        elif int(choice) == 2:
            upgrade = Upgrade(user)
            upgrade.random_up()
        elif int(choice) == 3:
            return main(user)
        elif (int(choice) < 1) or (int(choice) > 3):
            print("1 ~ 3 입력해주세요")
            print("============")
            continue

def write_record(user):
    txt = "{:^22}".format(user.name)
    with open('./honor/record.txt', 'at') as f:
        f.write(txt)

def show_record():
    print()
    print()
    print('{:=^30}'.format(''))
    print('{0:^24}'.format('명 예 전 당'))
    print('{0:^26}'.format('--------------'))
    try:
        f = open('./honor/record.txt', 'rt')
        lines = f.readlines()
        f.close()
        for line in lines:
            print(line)
        for _ in range(4):
            print()
        choice = input('[1] 뒤로가기 : ')
        if choice == '1':
            return start()

    except FileNotFoundError:
        return start()

if __name__ == '__main__':
    start()

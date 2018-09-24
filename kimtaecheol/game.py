from functions import *

def start():
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
    print("{0:^17}".format("[1] 게임 시작"))
    print("{0:^17}".format("[2] 게임 종료"))
    print()
    for _ in range(20):
        print('-', end='')
    print()
    choice = int(input("    선택해주세요: "))
    if choice == 1:
        make_id()
    else:
        print("   게임을 종료합니다.")

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
            main(user)
            break

def main(user):
    while True:
        if UserInfo.money < 100:
            print("{}님은 더 이상 게임을 진행할 수 없습니다.".format(user))
            break
        print()
        print(" [1] 내 정 보")
        print(" [2] 돈 벌 기")
        print(" [3] 강    화")
        print(" [4] 종    료")
        print()
        for _ in range(12):
            print('=', end='')
        choice = int(input(" 선택해주세요: "))
        if choice == 1:
            print(user.show_info)
        elif choice == 2:
            makemoney_list(user)
        elif choice == 3:
            upgrade_item(user)
        elif choice == 4:
            print("게임을 종료합니다.")
            break

def makemoney_list(user):
    game_list = []
    print()
    print(" [1] 주  사  위")
    print(" [2] 숫자맞히기(미구현)")
    print(" [3] 로      또(미구현)")
    print(" [4] 뒤 로 가 기")
    print()
    for _ in range(12):
        print('=', end='')
    choice = int(input(" 선택해주세요: "))
    if choice == 1:
        game_list.append(MakeMoney(user))
        game_list[0].dice_game()
    elif choice == 4:
        main(user)

def upgrade_item(user):
    upgrade_list = []
    print()
    print(" [1] 기 본 강 화")
    print(" [2] 랜 덤 강 화(미구현)")
    print(" [3] 뒤 로 가 기")
    print()
    for _ in range(12):
        print('=', end='')
    choice = int(input(" 선택해주세요: "))
    if choice == 1:
        upgrade_list.append(Upgrade(user))
        upgrade_list[0].basic_up()
    elif choice == 3:
        main(user)

start()

from functions import *

def start_game():
    print_rank()
    sword = Sword()
    user = User(input('너의 이름은? : '))
    while True:
        if user.money < 300 and sword.now_enchant >= 2:
            write_rank(user)
            print_rank()
            print("돈이 부족하여 자동으로 종료됩니다.")
            break
        print_menu(sword, user)
        i_new_weapon = sel_menu(sword, user)
        if i_new_weapon == False:
            sword = Sword()
        elif i_new_weapon == 2:
            write_rank(user)
            print_rank()
            print("게임을 종료합니다!")
            break

if __name__ == "__main__":
    start_game()

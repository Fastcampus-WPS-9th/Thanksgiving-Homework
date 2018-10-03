from functions import *


from functions import *
import random

def turn_on():
    print('= Turn on game =')
    name = input('\n유저 이름을 입력해주세요\n입력: ')
    user1 = User(name)
    sword = Sword(name)
    while True:
        print(f'{user1}님 반갑습니다!!\n'
              '지금부터 검 강화게임을 시작하도록 하겠습니다'
              )
        choice = input(
            '번호를 입력해주세요\n'
            ' 1: 검 강화하기\n'
            ' 0: 게임 나가기\n'
            'Input: '
        )
        if choice == '1':
            print(f'{sword.name}을 강화시작 하겠습니다!')
            sword.upgrade()
            game_continue = 'y'
            if sword.strength < 10:
                while True:
                    game_continue = input('계속 강화하시겠습니까(y/n) : ')
                    if game_continue == 'y':
                        sword.upgrade()
                        if sword.strength >= 10:
                            break
                    elif game_continue == 'n':
                        break
                    elif game_continue != 'y':
                        print('잘못 입력하셨습니다.\n''다시 입력해주세요!')
                        continue
                        
            print('10이상은 강화 할수 없습니다\n수고하셨습니다.')
            break
        elif choice == '0':
            break
        else:
            print('선택지 항목에서 벗어났습니다\n'
                  '다시 선택해주세요')
        print('--------------------------')
    print('= 게임 종료 =')

if __name__ == '__main__':
    turn_on()

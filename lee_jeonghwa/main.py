import time
import random

from functions import Users, Ranking, MultiplicationGame

def turn_on():
    print('''
    *****************************
    **구구단 게임을 시작합니다**
    *****************************


    ''')
    print('**랭킹 5위까지 보여드립니다**')
    print('********************************')
    ranking = Ranking()
    ranking.show_ranking()


    print('''
    2에서 12단까지 구구단 게임입니다
    10문제를 빠른 시간안에 맞추면 됩니다.
    한문제 틀릴 때 마다 3초의 패널티가 있습니다.
    3문제 틀릴시 실패!!
    ''')

    user_name = input('이름을 입력하세요: ')
    user = Users(user_name) #user 생성

    start_char = input(f'{user.name}님 시작하시겠습니까?[y]')

    if start_char == 'y':
        game = MultiplicationGame(user)
        game.repeat_game()

    else:
        print('''
        **************************
        ** 구구단 게입을 종료합니다 **
        **************************
        ''')


if __name__ == '__main__':
    turn_on()

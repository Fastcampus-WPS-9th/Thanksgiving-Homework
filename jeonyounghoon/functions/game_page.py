import random
from .User import *
def game_page():
 
    while True:

        print('사용자의 이름을 입력해주세요.초기 생명력은 10 게임을 나가거나 생명을 다 쓰면 게임은 끝납니다.')
        
        name = input()
        user=User(name)
            
        
        while True:
            
            number = random.randint(1,10)
            print(f'{user.name}님 1부터 10안의 숫자를 고르세요')

            while True:
                guess = input( )

                if int(guess)>10 or int(guess)<0:
                    print('숫자를 다시 입력하세요\n')
                    continue

                if number>int(guess):
                    user.life-=1
                    print('숫자를 올려보세요')
                    print(f'{user.name}의 현재 생명은 {user.life}입니다.\n')
                    continue

                if number<int(guess):
                    user.life-=1
                    print('숫자를 내려보세요')
                    print(f'{user.name}님의 현재 생명은 {user.life}입니다.\n')
                    continue

                if number==int(guess):
                    print('정답입니다. 점수를 획득하셨습니다.\n')
                    user.score+=1
                    print(f'{user.name}님의 점수는 {user.score}점 이며 남은 생명은 {user.life}입니다.\n')
                    break


            print('게임이 진행되길 원하면 엔터 종료를 원하면 종료를 입력해주세요\n')
            user_select=input()
            if user_select == '종료':
                break

            else:
                continue
        print('완전한 종료를 원하면 종료를 한번 더 입력해주세요 엔터를 누르면 새로운 사용자로 게임이 시작됩니다.')
        final_select=input()
        if final_select=='종료':
            break
        else:
            continue


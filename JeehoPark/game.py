import functions

def turn_on():
    print('= 상자깡 시뮬레이터 =')
    print('당신의 운을 시험하십시오')

    while True:
        choice = input(
                '무엇을 하시겠습니까\n'
                ' 1: 게임시작\n'
                ' 2: 결과보\n'
                ' 0: Exit\n'기
                'Input : ')
        if choice == '0':
            break
        elif choice == '1':
            functions.game_start.game_start()
        elif choice == '2':
            with open('./save_data/save.txt', 'rt') as f:
                a = f.read()
                print(a)
        else:
            print('잘못 선택 하셨습니다.')
        print('---------------------------')

    print('= Turn off game =')

if __name__ == '__main__':
    turn_on()


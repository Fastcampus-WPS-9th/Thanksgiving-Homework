from functions import game_config

def game_start():
    hogu_name = input('이름을 입력하세요\n'
                      '이름: ')
    p1 = game_config.hogu(hogu_name)
    lotto = game_config.lottery()

    print(f'당신은 {p1.money}원을 가지고 시작합니다. 최대 10번의 기회가 주어집니다.\n'
          '상자깡을 통해 최대한 많은 돈을 모으십시오.\n'
          '상자깡을 시작합니다.'
          )

    while p1.money > 0 and p1.timeleft >= 0:
        choice = input(
            '무엇을 지르시겠습니까?\n\n'
            ' 1: 쫄보 패키지 (10원 사용; 성공시 20원 반환)\n'
            ' 2: 애매 패키지 (50원 사용; 성공시 120원 반환)\n'
            ' 3: 대박 패키지 (100원 사용; 성공시 300원 반환)\n'
            ' 모든 패키지는 일확천금의 기회가 있습니다.\n'
            ' 선택 : ')
        if choice == '1':
            lotto.box10(p1)
        elif choice == '2':
            lotto.box50(p1)
        elif choice == '3':
            lotto.box100(p1)
        else:
            print('잘못 선택하셨습니다.')
        print('---------------------------')
    else:
        if p1.money <= 0:
            print('게임 오버! 과도한 도박은 인생을 망칠 수 있습니다.')
        else:
            with open('./save_data/save.txt', 'at') as f:
                a = f.write('\n 이름: {} 최종금액: {}'.format(p1.name, p1.money))
                print('게임 끝! 게임 결과가 등록되었습니다')
                print(f'{p1.name}의 최종 결과 금액은 {p1.money}원 입니다.')


if __name__ == '__main__':
    game_start()


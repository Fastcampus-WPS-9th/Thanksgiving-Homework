from functions import ran, status, vs

print('라이벌과의 패배 이후, 자신의 힘과 비례해서 강해지는 던전에 들어오게되었다.\n'
     '여기서 강해진 뒤 라이벌과의 싸움을 이기는 것이 목표이다.')
def turn_on():
    game_count = 1
    name = input('이름을 입력해주세요.')
    print(f'{name}이 던전에 입장하였습니다.')
    while True:
        choice = input(
            '1: 능력치 보기\n'
            '2: 주사위 굴리기\n'
            '3: 결투 신청\n'
            '4: 랭킹보기\n'
            '0: 게임 종료\n'
        )
        if choice == '1':
            print('능력치를 보여줍니다.')
            status.show_status()
        elif choice == '2':
            while True:
                if ran.dice_count <= game_count:
                    print('주사위를 굴립니다.')
                    ran.dice()
                else:
                    print('횟수를 초과했습니다.')
                break
        elif choice == '3': 
            print(
                    f'{ran.dice_count}층 보스의 체력은 {status.boss_hp}\n'
                    f'공격력은 {status.boss_attack}\n'
                    f'방어력은 {status.boss_defence}입니다\n'
                    )
            answer = input('싸우시겠습니까?(y/n)')
            if answer == 'y':
                vs.versus()
                if vs.game_status == 'lose':
                    print('패배하셨습니다.')
                    with open('save_data/record.txt', 'at') as write_record:
                        write_record.write(f'{name}, {ran.dice_count}\n')
                        #with open('save_data/record.txt', 'rt') as ranker:
                            #if 
                    break
                else:
                    game_count += 1
                    print(f'{ran.dice_count}층 보스를 쓰려트렸습니다.')
            elif answer == 'n':
                print('단련하세요')
            else:
                print('잘못입력하셨습니다.')
        elif choice == '4':
            print('-------랭킹-------')
            with open('save_data/record.txt', 'rt') as read_record:
                read_line = 0
                ranking = ''
                while True:
#                while read_line < 15:
#                    read_line += 1
                    line = read_record.readline()
                    if not line:
                        break
                    ranking += line
                print(ranking)
        elif choice == '0':
            print('게임이 종료되었습니다.')
            break
        else:
            print('잘못 입력하셨습니다.')
        print('-_-_-_-_-_-_-_-_-_-_-_-_')

if __name__ == '__main__':
    turn_on()

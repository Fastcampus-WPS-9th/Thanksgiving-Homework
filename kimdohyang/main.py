from time import sleep
from functions import *

# 랭킹 출력
def print_rank():
    before_rank = read_rank()
    print("{:=^40}".format(" RANKING "))
    for i, item in enumerate(before_rank, start=1):
        print(f"{i}위 {Player}님 : {legendary_pokemon.turn}턴")


# 랭킹 읽기
def read_rank():
    before_rank = []
    try:
        with open('./save_data/record.txt', 'rt') as f:
            while True:
                line = f.readline()
                if not line: break
                ranking = line.split(', ')
                # Delete \n
                ranking[2] = ranking[2][:-1]
                before_rank.append(tuple(ranking))
    except FileNotFoundError as e:
        pass
    finally:
        return before_rank


# 랭킹 쓰기
def write_rank():
    before_rank = read_rank()
    my_rank = (Player, str(legendary_pokemon.turn))
    before_rank.append(my_rank)
    after_rank = sorted(before_rank, key=lambda x: int(x[1]), reverse=True)
    try:
        with open('./save_data/record.txt', 'wt') as f:
            for i in after_rank[:5]:
                string = ", ".join(i) + "\n"
                f.write(string)

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
#     import Pokegame
#     게임 실행 선택/ 랭킹 보기 선택/ 나가기 선택
    sentence = '전설의 포켓몬 포획 시뮬레이션 게임'
    title_intro = sentence.center(50,'=')
    print(title_intro+'\n')
    select_button = input(
    '원하는 번호를 입력해주세요.\n1:게임 실행\n2:랭킹 보기\n3:나가기\n'
    )

    if select_button == '3':
        quit()

    elif select_button == '2':
        print_rank()

    elif select_button == '1':
        Player = input('당신의 이름을 입력해주세요.\n')
        start_doc = '''
        \n선택한 3마리의 포켓몬으로 팀을 구성해 전설의 포켓몬을 포획하면 승리합니다.\n
        만약 자신의 포켓몬이 모두 쓰러지거나 몬스터볼을 다 소진할 경우 패배하게됩니다.\n
        3개의 몬스터볼과 1개의 하이퍼볼이 주어집니다. 신중하게 사용하세요.\n
        포켓몬의 체력이 낮을수록 포획 확률이 증가합니다!\n
        전설의 포켓몬을 포획하지 못한채 쓰러뜨릴 경우 무승부가 됩니다.\n
        몇 턴 내에 전설의 포켓몬을 포획하는가로 랭킹이 결정됩니다\n
        도전하고 싶은 전설의 포켓몬의 번호를 입력하세요.\n
        ****이 게임의 선택지는 모두 번호를 입력합니다. 주의해주세요!****\n
        ===================================================\n\n'
        '''
        print(start_doc)
        articuno = Articuno()
        groudon = Groudon()
        mewtwo = Mewtwo()

        charizard = Charizard()
        dragonite = Dragonite()
        snorlax = ()
        blastoise = ()
        pikachu = Pikachu()
        electrode = Electrode()

        legendary_list = [articuno, groudon, mewtwo]
        legendary_print_list = ['프리져', '그란돈', '뮤츠']
        print('\n\n'.join([f'{index}:{legendary}' for index, legendary in enumerate(legendary_print_list, start=1)]))
        select_legendary = input()
        legendary_pokemon = legendary_list[int(select_legendary) - 1]
        print(f'\n===================================================\n'
              f'전설의 포켓몬 {legendary_print_list[int(select_legendary)-1]}에 도전합니다!\n'
              f'\n===================================================\n'
              f'당신의 팀을 구성해주세요. 각 포켓몬마다 특성이 다르니 잘 조합하세요!\n'
              f'고른 순서가 포켓몬 배틀의 출전 순서이므로 신중하게 골라주세요.\n'
              )

        pokemon_list = [charizard, dragonite, snorlax, blastoise, pikachu, electrode]
        pokemon_print_list = ['리자몽', '망나뇽', '잠만보', '거북왕', '피카츄', '붐볼']
        battle_pokemon_list = []
        battle_pokemon_print_list = []
        print('\n\n'.join([f'{index}:{pokemon}' for index, pokemon in enumerate(pokemon_print_list, start=1)]))

        while True:
            select_pokemon = input()
            battle_pokemon_list.append(pokemon_list[int(select_pokemon) - 1])
            battle_pokemon_print_list.append(pokemon_print_list[int(select_pokemon) - 1])
            if len(battle_pokemon_list) < 3:
                print('다음 포켓몬을 골라주세요!')
            else:
                break

        print(f'\n===================================================\n'
              f'당신의 팀은 {battle_pokemon_print_list}입니다!\n'
              f'곧 전투가 시작됩니다. 포켓몬 배틀을 준비하세요!\n'
              )
        fn = 0
        player_pokemon = battle_pokemon_list[fn]
        sleep(2)

        while True:
            print(f'\n\n++++++++++++++++++++++++++++++++++++++++++++++++\n\n')
            player_pokemon.legendary_pokemon = legendary_pokemon
            legendary_pokemon.player_pokemon = player_pokemon
            legendary_pokemon.poke_info()
            player_pokemon.poke_info()

            legendary_pokemon.Do_attack()
            if player_pokemon.current_hp <= 0:
                print(f'{player_pokemon.name}이 쓰러졌다!')
                fn += 1
                if fn < 4:
                    player_pokemon = battle_pokemon_list[fn]
                    print(f'{player_pokemon.name}이 출전한다!')
                else:
                    print(
                        f'{Player}의 모든 포켓몬이 쓰러졌습니다. 다시 도전하세요!\n'
                        f'===================GAME END====================\n'
                        f'잠시 후 게임이 종료됩니다.'
                    )
                    sleep(3)
                    quit()

            print(
                f'{Player}의 턴입니다. 다음 행동을 선택해주세요.\n'
                f'1: 공격\n2: 포획\n'
            )

            turn_choice = input()
            player_pokemon.Do_turn(turn_choice)

            if player_pokemon.current_hp <= 0:
                fn += 1
                if fn < 4:
                    player_pokemon = battle_pokemon_list[fn]
                else:
                    print(
                        f'{Plyaer}의 모든 포켓몬이 쓰러졌습니다. 다시 도전하세요!\n'
                        f'===================GAME END====================\n'
                        f'잠시 후 게임이 종료됩니다.'
                    )
                    sleep(3)
                    quit()

            if legendary_pokemon.current_hp <= 0:
                print(
                    f'{legendary_pokemon}이 쓰러졌습니다.\n'
                    f'{Player}는 전설의 포켓몬을 포획하는데 실패했습니다.\n'
                    f'====================Draw Game====================\n'
                    f'잠시 후 게임이 종료됩니다.'
                )
                sleep(3)
                quit()

    else:
        print('잘못된 입력입니다. 다시 게임 스크립트를 실행해주세요.')
        quit()
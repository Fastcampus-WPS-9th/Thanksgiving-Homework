from functions import *

updated_records = []
def turn_on():
    print('---Play Game---')
    
    while True:
        main_menu = input('[1] 게 임 시 작\n[2] 기 록 보 기\n[0] 게 임 종 료: \n')
        if main_menu == '1':
            player = input('캐릭터 이름을 입력하세요 : ')
            type_of = input('캐릭터 속성을 입력하세요(fire / ice) : ')
            character = User(player, type_of)
            monster = Monster()
            print(f'{player}가 생성되었습니다.\n{player}의 정보입니다.\n')
            character.user_info()
            print('---------------------------')
            print(f'{monster.name}가 나타났습니다.')
            oppor = Rock_s_p()
            play_game = True
            while play_game:
                if character.hp > 0 and monster.hp > 0:
                    oppor.chance(character, monster)
                    if character.result > monster.result:
                        print('----------------------------')
                        print(f'{character.name}가 이겼습니다.')
                        print('\n')
                        attack_chance = input('공격 방법을 선택하세요\n[1] 기 본 공 격\n[2] 스 킬 공 격 \n')
                        if attack_chance == '1':
                            character.user_hit(monster)
                            character.user_info()
                            monster.mon_info()
                        elif attack_chance == '2':
                            character.user_skill(monster)
                            character.user_info()
                            monster.mon_info()
                        else:
                            print('1, 2중에 하나를 다시 입력하세요')

                    elif character.result < monster.result:
                        print('--------------------------')
                        print(f'{monster.name}가 이겼습니다.')
                        attack_chance = random.randint(1,2)
                        if attack_chance == 1:
                            print('\n')
                            print(f'{monster.name}가 [기 본 공 격]을 가했습니다')
                            print('----------------------------------')
                            monster.mon_hit(character)
                            character.user_info()
                            monster.mon_info()
                        else:
                            print('\n')
                            print(f'{monster.name}가 [스 킬]을 사용했습니다')
                            print('--------------------------------')
                            monster.mon_skill(character)
                            character.user_info()
                            monster.mon_info()
                            
                elif monster.hp <= 0:
                    print(f'{character.result}번의 가위바위보 승리로 {monster.name}을 잡았습니다') 
                    with open('./save_data/record.txt', 'rt') as file:
                        user_record = ' '.join([character.name, str(character.result)])

                    if user_record not in updated_records:
                        print(f'{character.name}님의 기록 ({character.result})가 기록되었습니다')
                        updated_records.append(user_record)
                    
                    with open('./save_data/record.txt', 'wt') as f:
                            f.write('\n'.join(updated_records))
                    
                    break
                    
                elif character.hp <= 0:
                    print('gmae over')
                    print('\n')
                    break
                    

        elif main_menu == '2':
            f = open('./save_data/record.txt', 'rt')
            print(f.read())
            
                
        
        elif main_menu == '0':
            print('게임을 종료합니다')
            break
            
        else:
            print('[1번] [2번] [3번] 중 에서 골라주세요.')
            
        
if __name__ == '__main__':
    turn_on()

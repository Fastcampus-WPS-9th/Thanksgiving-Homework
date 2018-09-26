import random
import operator
import user

class Game:
    def __init__(self):
        self.rock_scissor_paper = ['가위', '바위', '보']
    
    def write_score(self, name, score):
        text = name + " " + str(score) + "\n"
        with open('score.txt', 'a') as f:
            f.write(text)
    
    def show_ranker(self):
        with open('score.txt', 'r') as f:
            ranked = {}
            while True:
                line = f.readline()
                line = line[:-1]
                line = line.split(" ")
                if not line or line[0] == '':
                    break
                ranked[line[0]] = int(line[1])
                
            if (len(ranked) > 0):
                sorted_list = sorted(ranked.items(), key=operator.itemgetter(1), reverse=True)                
                print("랭커 점수")
                print('--------------------------')
                
                if len(sorted_list) < 3:
                    for idx, item in enumerate(sorted_list, start=1):
                        print(f'{idx}. {item[0]} : {item[1]}점')
                else:
                    for idx, item in enumerate(sorted_list, start=1):
                        print(f'{idx}. {item[0]} : {item[1]}점')
                        if idx == 3:
                            break
                print('--------------------------')

        
    def turn_on(self):
        with open('score.txt', 'w') as f:
            f.write('')
        print('= Turn on game =')

        while True:
            choice = input(
                '무엇을 하시겠습니까?\n'
                ' 1: 계정 생성\n'
                ' 2: 게임 플레이\n'
                ' 0: 게임 종료\n'
                'Input: '
            )
            if choice == '1':
                user1 = user.User()
                print(f'"{user1.name}" 계정이 생성됐습니다.')
            elif choice == '2':
                try:
                    if user1.name == None:
                        print('계정을 먼저 생성해 주십시오.')
                        continue
                    self.show_ranker()
                    while user1.life > 0:
                        print()
                        print(f"현재 라이프는 {user1.life}, 점수는 {user1.score}점 입니다.")
                        enemy_value = self.rock_scissor_paper[random.randrange(0,3)]
                        try:
                            my_number = int(input(
                                "1: 가위, 2: 바위, 3: 보 중 하나를 골라주세요.")) - 1
                            my_value = self.rock_scissor_paper[my_number]
                        except IndexError:
                            print('가위, 바위, 보 중 하나를 선택해주세요.')
                            continue
                        except ValueError:
                            print('가위, 바위, 보 중 하나를 선택해주세요.')
                            continue
                        print(f'상대: {enemy_value}, 나: {my_value}')
                        if enemy_value == my_value:
                            print("비겼습니다.")
                            continue
                        elif my_value == "가위":
                            if enemy_value == "바위":
                                print("졌습니다.")
                                user1.life -= 1
                                continue
                            elif enemy_value == "보":
                                print("이겼습니다.")
                                user1.score += 10
                                continue
                        elif my_value == "바위":
                            if enemy_value == "보":
                                print("졌습니다.")
                                user1.life -= 1
                                continue
                            elif enemy_value == "가위":
                                print("이겼습니다.")
                                user1.score += 10
                                continue
                        elif my_value == "보":
                            if enemy_value == "가위":
                                print("졌습니다.")
                                user1.life -= 1
                                continue
                            elif enemy_value == "바위":
                                print("이겼습니다.")
                                user1.score += 10
                                continue
                except UnboundLocalError:
                    print('계정을 먼저 생성해 주십시오.')
                    continue
                print()
                print(f'{user1.name}의 점수는 {user1.score}점 입니다.')
                print("점수가 기록됐습니다.")
                self.write_score(user1.name, user1.score)
                user1.name = None
                user1.score = 0
            elif choice == '0':
                break
            else:
                print('해당 선택지는 존재하지 않습니다.')
            print('--------------------------')
        print('= Turn off game =')

if __name__ == '__main__':
    g1 = Game()
    g1.turn_on()

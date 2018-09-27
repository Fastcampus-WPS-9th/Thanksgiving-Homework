import random

class Rock_s_p:
    def __init__(self):
        pass
    def chance(self, user, target):
        while True:
            player = input('가위바위보를 합니다 [Rock], [Scissors], [Paper] 중에 하나를 입력하세요: ')
            player = player.lower()
            monster = random.randint(1,3)
            if monster == 1:
                monster = 'rock'
            elif monster == 2:
                monster = 'scissors'
            else:
                monster = 'paper'
                
            if player == 'rock':
                if monster == 'rock':
                    result = 'Draw'
                if monster == 'scissors':
                    user.result += 1
                    return user.result
                    
                if monster == 'paper':
                    target.result += 1
                    return target.result
                    
            elif player == 'scissors':
                if monster == 'rock':
                    target.result += 1
                    return target.result

                if monster == 'scissors':
                    result = 'Draw'
                    
                if monster == 'paper':
                    user.result += 1
                    return user.result
                
            else:
                if monster == 'rock':
                    user.result += 1
                    return user.result
                if monster == 'scissors':
                    target.result += 1
                    return target.result
                if monster == 'paper':
                    result = 'Draw'

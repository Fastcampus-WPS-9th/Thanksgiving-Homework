import random


class Sword:
    def __init__(self, name):
        self.name = name
        self.strength = 0
        self.atk = 100
        self.score = ''
    
    def __repr__(self):
        return f' {self.strength}, {self.atk}'
    
    def upgrade(self):
        success = ['성공', '실패']
        result = random.choice(success)
        print(result)
        while self.strength < 10:
            if result == '성공':
                print(f'{result} 했습니다.')
                self.strength += 1
                self.atk += 100
                print(f'현재 {self.strength}강이며, 현재 공격력은 {self.atk}입니다.')
                break
            else:
                print(f'{result} 했습니다.')
                print(f'현재 {self.strength}강이며, 현재 공격력은 {self.atk}입니다.')
                break
        

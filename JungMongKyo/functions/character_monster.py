import random

class User:
    def __init__(self, name, type_of):
        self.name = name
        self.type_of = type_of
        self.hp = 100
        self.mp = 80
        self.attack = 20
        self.result = 0
        self.point = 0
        
    def user_info(self):
        print(f'유저명: {self.name}',
              f'유저 속성: {self.type_of}',
              f'hp: {self.hp}, mp: {self.mp}\n'
             )

    def user_skill(self, target):
        
        self.mp = self.mp - 10
        if self.type_of == target.type_of:
            target.hp = target.hp - self.attack * 1/2
        else:
            target.hp = target.hp - self.attack * 2
    
    def user_hit(self, target):
        target.hp = target.hp - self.attack

        
        
class Monster:
    def __init__(self):
        self.type_of = random.randint(1,2)
        if self.type_of == 1:
            self.type_of = 'fire'
            self.name = 'fire_monster'
        else:
            self.type_of = 'ice'
            self.name = 'ice_monster'

        self.hp = 100
        self.mp = 80
        self.attack = 20
        self.result = 0       
        
    def mon_info(self):
        print(f'monster type: {self.type_of}',
              f'monster hp: {self.hp}\n'
             )
    def mon_skill(self, target):
        self.mp = self.mp - 20
        if self.type_of == target.type_of:
            target.hp = target.hp - self.attack * 1/2
        else:
            target.hp = target.hp - self.attack * 2
    def mon_hit(self, target):
        target.hp = target.hp - self.attack

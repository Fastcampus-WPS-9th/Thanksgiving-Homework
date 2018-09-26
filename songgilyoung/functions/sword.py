import random

class Sword:
    price_list = [300, 300, 500, 500, 1000, 1500, 2000, 2000, 3000, 5000, 10900, 20000, 35000, 55000, 100000, 180000, 300000, 500000, 600000, 1500000]
    sel_list = [0, 150, 400, 600, 800, 1600, 3500, 6100, 10000, 20000, 35100, 160000, 350000, 1000000, 3000000, 7500000, 14200000, 20000000, 30000000, 68300000]
    per_list = [100, 98, 95, 95, 95, 90, 90, 90, 85, 80, 80, 75, 70, 65, 60, 60, 55, 50, 50, 45]
    
    def __init__(self):
        self.now_enchant = 0
        self.insert_enchant_value()
        
    def update_user_enchant(self, user):
        if user.max_enchant < self.now_enchant:
            user.max_enchant = self.now_enchant
            
        if user.max_money < user.money:
            user.max_money = user.money
        
    def sel_weapon(self, user):
        user.money += self.now_sel
        print('\t\tSELLLLL!! {} WON PLUS!!!'.format(self.now_sel))
        self.update_user_enchant(user)
        return False
    
    def upgrade_weapon(self, user):
        # 유저의 돈 체크
        if user.money < self.now_price:
            print('\t\tNO MONEY')
            return True
        
        # 유저돈 삭감
        user.money -= self.now_price
        
        # 강화 성공실패 확인
        rand_per = random.randrange(0, 100)
        if self.now_per < rand_per:
            print('\t\tBROKENNNNNNN :(((')
            return False
        
        # 강화 성공시
        self.update_user_enchant(user)
        self.now_enchant += 1
        self.insert_enchant_value()
        return True
        
    def insert_enchant_value(self):
        self.now_price = self.price_list[self.now_enchant]
        self.now_per = self.per_list[self.now_enchant]
        self.now_sel = self.sel_list[self.now_enchant]

import random


class lottery():
    
    def __init__(self):
        pass
    
    
    def box10(self, hogu):
        rd = random.random()
        hogu.timeleft -= 1
        if rd <= 0.4 :
            hogu.money += 10
            print('당첨! 당첨금을 10원만큼 획득 하셨습니다.')
        elif rd <= 0.9:
            hogu.money -= 10
            print('꽝! 다시시도하세요.')
        else:
            hogu.money += 20
            print('대박! 운이 좋으시군요 30원을 획득하셨어요!')
    def box50(self, hogu):
        rd = random.random()
        hogu.timeleft -= 1
        if rd <= 0.4 :
            hogu.money += 120
            print('당첨! 당첨금을 120원 만큼 획득 하셨습니다..')
        elif rd <= 0.95:
            hogu.money -= 50
            print('꽝! 다시시도하세요.')
        else:
            hogu.money += 240
            print('대박! 운이 좋으시군요 당첨금이 두배! 240원을 획득하셨습니다.')
            
    def box100(self, hogu):
        rd = random.random()
        hogu.timeleft -= 1
        if rd <= 0.1 :
            hogu.money += 300
            print('당첨! 무려 300원을 획득하셨습니다.')
        elif rd <= 0.95:
            hogu.money -= 100
            print('꽝! 다시시도하세요.')
        else:
            hogu.money += 600
            print('초대박! 1등은 당신것! 무려 600원을 획득하셨습니다.')
            
class hogu():
    
    def __init__(self,name):
        self.name = name
        self.money = 100
        self.timeleft = 9
        
        
    def set_money (self,money):
        self.money = money

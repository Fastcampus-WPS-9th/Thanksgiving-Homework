from functions.enchant import do_enchant
from models.shop import Shop
from models.user import User
from models.sword import Sword

def system_on():
    print('>>>>>SYSTEM ON<<<<<')
    name = input('\n유저 이름을 생성해 주세요\n입력 :')
    user1 = User(name)
    shop1 = Shop()
    while True:
        choice = input(
            '1. 검 구매'
            ' 2. 검 강화하기'
            ' 3. 랭크 보기'
            ' 0. 게임 종료'
            '\n선택 : ')
        
        if choice == '1':
            print(shop1.show_item_list)
            selected = input('\n구매할 아이템 선택 : ')
            sword1 = shop1.sell_item(selected)
            print(sword1.name)
            user1.buy_sword(sword1)
            print(user1.show_sword_list)
            
        elif choice == '2':
            do_enchant(user1)
            
        elif choice == '3':
#             with open('rank.txt', 'rt') as f:
            pass
        
        elif choice == '0':
            print('검 강화하기 게임을 종료하겠습니다')
            break
         
        else:
            print('없는 선택지 입니다. 다시 선택해주세요.')

if __name__ == '__main__':
    system_on()

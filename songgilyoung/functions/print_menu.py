# 출력을 위한 print decorator
def printOverlap(fprint):
    def wrapper(*args, **kwargs):
        print("")
        print("==-==-==-==-==-"*5)
        print("")
        fprint(*args, **kwargs)
    return wrapper

fprint = printOverlap(print)

# 메뉴 출력
def print_menu(sword, user):
    logo_str = '\t\tEnchant Sword'
    money_str = '\t\t{}님의 현재 가진 돈: {}'.format(user.name, user.money)
    menu_str = '\t\t1. 강화하기\n\t\t2. 판매하기\n\t\t3. 겜끝\n\n\t\t현재 판매비용: {}'.format(sword.now_sel)
    sword_str = '\t\t현재 강화 수치: {}\n\t\t강화비용: {}\n\t\t성공률: {}%'.format(sword.now_enchant, sword.now_price, sword.now_per)
    
    fprint(logo_str)
    fprint(money_str)
    fprint(menu_str)
    fprint(sword_str)

#메뉴 선택
def sel_menu(sword, user):
    menu_item = {1: sword.upgrade_weapon, 2: sword.sel_weapon}
    choice = int(input("> "))
    if choice == 3:
        return 2
    return menu_item[choice](user)

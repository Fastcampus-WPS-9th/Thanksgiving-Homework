from functions.User import *
from functions.game_page import*

def mainpage():
    
    while True:
        
        print('=============\n원하는 진행의 숫자를 눌러주세요!! \n1.게임하기\n2.순위보기\n3.종료하기\n===================\n')
        choose=input()
        
        if int(choose)==1:
            game_page()
            continue
    #     if int(choose)==2:
    #         rank_page()

        if int(choose)==3:

            print('추석연휴 수고하셨습니다. :D')
            break

if __name__ == "__main__":
    mainpage()

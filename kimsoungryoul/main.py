# This is OneCard Game
from KimSoungRyoul.models.card import Deck
from KimSoungRyoul.models.player import Player

if __name__ == '__main__':
    Deck()

    player1 = Player(username='ksr', score_num=0)
    player2 = Player(username='jkk', score_num=0)

    print(Deck.check_card_num())

    for i in range(0, 5):
        player1.get_card()
        player2.get_card()

    print('최초 카드패 --------------------')
    player1.show_card_list()
    player2.show_card_list()
    print('----------------------------')

    print(Deck.check_card_num())

    who_s_turn = True
    draped_card = Deck.draw_card()

    turn_num = 0
    while True:
        turn_num += 1
        print('-------------', turn_num, ' 번째 턴!!!!--------------------')
        print('\n바닥에 놓인 카드 : ', draped_card, '\n')
        if who_s_turn:
            print('------player1:--')
            draped_card = player1.raise_card(draped_card=draped_card)
            who_s_turn = False
            # print('player1의 카드패 : ')
            player1.show_card_list()
            print('---------------------------')
        else:
            print('-------player2:--')
            draped_card = player2.raise_card(draped_card=draped_card)
            who_s_turn = True
            # print('player2의 카드패 : ')
            player2.show_card_list()
            print('-------------------')
        print('-----------turn end----------------------------------------\n\n')

        if player1.show_card_list() is 0:
            print(player1.username, ' is Win!!!!')
            break
        elif player2.show_card_list() is 0:
            print(player2.username, ' is Win!!!!')
            break

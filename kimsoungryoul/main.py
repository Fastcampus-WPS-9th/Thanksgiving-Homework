# This is OneCard Game
from KimSoungRyoul.models.card import Deck
from KimSoungRyoul.models.player import Player

if __name__ == '__main__':
    Deck()

    player1 = Player(username='ksr', score_num=10)

    player1.get_card()
    player1.show_card_list()

    print(Deck.check_card_num())
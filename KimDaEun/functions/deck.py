from .card import Card
from itertools import product
from random import shuffle


class Deck:

    suits = ['heart', 'club', 'diamond', 'spade']
    ranks = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    cards = []
    pile = []

    # 52장의 카드 생성
    @classmethod
    def create_cards(cls):
        combinations = list(product(cls.suits, cls.ranks))
        for card in combinations:
            cls.cards.append(Card(card[Card.SUIT], card[Card.RANK]))

    # 카드 섞기
    @classmethod
    def shuffle_cards(cls):
        for i in range(10):
            shuffle(cls.cards)

    # 카드 1장 가져오기
    @classmethod
    def pop_cards(cls):
        return cls.cards.pop(0)

    # 게임 시작 전 선수들에게 카드 4장씩 배분
    @classmethod
    def distribute(cls, player1, player2):
        player1.receive(cls.cards[0:7:2])
        player2.receive(cls.cards[1:8:2])
        cls.cards = cls.cards[8:]

    # 카드더미에 카드쌓기
    @classmethod
    def set_top_of_pile(cls, card):
        cls.pile.append(card)

    # 카드더미의 가장 위에 있는 카드 가져오기
    @classmethod
    def get_top_of_pile(cls):
        return cls.pile[len(cls.pile)-1]

    # 게임 셋팅하기
    @classmethod
    def initiate(cls, player1, player2):
        cls.create_cards()
        cls.shuffle_cards()
        cls.distribute(player1, player2)
        cls.set_top_of_pile(cls.cards.pop(0))

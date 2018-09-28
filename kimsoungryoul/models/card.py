import enum
import random


@enum.unique
class Shape(enum.Enum):
    SPADE = 100
    DIAMOND = 101
    CLUB = 103
    HEART = 104


class NamedNum(enum.Enum):
    Jack = 11
    Queen = 12
    King = 13
    Ace = 1


class Card:

    def __init__(self, shape, card_num):
        self.card_num = card_num
        self.shape = shape

    def is_greater_than(self, card):
        if card.shape == self.shape:
            if card.card_num < self.card_num:
                return True
            else:
                return False
        elif card.shape < self.shape:
            return True
        else:
            return False

    def __repr__(self):
        return 'cardstate=[ ' + self.shape.name + ', ' + str(self.card_num) + ' ]'


class GeneralCard(Card):

    def special_ability(self):
        pass


class JackCard(GeneralCard):

    def special_ability(self):
        return 'jump'


class QueenCard(GeneralCard):
    pass


class KingCard(GeneralCard):
    pass


class Deck:
    card_list = []

    def __init__(self):
        for sh in [Shape.CLUB, Shape.DIAMOND, Shape.HEART, Shape.SPADE]:
            for num in range(1, 14):
                if num is 10:
                    Deck.card_list.append(Card(shape=sh, card_num=NamedNum.Jack))
                elif num is 11:
                    Deck.card_list.append(Card(shape=sh, card_num=NamedNum.Queen))
                elif num is 12:
                    Deck.card_list.append(Card(shape=sh, card_num=NamedNum.King))
                else:
                    Deck.card_list.append(Card(shape=sh, card_num=str(num)))

        print('총 카드 숫자 :', len(Deck.card_list))

    @classmethod
    def draw_card(cls):
        random_num = random.randrange(1, 52)

        return cls.card_list.pop(random_num)

    @classmethod
    def check_card_num(cls):
        return len(cls.card_list)

from .player import Player
from .deck import Deck
from .card import Card
from random import choice


class Computer(Player):

    def __init__(self, name='computer'):
        super().__init__(name)

    def show(self):
        print(f'{self.name}님이 가지고 있는 카드는 ({len(self.cards)}개)입니다.')

    def draw(self):
        drawable_cards = super().get_drawable()
        chosen_card = choice(drawable_cards)
        Deck.set_top_of_pile(chosen_card)
        self.cards.remove(chosen_card)
        chosen_card.drawer = self
        print(f'{self.name}님이 {Card.SHAPE[chosen_card.suit]}{chosen_card.rank}를 냈습니다.')
        return chosen_card

    def change_suit(self):
        chosen_suit = choice(Deck.suits)
        if chosen_suit != Deck.get_top_of_pile().suit:
            Deck.get_top_of_pile().suit = chosen_suit
            print(f'{self.name}님이 {chosen_suit}로 카드모양을 바꿨습니다.')
        else:
            print(f'{self.name}님이 카드 모양을 유지했습니다.')

    def add(self):
        print(f'{self.name}님이 1장을 가져갔습니다.')
        return super().add()

    def play(self):
        if len(self.get_drawable()) > 0:
            self.draw()
        else:
            self.add()

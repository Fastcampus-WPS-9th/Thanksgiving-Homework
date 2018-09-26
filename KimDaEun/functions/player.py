from .deck import Deck


class Player:

    cards_set = []

    def __init__(self, name, score=10000, cards=None):
        self.name = name
        self.score = score
        self.cards = cards

    # 카드 4장 받기
    def receive(self, cards):
        self.cards = cards

    # 가지고 있는 카드 보여주기
    def show(self):
        pass

    # 카드 내기
    def draw(self):
        pass

    # 카드 모양 바꾸기
    def change_suit(self):
        pass

    # 카드 1장 받기
    def add(self):
        new_card = Deck.pop_cards()
        self.cards.append(new_card)
        return new_card

    # 자기 차례에서 카드를 내거나 1장 받기
    def play(self):
        pass

    # 낼 수 있는 카드 가져오기
    def get_drawable(self):
        top_of_pile = Deck.get_top_of_pile()
        drawable_cards = []
        for card in self.cards:
            if card.suit == top_of_pile.suit or card.rank == top_of_pile.rank:
                drawable_cards.append(card)
            else:
                pass
        return drawable_cards

    # 상태 보여주기
    def get_status(self):
        cards_len = len(self.cards)
        if cards_len == 1:
            print(f'**** {self.name}님이 원카드를 소유했습니다. ****')
        elif cards_len == 0:
            print(f'**** {self.name}님의 카드가 더 이상 없습니다. ****')
            return self
        else:
            pass

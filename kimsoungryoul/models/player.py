from KimSoungRyoul.models.card import Deck


class Player:
    total_player_num = 0

    def __init__(self, username, score_num=0, cards=None):
        Player.total_player_num += 1
        self.username = username
        self.score_num = score_num
        self.score_view_cnt = 0
        if cards is None:
            self.cards = []
        else:
            self.cards = cards

    def get_card(self):
        self.cards.append(Deck.draw_card())

    # 카드는 내다
    def raise_card(self, draped_card):
        for i in range(0, len(self.cards)):
            if draped_card.card_num is self.cards[i].card_num or draped_card.shape is self.cards[i].shape:
                raised_card = self.cards[i]
                self.cards.pop(i)
                Deck.return_card(raised_card)
                print('카드를 제출합니다..', raised_card)
                return raised_card
        else:
            print('맞는 카드가 없어서 카드를 가져갑니다..')
            self.cards.append(Deck.draw_card())
            return draped_card

    def show_card_list(self):
        print(self.username, '의 카드패 : ', self.cards)
        return len(self.cards)

    # @username.setter
    # def username(self, value):
    #     if value in ['!', '@', '#', '$', '%']:
    #         raise ValueError('회원이름에 특수문자가 들어갈수 없습니다..')
    #     else:
    #         self._username = value

    # @property
    # def score_num(self):
    #     self.score_view_cnt += 1
    #     return self.score_num

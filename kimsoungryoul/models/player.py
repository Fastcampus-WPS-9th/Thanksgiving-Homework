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

    def raise_card(self, index):
        return self.cards.pop(index)

    def show_card_list(self):
        print(self.cards)
        return self.cards

    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, value):
        if value in ['!', '@', '#', '$', '%']:
            raise ValueError('회원이름에 특수문자가 들어갈수 없습니다..')
        else:
            self._username = value

    # @property
    # def score_num(self):
    #     self.score_view_cnt += 1
    #     return self.score_num

from .player import Player
from .deck import Deck
from .card import Card


class User(Player):

    def __init__(self, name):
        super().__init__(name)

    def show(self):
        message = ''
        for card in self.cards:
            message += f'{Card.SHAPE[card.suit]}{card.rank} '
        print(f'{self.name}님이 가지고 있는 카드는', message, f'({len(self.cards)}개)입니다.')

    def draw(self):
        drawable_cards = self.get_drawable()
        drawable_cards = [''.join([Card.SHAPE[card.suit], card.rank]) for card in drawable_cards]
        drawn_card = None

        try:
            while drawn_card is None:
                print(f'낼 카드를 입력하세요.(낼 수 있는 카드 : {" ".join(drawable_cards)})\n',
                      '---- 참고 ----\n',
                      '♠ : spade\n',
                      '♥ : heart\n',
                      '♣ : club\n',
                      '◆ : diamond\n',
                      '--- 입력예시 ---\n',
                      'spade 7\n',
                      'heart Q\n')

                suit, rank = input('입력 : ').split(' ')

                for card in self.cards:
                    if card.suit == suit and card.rank == rank:
                        drawn_card = card
                        Deck.set_top_of_pile(drawn_card)
                        self.cards.remove(drawn_card)
                        drawn_card.drawer = self
                        break
                    else:
                        pass
                else:
                    print('낼 수 없는 카드입니다. 다시 입력하세요.')

            print(f'{self.name}님이 {Card.SHAPE[drawn_card.suit]}{drawn_card.rank}를 냈습니다.')
            return drawn_card

        except ValueError:
            raise ValueError('잘못된 값에 인한 에러가 발생했습니다. 게임을 종료합니다.')

    def change_suit(self):
        print('바꿀 모양을 입력하세요.\n',
              '--- 입력 예시 ---\n',
              'spade\n'
              'diamond\n',
              'club\n',
              'heart\n',
              'keep (모양을 유지하려면)\n')

        suit_list = ['keep']
        suit_list.extend(Deck.suits)
        chosen_suit = ''

        while chosen_suit not in suit_list:
            print('spade, diamond, club, heart, keep 중 하나만 입력하세요.')
            chosen_suit = input('입력 : ')

        if chosen_suit == 'keep' or chosen_suit == Deck.get_top_of_pile().suit:
            print(f'{self.name}님이 카드 모양을 유지했습니다.')
        else:
            print(f'{self.name}님이 카드 모양을 {chosen_suit}로 변경했습니다.')
            Deck.get_top_of_pile().suit = chosen_suit

    def add(self):
        print('새로운 카드를 가져옵니다.')
        new_card = super().add()
        print(f'{Card.SHAPE[new_card.suit]}{new_card.rank}를 받았습니다.\n')

    def play(self):
        if len(self.get_drawable()) > 0:
            self.draw()
        else:
            answer = input('낼 수 있는 카드가 없습니다. 새로운 카드를 가져오시겠습니까?[y]')
            while answer != 'y':
                print('새로운 카드를 가져와야 합니다. y를 입력하세요.')
                answer = input('입력[y] : ')
            self.add()

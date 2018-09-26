class Card:

    SUIT = 0
    RANK = 1
    SHAPE = {
        'heart': '♥',
        'club': '♣',
        'diamond': '◆',
        'spade': '♠'
    }

    def __init__(self, suit, rank, drawer=None):
        self.suit = suit
        self.rank = rank
        self.drawer = drawer

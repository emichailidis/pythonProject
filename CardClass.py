
class Card:

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
        self._display = rank+suit
        self._value = self.set_value(rank)

    def set_value(self, r) :
        match r:
            case 'K':
                v=4
            case 'B':
                v=2
            case 'D':
                v=3
            case 'A':
                v=11
            case _:
                v=r
        return v





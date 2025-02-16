import random

class Card(object):
    """一张牌"""
    def __init__(self, suite, face):
        self._face = face
        self._suite = suite
    @property
    def face(self):
        return self._face
    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (face_str, self._suite)
    def __repr__(self):
        return self.__str__()

class Poker(object):
    # 一副牌
    def __init__(self):
        self._cards = [Card(suite, face) for face in range(1, 14) for suite in '♥♠♣♦']
        self._current = 0
    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        # 洗牌
        self._current = 0
        # random.shuffle(self._cards)
        random.shuffle(self._cards)
    @property
    def next(self):
        # 发牌
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        return self._current < len(self._cards)

class Player(object):
    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []
    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self,card):
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        self._cards_on_hand = sorted(self._cards_on_hand, key=card_key)

#排序规则-先根据花色再根据点数排序
def card_key(card):
    return (card.suite, card.face)

def main():
    p = Poker()
    p.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            player.get(p.next)
    for player in players:
        print(player.name + ':', end=' ')
        player.arrange(card_key)
        print(player.cards_on_hand)

if __name__ == '__main__':
    main()


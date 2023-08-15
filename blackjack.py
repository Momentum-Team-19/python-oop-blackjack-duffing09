import random

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


class Deck:
    def __init__(self, suits, ranks):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.cards.append(card)
        

# directions for building a card for us
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f'{self.suit}  {self.rank}'


new_deck = Deck(SUITS, RANKS)
for card in new_deck.cards:
    print(card)

# Write your blackjack game here.

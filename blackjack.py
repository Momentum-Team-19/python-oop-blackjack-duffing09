import random
import colorama
from colorama import Fore, Style, Back

SUITS = [f'{Fore.BLACK}{Style.BRIGHT}♠{Fore.WHITE}{Style.NORMAL}', f'{Fore.RED}{Style.BRIGHT}♥{Fore.WHITE}{Style.NORMAL}', f'{Fore.RED}{Style.BRIGHT}♦{Fore.WHITE}{Style.NORMAL}', f'{Fore.BLACK}{Style.BRIGHT}♣{Fore.WHITE}{Style.NORMAL}']
RANKS = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]


class Deck:
    def __init__(self, suits, ranks):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank, value=0)
                if card.rank in ["J", "Q", "K"]:
                    card.value = 10
                elif card.rank == "A":
                    card.value = 11
                else:
                    card.value = card.rank
                self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_card(self):
        card = self.cards.pop()
        return card


# directions for building a card for us
class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
    
    def __str__(self):
        return f'{self.suit}  {self.rank}'
    

class Player:
    def __init__(self):
        self.name = input("Please enter your name: ")
        self.hand = []
        self.score = 0
        self.balance = 100 #initial balance
    
    def place_bet(self):
        while True:
            try:
                bet = int(input(f"{self.name}, your current balance is {self.balance}. Place your bet: "))
                if 0 <= bet <= self.balance:
                    self.balance -= bet
                    return bet
                else: 
                    print("Invalid bet. Enter a valid amount.")
            except ValueError:
                print("Invalid input. Enter a valid number.")


class Dealer:
    def __init__(self):
        self.name = "Dealer Kate"
        self.hand = []
        self.score = 0


class Game:
    def __init__(self):
        self.deck = Deck(SUITS, RANKS)
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Dealer()

    def play_game(self):
        bet = self.player.place_bet()
        self.dealer.hand.append(self.deck.draw_card())
        while len(self.player.hand) < 2:
            self.player.hand.append(self.deck.draw_card())
        print(self.player.name)
        for card in self.player.hand:
            self.player.score += card.value
            print(card)
        print(self.player.score)

        while len(self.dealer.hand) < 2:
            self.dealer.hand.append(self.deck.draw_card())
        print(self.dealer.name)
        for card in self.dealer.hand:
            self.dealer.score += card.value
            print(card)
        print(self.dealer.score)
        if self.player.score == 21 or self.dealer.score == 21:
            if self.dealer.score < 21:
                print("Player got blackjack!")
                return
            elif self.player.score < 21:
                print("Dealer got blackjack!")
                return
            else:
                print("You pushed!")
                return
        if self.player.score < 21:
            self.player_hit()
        if self.player.score <= 21:
            self.dealer_hit()

    def player_hit(self):
        action = None
        while action != 's':
            action = input("[H]it or [S]tay? ").lower().strip()
            if action == "h":
                self.player.hand.append(self.deck.draw_card())
                self.player.score = sum(
                    card.value for card in self.player.hand)
                if "A" in [card.rank for card in self.player.hand] and self.player.score > 21:
                    self.player.score -= 10

                print("Player hand:", )
                for card in self.player.hand:
                    print(card)
                print("Your score:", self.player.score)
                if self.player.score > 21:
                    print("Bust!")
                    break
                elif self.player.score == 21:
                    print("You got blackjack!")
                    break
            elif action != 's':
                print("Invalid choice, enter 'h' or 's'")
        else:
            print("You chose to stay")

    def declare_winner(self):
        if self.player.score > 21:
            print('Dealer won the hand')
        elif self.dealer.score > 21:
            print('Player won')
        elif self.player.score <= 21 and self.dealer.score <= 21:
            if self.player.score == self.dealer.score:
                print("Push")
            elif self.player.score > self.dealer.score:
                print("Player wins")
                self.player.score += 2 * self.bet
            else:
                print
    
    def dealer_hit(self):
        print("Dealer's turn:")
        while self.dealer.score < 17:
            self.dealer.hand.append(self.deck.draw_card())
            self.dealer.score = sum(
                card.value for card in self.dealer.hand)
            print("Dealer hand:")
            for card in self.dealer.hand:
                print(card)
            print("Dealer score:", self.dealer.score)
            if self.dealer.score > 21:
                print("Dealer busts!!")
                break
            elif self.dealer.score == 21:
                print("dealer got blackjack!")
                break


new_game = Game()
new_game.play_game()

# while True:
#     def __init__(self):
#         if self.player.score > 21:
#             print('Dealer won the hand')
#         elif self.dealer.score > 21:
#             print('Player won')
#         elif self.player.score <= 21 and self.dealer.score <= 21:
#             if self.player.score == self.dealer.score:
#                 print("Push")
#             elif self.player.score > self.dealer.score:
#                 print("Player wins")
#                 self.player.score += 2 * self.bet
#             else:
#                 print
    # new_game.play_game()
    # if new_game.player.score > 21:
    #     print("Player busts!")
    # elif new_game.dealer.score > 21:
    #     print("Dealer busts!")
    #     new_game.player.score += 2 * new_game.bet
    # elif new_game.player.score > new_game.dealer.score:
    #     print("Player wins!")
    #     new_game.player.balance += 2 * new_game.bet
    # elif new_game.dealer.score > new_game.player.score:
    #     print("Dealer wins!")
    # else:
    #     print("Push!")
    
    # print(f"Player's balance: {new_game.player.balance}")
    # play_again = input("Play again? (y/n) ").lower()
    # if play_again != "y":
    #     break





# Write your blackjack game here.

import random


class Deck:

    self.cards = []
    self.NumberOfCards = 52
    self.NumberOfSuits = 4
    self.NumberOfCardsPerSuit = 12
    self.CardsPerSuit = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(2, 11):
                self.cards.append(Card(j))
            for j in ['J', 'Q', 'K', 'A']:
                self.cards.append(Card(j))

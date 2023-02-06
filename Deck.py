import random
import Cards


class Deck:

    # setup member variables
    def __init__(self):
        # initialize member variables
        self.single_suite = Cards.Cards()

        # creating a deck of 52 cards
        self.cards = list(self.single_suite.all_cards) * 4

        # shuffles the deck
        self.shuffle()

    # shuffles the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # remove give card from the deck
    def remove_card(self, card):
        self.cards.remove(card)

    # get the top card from the deck
    def get_top_card(self):
        return self.cards.pop()

    # reset deck
    def reset_deck(self):
        # creating a deck of 52 cards
        self.cards = list(self.single_suite.all_cards) * 4

        # shuffles the deck
        self.shuffle()

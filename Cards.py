import json


class Cards:

    # setup member variables
    def __init__(self):
        # initialize member variables
        self.CARDS_IN_A_SUIT = 12
        self.all_cards = set()
        self.card_values = {}

        # create points map for all cards
        self.set_card_values()

        # create set of all cards
        self.all_cards = set(self.card_values.keys())

    # creates a points map from the json file
    def set_card_values(self):
        # load cards and their values from json file
        try:
            f = open('card_values.json')
            self.card_values = json.load(f)[0]
            f.close()
        except:
            print("Cards.py -> Error: Loading card_values.json")

    # returns the point value of a card
    def get_card_values(self, card):
        try:
            return self.card_values[card]
        except:
            return "Cards.py -> Error: Card not found"

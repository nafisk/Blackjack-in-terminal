import json


class Cards:

    # setup member variables
    def __init__(self):
        self.CARDS_IN_A_SUIT = 12
        self.all_cards = set()
        self.card_values = {}

        # set values for all cards
        self.set_card_values(self.card_values)

    # creates a map of all cards and its values
    def set_card_values(self, card_values):
        f = open('card_values.json')
        values = json.load(f)
        print(values)
        # for key in values:
        # card_values[key] = values[key]
        f.close()
    #   return card_values


# call Cards class
cards = Cards()
print(cards.card_values)

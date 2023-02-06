import Cards
import itertools


class Player:

    # setup member variables
    def __init__(self, name, max_score):
        self.NAME = name
        self.MAX_SCORE = max_score
        self.hand = []
        self.card_suite = Cards.Cards()

    # add card to player's hand
    def add_card(self, card):
        self.hand.append(card)

    # get player's hand
    def get_hand(self):
        return self.hand

    # get player's name
    def get_name(self):
        return self.NAME

    # get player's total score
    def get_score(self):
        score = 0
        number_of_aces = 0

        # get score of hand
        for card in self.hand:
            if card == 'A':
                number_of_aces += 1
            else:
                score += int(self.card_suite.get_card_values(card))

        # handle multiple aces in hand
        if number_of_aces > 0:
            score = self.handle_aces(score, number_of_aces)

        return score

    # handle multiple aces in hand with given score
    def handle_aces(self, score, number_of_aces):

        # score + optimal ace value
        optimal_score = score

        # get all possible ace values
        ace_points = self.card_suite.get_card_values("A").split('|')

        # combination of ace values as a list // [[1, 11], [1, 11], ...]
        ace_list = number_of_aces * [list(map(int, ace_points))]

        # get all possible combinations of ace values and set hightest score <= 21
        for combination in itertools.product(*ace_list):
            if sum(combination) + score <= self.MAX_SCORE:
                optimal_score = sum(combination) + score

        return optimal_score

    # player score print with cards
    def hand_with_score(self):
        _ = ' '.join(self.hand)
        return f'{self.NAME} has: {_} = {str(self.get_score())}'

    # for dealer score print with hidden cards
    def hand_with_hidden_score(self):
        _ = self.hand[1:]
        # print('Player.py:', self.hand, '->', _)  # debug
        unknowns = '  ? '*len(_) if len(_) > 0 else ''
        return f'{self.NAME} has: {self.hand[0] + unknowns} = ?'

    # reset player's hand
    def reset_hand(self):
        self.hand = []


# 4 7 A = 12
# player = Player('Player', 21)
# player.add_card('4')
# player.add_card('7')
# player.add_card('A')
# print(player.hand_with_score())

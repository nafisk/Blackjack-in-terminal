import os
from time import sleep
from subprocess import call


class Game:

    MAX_HIT_SCORE = 21
    DEALER_STAND_SCORE = 17

    def init(self):
        pass

    def play_blackjack(self):
        pass

    def play_again(self):
        pass

    def clear_screen(self):
        # clear screen for specific operating system
        _ = call('clear' if os.name == 'posix' else 'clear')

    def print_welcome(self):
        print('Welcome to Blackjack!')
        sleep(1)
        print('Dealing cards...')
        sleep(1)

    def get_player_name(self):
        return input('What is your name? ')

    def print_player_hand(self, player):
        print(f'{player.name}\'s hand: {player.hand} ({player.get_score()})')


game = Game()
print('hello geeks\n'*10)

game.clear_screen()

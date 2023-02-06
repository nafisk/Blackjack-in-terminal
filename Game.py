from time import sleep
import os
from subprocess import call
import Player
import Deck
import sys


class Game:

    def __init__(self):
        # assign member variables
        self.MAX_HIT_SCORE = 21
        self.DEALER_STAND_SCORE = 17

        # get and set game info
        self.clear_screen()
        self.deck = Deck.Deck()
        player_name = self.print_welcome_and_get_name()
        self.player = Player.Player(player_name, self.MAX_HIT_SCORE)
        self.dealer = Player.Player('Dealer', self.MAX_HIT_SCORE)

        # start game
        self.play_blackjack()

    def play_blackjack(self):
        self.clear_screen()

        # game loop
        end_game = False
        while end_game == False:
            # clear screen
            self.clear_screen()

            print(f'Hi {self.player.get_name()}! Welcome To Blackjack!')
            print()

            # set player and dealer hands
            self.set_initial_hand()

            # player turn loop
            while True and end_game is False:

                # print turn and points
                self.print_turn('Your')
                self.player_turn_print()

                # get player input
                player_input = input('Would you like to (H)it or (S)tand? ')
                print()
                sleep(1)

                # evaluate hit input, add card to hand, and check for bust
                if player_input == 'H' or player_input == 'h':
                    self.player.add_card(self.deck.get_top_card())

                    # if card is exactly MAX_HIT_SCORE
                    if self.player.get_score() == self.MAX_HIT_SCORE:
                        # announce player win and exit to replay
                        self.player_turn_print()
                        print('Blackjack! You Win!')
                        end_game = True
                        break
                    # if card is greater than MAX_HIT_SCORE (bust)
                    elif self.player.get_score() > self.MAX_HIT_SCORE:
                        # announce dealer win and exit to replay
                        self.dealer_turn_print()
                        print('You busted! Dealer Wins!')
                        end_game = True
                        break
                    # if card is less than MAX_HIT_SCORE
                    else:
                        # print and continue game
                        self.player_turn_print()

                # evaluate stand input, exit to dealer turn
                if player_input == 'S' or player_input == 's':
                    break

                # shuffle deck after each turn
                self.shuffle_deck()
                print('\n')

            print()

            # dealer turn loop
            while True and end_game is False:

                # print turn and points
                self.print_turn('Dealer\'s')
                self.load_animation('_', 20, False)
                print()
                self.dealer_turn_print()
                sleep(1)
                # if dealer score is less than dealer stand score
                if self.dealer.get_score() < self.DEALER_STAND_SCORE:
                    # card card to dealers hand
                    self.dealer.add_card(self.deck.get_top_card())
                    sleep(1)
                else:
                    # compare dealer and player scores
                    if self.dealer.get_score() > self.player.get_score() and self.dealer.get_score() <= self.MAX_HIT_SCORE:
                        self.clear_screen()
                        print('Dealer Wins!')
                        self.dealer_turn_print()
                        end_game = True
                        break
                    elif self.player.get_score() == self.dealer.get_score():
                        self.clear_screen()
                        print('It\'s a tie!')
                        self.dealer_turn_print()
                        end_game = True
                        break
                    else:
                        self.clear_screen()
                        print('You Win! Dealer Busted!')
                        self.dealer_turn_print()
                        end_game = True
                        break

                self.shuffle_deck()
                print('\n'*2)

            # replay game
            end_game = self.play_again()
            self.reset_hand_and_deck() if end_game is False else None

        print('Thanks for playing!')

    def print_turn(self, player):
        print(f'\n{player} turn...')

    def set_initial_hand(self):
        self.shuffle_deck()
        self.deal_cards()
        self.player.add_card(self.deck.get_top_card())
        self.dealer.add_card(self.deck.get_top_card())
        self.player.add_card(self.deck.get_top_card())
        self.dealer.add_card(self.deck.get_top_card())
        self.clear_screen()
        print('Starting hands dealt...')
        print()

    def shuffle_deck(self):
        self.deck.shuffle()
        self.load_animation('Shuffling deck...', 20, False)
        sleep(1)

    def deal_cards(self):
        self.load_animation('Dealing cards...', 20, False)
        sleep(1)

    def player_turn_print(self):
        print(self.bordered(self.dealer.hand_with_hidden_score() +
              '\n' + self.player.hand_with_score()) + '\n')

    def dealer_turn_print(self):
        sleep(1)
        print(self.bordered(self.dealer.hand_with_score() +
              '\n' + self.player.hand_with_score()) + '\n')

    def bordered(self, text):
        lines = text.splitlines()
        width = max(len(s) for s in lines)
        res = ['┌' + '─' * width + '┐']
        for s in lines:
            res.append('│' + (s + ' ' * width)[:width] + '│')
        res.append('└' + '─' * width + '┘')
        return '\n'.join(res)

    def play_again(self):
        print()
        _ = input('Would you like to play again? Yes(Y) or No(N) ')
        if _ == 'Y' or _ == 'y':
            return False
        return True

    def clear_screen(self):
        # clear screen for specific operating system
        sleep(1)
        _ = call('clear' if os.name == 'posix' else 'clear')

    def print_welcome_and_get_name(self):
        self.load_animation('~Welcome to Blackjack!~', 20)
        sleep(1)
        return input('Please enter your name: ')

    def reset_hand_and_deck(self):
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.deck.reset_deck()

    def load_animation(self, msg, relative_time, clear_screen=True):

        # String to be displayed when the application is loading
        load_str = msg
        ls_len = len(load_str)

        # String for creating the rotating line
        animation = "|/-\\"
        anicount = 0

        # used to keep the track of the duration of animation
        counttime = relative_time

        # pointer for travelling the loading string
        i = 0
        while (counttime != 0):

            # used to change the animation speed
            # smaller the value, faster will be the animation
            sleep(0.075)

            # converting the string to list
            # as string is immutable
            load_str_list = list(load_str)

            # x->obtaining the ASCII code
            x = ord(load_str_list[i])

            # y->for storing altered ASCII code
            y = 0

            # if the character is "." or " ", keep it unaltered
            # switch uppercase to lowercase and vice-versa
            if x != 32 and x != 46:
                if x > 90:
                    y = x-32
                else:
                    y = x + 32
                load_str_list[i] = chr(y)

            # for storing the resultant string
            res = ''
            for j in range(ls_len):
                res = res + load_str_list[j]

            # displaying the resultant string
            sys.stdout.write("\r"+res + animation[anicount])
            sys.stdout.flush()

            # Assigning loading string
            # to the resultant string
            load_str = res

            anicount = (anicount + 1) % 4
            i = (i + 1) % ls_len
            counttime -= 1

        # for windows OS
        if clear_screen == True:
            if os.name == "nt":
                os.system("cls")

            # for linux / Mac OS
            else:
                os.system("clear")


game = Game()

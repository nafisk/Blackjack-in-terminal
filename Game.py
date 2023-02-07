from time import sleep
from subprocess import call
import Player
import shutil
import Deck
import sys
import os


class Game:

    # constructor
    def __init__(self):

        # assign member variables
        self.MAX_HIT_SCORE = 21
        self.DEALER_STAND_SCORE = 17

        # get and set game info
        self.clear_screen()
        self.deck = Deck.Deck()
        self.player = Player.Player(
            self.print_welcome_and_get_name(), self.MAX_HIT_SCORE)
        self.dealer = Player.Player('Dealer', self.MAX_HIT_SCORE)

        # start game
        self.play_blackjack()

    # handles entire game loop
    def play_blackjack(self):

        # clears screen before starting game
        self.clear_screen()

        # handles gameplay replay
        end_game = False

        # main game loop
        while end_game == False:

            # clear screen and print welcome message
            self.clear_screen()
            self.print_centre(
                f'Hi {self.player.get_name()}! Welcome To Blackjack!')
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
                if player_input == 'H' or player_input == 'h' or player_input == 'Hit' or player_input == 'hit':

                    # add card from deck to player hand
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
                        # announce dealer loss and exit to replay
                        self.dealer_turn_print()
                        print('You busted! Dealer Wins!')
                        end_game = True
                        break
                    # if card is less than MAX_HIT_SCORE
                    else:
                        # continue game
                        self.player_turn_print()

                # evaluate stand input, exit to dealer turn
                elif player_input == 'S' or player_input == 's':
                    break

                # wrong input
                else:
                    print('Invalid input, please try again.')

                # shuffle deck after each turn
                self.shuffle_deck()
                print('\n')

            print()

            # dealer turn loop
            while True and end_game is False:

                # print turn and points
                self.print_turn('Dealer\'s')

                # dealer turn animation and score board
                self.load_animation('_', 20, False)
                print()
                self.dealer_turn_print()
                sleep(1)

                # if dealer score is less than dealer stand score
                if self.dealer.get_score() < self.DEALER_STAND_SCORE:
                    # add card to dealers hand
                    self.dealer.add_card(self.deck.get_top_card())
                    sleep(1)

                # if dealer score is greater than dealer stand score
                else:

                    # compare dealer and player scores
                    if self.dealer.get_score() > self.player.get_score() and self.dealer.get_score() <= self.MAX_HIT_SCORE:
                        # dealer wins
                        self.clear_screen()
                        print('Dealer Wins!')
                        self.dealer_turn_print()
                        end_game = True
                        break

                    elif self.player.get_score() == self.dealer.get_score():
                        # player and dealer tie
                        self.clear_screen()
                        print('It\'s a tie!')
                        self.dealer_turn_print()
                        end_game = True
                        break
                    else:

                        # dealers score is lower than player score
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

        self.print_centre('Thanks for playing!')

    # prints the turn of the current player
    def print_turn(self, player):
        print(f'\n{player} turn...')

    # adds two cards to each player and dealer
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

    # shuffles and randomizes deck
    def shuffle_deck(self):
        self.deck.shuffle()
        self.load_animation('Shuffling deck...', 20, False)
        sleep(1)

    # dealing cards animation
    def deal_cards(self):
        self.load_animation('Dealing cards...', 20, False)
        sleep(1)

    # score print with dealer cards hidden
    def player_turn_print(self):
        print(self.bordered(self.dealer.hand_with_hidden_score() +
              '\n' + self.player.hand_with_score()) + '\n')

    # score print with dealer cards visible
    def dealer_turn_print(self):
        sleep(1)
        print(self.bordered(self.dealer.hand_with_score() +
              '\n' + self.player.hand_with_score()) + '\n')

    # prints text with border around it
    def bordered(self, text):
        lines = text.splitlines()
        width = max(len(s) for s in lines)
        res = ['┌' + '─' * width + '┐']
        for s in lines:
            res.append('│' + (s + ' ' * width)[:width] + '│')
        res.append('└' + '─' * width + '┘')
        return '\n'.join(res)

    # returns true if player wants to play again
    def play_again(self):
        print()
        _ = input('Would you like to play again? Yes(Y) or No(N) ')
        if _ == 'Y' or _ == 'y':
            return False
        return True

    # clears the entire console
    def clear_screen(self):
        # clear screen for specific operating system
        sleep(1)
        _ = call('clear' if os.name == 'posix' else 'clear')

    # prints welcome message and gets player name
    def print_welcome_and_get_name(self):
        # self.load_animation('~Welcome to Blackjack!~', 40)
        self.print_centre('~Welcome to Blackjack!~')
        sleep(1)
        return input('Please enter your name: ')

    # prints centered text
    def print_centre(self, s, animation=False):
        print(s.center(shutil.get_terminal_size().columns))

    # resets the hand and deck
    def reset_hand_and_deck(self):
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.deck.reset_deck()

    # animation for loading
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

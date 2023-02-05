'''

- The only interaction point is whether the player should hit or stand
- Hand scores should be present when all card values are known
  (that is, everywhere except for the dealer when one of their cards is hidden).
  
- 52-card deck
    - Suite: [2 - 10, J, Q, K, A]
    - Deck: 4 x [2 - 10, J, Q, K, A]
        - Number cards: 2-10, worth the number on the card
        - face cards (King, Queen, Jack), each worth 10 points
        - aces, worth 1 or 11 points

- All 52 cards should be present in the deck at the start of the game
- The cards dealt should be randomized during play 
- the cards dealt should not be predictable.

- Definitions
    - Hand: a collection of cards that a player owns for the duration of the game.
    - Hit: add another card to a player's hand
    - Stand: add no more cards to a player's hand; stop playing a turn; proceed to the next phase of the game.
    - Bust: more than 21 points in a player's hand; the player's turn is instantly over; the player has lost.
  
- Winning
    - Player has to go as close to 21 points as possible without going over.
    - The dealer plays by a simple rule: hit until the hand's score is greater than or equal to 17 ("stand on 17").    

- Scoring
    - Add all the points in hand
    - Ace can be worth 1 or 11 points. Program should choose the best option. Has to be as close to 21 as possible. 
        - if score with 8+A+7, score can be 16 or 26. Then program should choose 16.

- Functions
    - deal_card: deals a card from the deck to a player
    - calculate_score: calculates the score of a hand
    - compare: compares the score of the player's hand to the dealer's hand
    - play_blackjack: starts the game
    - play_again: asks the player if they want to play again
    - clear: clears the console
    - logo: prints the logo
    - did_player_win: prints the result of the game
    - print_score: prints the score of the player and the dealer

- Classes
    - Deck: contains the deck of cards
    - Card: contains the value of a card
    - Player: contains the hand of a player
    - Dealer: contains the hand of the dealer
    - Game: contains the game logic and result

    


'''

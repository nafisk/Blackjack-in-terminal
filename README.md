# freenome

Install required dependencies:

  - Install a random library to shuffle the deck of cards at the start of each game.
  - Install a library for command-line interface.

Create a deck of cards:

  - Create a list of cards (2-10, J, Q, K, A) for each suit.
  - Shuffle the deck of cards using the random library.

Start the game:

  - Draw two cards for the player and two cards for the dealer. Show one card of the dealer face up.
  - Ask the player if they want to hit or stand. If they hit, draw another card. Repeat until they - stand or bust (score over 21).
  - If the player busts, the game is over.
  - If the player stands, the dealer plays. The dealer will hit until their score is greater than or - equal to 17.
  - Compare the scores of the player and the dealer. The one with the highest score (less than or - equal to 21) wins.

Optimize the scoring of Ace:

  - At the start of the game, assign Ace a value of 11. If the score goes over 21, change the value of - Ace to 1.
  - Repeat this process until the score is less than or equal to 21.

Create a README file:

  - Explain the steps to run the program, including the dependencies required.
  - Mention any assumptions/choices made.
  - Discuss design choices, algorithmic decisions, and tradeoffs.
  - Explain what can be improved given more time.
  - Provide manual tests and steps to run automated tests (if any).

Zip the code, README, and test files (if any) and send as a reply to the email.

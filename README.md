<h1 align="center">Blackjack</h1>

<p align="center">♣️♦️♥️♠️</p>
<p align="center">Blackjack is a simplified CLI version of the classic card game</p>

<br/><br/>
## 🚀 Getting Started

Only requirement for this project is ```python3```. To run the game, downlaod or clone the project, go to the project folder and then run the command
```
python3 Main.py
```


## 🕹️ How the game works
* 🙋‍♂️ Player's Turn
  - The game starts with each player receiving two cards, and the dealer receiving one card face up and one card face down
  - The players then have the option to "hit" and receive additional cards or "stand" and keep their current hand value
  - The player must keep hitting until their hand value is 21 or above, or they can choose to stand at any time
* 🤖 Dealer's Turn
  - Once all players have finished their turns, the dealer reveals their second card and hits or stands according to a set of predetermined rules
  - The dealer must hit until their hand value is 17 or above, and must stand on 17 or above.
* 💯 Score
  - If the player's hand value exceeds 21, they "bust" and lose the game
  - If the dealer busts, all remaining players win
  - If neither the player nor the dealer busts, the hand with the highest value closest to 21 wins
  - If both the dealer and player has the same score, it's a tie

<br/>

## 🤔 Assumptions and choices made
  * The code should be able to handle multiple players with little adjustment to the main game loop
  * Scores need to be recounted each time it is displayed to get the most optimized score due to 1 / 11 condition
  * Store card values in a .json file so that card values could be edited with relative ease in the future
  * Use suttle animations and sleep functions to make the game feel more natural 

<br/>

## 👩‍🏫 Design choices and algorithmic decisions
  * Utilizes Object-Oriented Programming concepts to abstract classes and build up game logic for a clean architecture
  * Implements code reuseability concepts by creating functions that reduce lines of code while simplifying logic
  * Score calculating algorithm adjusts for all bust scores if rules and values were to change
  * Score calculating algorithm takes care of score without Aces, with all Aces, a mixture of regular and Ace cards and always produces the most optical result

<br/>

## 👽 Future improvements
  * Refactor code to be able to handle multiple players
  * Be able to take inputs for bust score
  * Optimize dealer hits and stands so that it's as close to bust score as possible just like player
  * Center all text and clear screen each turn
  * Create actual card UI with text, both face up and face down

<br/>

## ✍️ Manual testing
  * Manual unit tests were performed for each class by creating objects at the end of the file
  * Test cases were written assess whether all functions performed as expected
  * Error checks are done to deal with any read/write errors, invalid input errors, etc
  * All classes and member functions passed all test casses

<br/>

## 🧠 Automated testing
  * No automatic testing was done in this case due to time constrants
  * Given more time pytest would be a great solution to automate testing for all functions

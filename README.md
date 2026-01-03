# **Blackjack**
A text based console version of blackjack that simulates a player vs a dealer in standard (hopefully normal) blackjack rules!

# **Quick explanation of blackjack**
- The goal of this game is to get as close to **21** as possible without going over
- Number cards are worth their face value (e.g 3 = 3)
- Face cards (Jack, Queen, King) are all worth **10**
- Aces can be worth **1** or **11** depending on what benefits the player most
- If your total goes over **21**, you bust and lose. Same goes for the dealer.
- You start with 2 cards, and are asked to hit or stand until you say stand or bust.
- If you hit, the dealer gives you another card. If you stand, your final score is your current cards total value.
- Dealer draws after player chooses to hit, and in most cases stops drawing until they reach 17 or higher. In my version this is the case.

# **Features**
- Simulates an entire game of blackjack against a dealer
- Players start with a balance to bet that they can choose to maintain over a number of rounds (until they run out of money 😔)
- Aces are adjusted to be 1 or 11 depending on if player may bust.
- Dealer hits until 17
- Input validation for entries
- Cards are randomly shuffled each round

# **How to run**
- Open terminal / command prompt
- Navigate to project folder
- e.g `cd blackjack`
- then run the game: `python blackjack.py`

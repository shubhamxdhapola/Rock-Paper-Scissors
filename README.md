### Rock, Paper, Scissors Game

The Rock, Paper, Scissors Game is a Python-based console application that allows users to play the classic game against a computer opponent.
The game involves multiple rounds, with each round determining a winner based on the player's and the computer's moves. At the end of the specified rounds, 
the game displays the final result, including the total number of rounds played, wins, losses, draws, and the overall winner.

#### Key Features:

1. **User Interaction and Input:**
   - The game starts by greeting the user and providing instructions on how to play.
   - The user is prompted to enter the number of rounds they want to play.
   - For each round, the user inputs their move by pressing 1 for Rock, 2 for Paper, or 3 for Scissors.

2. **Computer Move Generation:**
   - The computer randomly generates its move for each round using Python's `random.randint(1,3)` function.

3. **Round-by-Round Gameplay:**
   - The game compares the player's move with the computer's move to determine the round's outcome.
   - There are three possible outcomes for each round:
     - **Player Wins:** If the player's move beats the computer's move.
     - **Draw:** If both the player and the computer choose the same move.
     - **Computer Wins:** If the computer's move beats the player's move.
   - The result of each round is displayed along with both the player's and the computer's moves.

4. **Tracking Scores:**
   - The game keeps track of the number of rounds won by the player, the computer, and the number of draw rounds.
   - These scores are updated after each round.

5. **Final Result Calculation:**
   - After all the rounds are played, the game calculates and displays the final result.
   - It shows the total number of rounds played, the number of rounds won by the player, the computer, and the number of draws.
   - The overall winner is determined based on who won the most rounds.

6. **Error Handling:**
   - The game includes error handling to manage invalid inputs (e.g., entering non-integer values or values outside the range of 1 to 3).
   - It prompts the user to enter valid inputs when an error is detected.

### Summary:

This Rock, Paper, Scissors game project provides an interactive and engaging way for users to play the classic game against a computer. It features:
- Clear instructions and user prompts.
- Random move generation for the computer.
- Real-time tracking of scores and round outcomes.
- A final result summary after the specified rounds.
- Basic error handling to ensure smooth gameplay.

Overall, this project demonstrates basic programming concepts such as input handling, conditional statements, loops, functions, and error handling in Python. 
It offers a simple yet fun application that can be further enhanced with additional features such as graphical user interfaces, multiplayer options, or extended
gameplay rules.

# Assignment 3: Number Guessing Game

The computer picks a random number from 1 to 100 and you try to guess it.

- Hints: "Too high!" or "Too low!" after each wrong guess.
- Counts your attempts and shows the total when you win.
- Typing something that is not a whole number from 1 to 100 is rejected and does not count as an attempt.
- You can play again and the game tracks your best score.

## How to run in VS Code

1. Unzip the folder and open it in VS Code (File > Open Folder).
2. Open `guessing_game.py` and click the Run (play) button, or press `F5`.
   Or in the terminal: `python guessing_game.py` (`python3` on Mac/Linux).

Requires Python 3.6 or newer. No extra packages needed.

## Sample run

```
I'm thinking of a number between 1 and 100.
Enter your guess (1-100): 50
Too high!
Enter your guess (1-100): 25
Too low!
Enter your guess (1-100): 42

Correct! The number was 42.
You guessed it in 3 attempts.
```

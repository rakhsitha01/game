"""
Number Guessing Game
--------------------
- Generates a random number between 1 and 100.
- The user keeps guessing until correct.
- Shows "Too high!" or "Too low!" hints.
- Counts and displays the number of attempts.
"""

import random

LOWEST = 1
HIGHEST = 100


def get_guess():
    """Ask for a guess and make sure it is a whole number in range."""
    while True:
        raw = input(f"Enter your guess ({LOWEST}-{HIGHEST}): ").strip()
        try:
            guess = int(raw)
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if LOWEST <= guess <= HIGHEST:
            return guess
        print(f"  Your guess must be between {LOWEST} and {HIGHEST}.")


def play_round():
    """Play one game and return the number of attempts used."""
    secret = random.randint(LOWEST, HIGHEST)
    attempts = 0
    print(f"\nI'm thinking of a number between {LOWEST} and {HIGHEST}.")

    while True:
        guess = get_guess()
        attempts += 1  # only valid guesses are counted

        if guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low!")
        else:
            word = "attempt" if attempts == 1 else "attempts"
            print(f"\nCorrect! The number was {secret}.")
            print(f"You guessed it in {attempts} {word}.")
            return attempts


def main():
    print("=== Number Guessing Game ===")
    best = None

    while True:
        attempts = play_round()
        if best is None or attempts < best:
            best = attempts
        print(f"Your best score so far: {best}")

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGame ended. Goodbye!")

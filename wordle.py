from collections import Counter
import random

# This script implements the logic for a Wordle-like game where the player has 6 attempts to guess a 5-letter word.

def checkGuess(target, guess):
    """
    Compares the guess to the target word and returns a string indicating the accuracy of each letter.

    Parameters:
    target (str): The word to be guessed.
    guess (str): The player's guess.

    Returns:
    str: A result string where 'G' indicates a correct letter in the correct position,
         'Y' indicates a correct letter in the wrong position, and 'W' indicates a wrong letter.
    """
    res = ""
    m = Counter(target)
    for i, g in enumerate(guess):
        if m[g] > 0 and g in target:
            if g == target[i]:
                res += "G"
                m[g] -= 1
            else:
                res += "Y"
                m[g] -= 1
        else:
            res += "W"

    return res


def playWordle():
    """
    Runs the main game loop where the player has a fixed number of attempts to guess the target word.
    """

    # List of possible target words for the game
    word_bank = ["HEART", "CHART", "SMART", "START", "PARTY", "CHIEF", "BRIEF", "CRAFT",
                 "GRACE", "BLAST"]

    # Randomly select a target word from the word bank
    target = random.choice(word_bank)
    max_attempts = 6

    print("Welcome to Wordle!")
    print(f"You have {max_attempts} attempts to guess the correct 5-letter word.")

    for attempt in range(1, max_attempts+1):
        guess = input(f"Attempt {attempt}/{max_attempts}. Enter your guess: ").upper()

        # Ensure the player's guess is a 5-letter word
        if len(guess) != 5:
            print("Invalid input. Please enter a 5-letter word.")
            continue

        result = checkGuess(target, guess)
        print(f"{guess}\n{result}")

        # Check if the player has guessed the word correctly
        if result == "GGGGG":
            print("Congrats! You guessed the word correctly!")
            return

    print(f"Sorry, you've run out of attempts. The correct word was {target}.")

# Start the game
playWordle()

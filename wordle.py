from collections import Counter
import random

def checkGuess(target, guess):
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
  
  word_bank = ["HEART", "CHART", "SMART", "START", "PARTY", "CHIEF", "BRIEF", "CRAFT", 
               "GRACE", "BLAST"]

  # Randomly select a target word from the word bank
  target = random.choice(word_bank)
  max_attempts = 6

  print("Welcome to Wordle!")
  print(f"You have {max_attempts} attempts to guess the correct 5-letter word.")

  for attempt in range(1, max_attempts+1):
    guess = input(f"Attempt {attempt}/{max_attempts}. Enter your guess: ").upper()

    if len(guess) != 5:
      print("Invalid input. Please enter a 5-letter word.")
      continue

    result = checkGuess(target, guess)
    print(f"{guess}\n{result}")

    if result == "GGGGG":
      print("Congrats! You guessed the word correctly!")
      return
      
  print(f"Sorry, you've run out of attempts. The correct word was {target}.")

playWordle()

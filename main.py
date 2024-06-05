import random 

def guessing_game():
  rand_num = random.randint(1,100)
  lives = 0

  while True:
    difficulty = input("\nChoose a difficulty: 'Hard' or 'Easy'? \n").lower()
    if difficulty not in ['hard', 'easy']:
      print("Please choose a valid difficulty level. ")
    else:
      if difficulty == 'hard':
        lives = 5
      else:
        lives = 10
      break

  print(f"You have {lives} lives.\n")
      
  while lives > 0:
    player_guess = int(input("Guess a number between 1-100. "))
    if lives == 1:
      print("You ran out of guesses. You lost!")
      break
    elif player_guess < rand_num:
      print("\nToo Low. Guess Again.")
      lives -= 1
      print(f"You have {lives} left.\n")
    elif player_guess > rand_num:
      print("\nToo High. Guess Again.")
      lives -= 1
      print(f"You have {lives} left.\n")
    elif player_guess == rand_num:
      print(f"\nYou Win! The correct number was {rand_num}")
      break
      
guessing_game()
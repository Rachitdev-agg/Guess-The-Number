import random
import art

print(art.logo)
print("Welcome to the Number Guessig Game")
print("I am thinking of a number between 1 and 100")
answer = random.randint(1, 100)
print(answer)
difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
  attempts = 10
if difficulty == "hard":
  attempts = 5
def check_guess():
  global attempts
  if attempts > 0:
    print(f"You have {attempts} remaining to guess the number")
    guess = int(input("Make a guess: "))
  if attempts == 0:
    print("You ran out of guesses")
  elif guess == answer:
    print(f"You got it, The answer was {guess}")
  elif guess > answer:
    print("Too high")
    print("Guess again")
    attempts -= 1
    check_guess()
  elif guess < answer:
    print("Too low")
    print("Guess again")
    attempts -= 1
    check_guess()
  
check_guess()
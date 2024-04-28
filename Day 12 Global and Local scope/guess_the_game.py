import random
from logoart import logo

num = random.randint(1, 100)

print(logo)
print("welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
play = True
while play:
    level = input("Choose the difficulty: easy or hard: ")
    attempts = 0
    if level == "easy":
        attempts = 10
    elif level == "hard":
        attempts = 5
    else:
        print("Invalid Level!")
    while attempts>0:
        guess = int(input("Make a guess: "))
        if guess==num:
            print(f"You got it right the number is {guess} ")
            break
        elif guess>num:
            attempts-= 1
            print(f"Too High! \nGuess again \nYou have {attempts} attempts left.")
        elif guess<num:
            attempts -= 1
            print(f"Too Low! \nGuess again \nYou have {attempts} attempts left.")
    if attempts ==0:
        print(f"Sorry you lose the number is {num}")
    again = input("Do you want to play again? yes or no: ")
    if again == 'no':
        play=False



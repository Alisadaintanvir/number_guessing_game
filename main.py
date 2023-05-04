import random
from art import logo

easy_attempts = 10
hard_attempts = 5
random_number = random.randint(1, 100)

print(logo)
print("Welcome to the number Guessing Game!")
print("I am thinking about a number 1 to 100.")
playing_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")


def game(level):
    """This function takes the game level as a parameter and compare the answer with the guess number"""
    while level != 0:
        print(f"You have {level} attempts remaining to guess the number.")
        level -= 1
        guessed_number = int(input("Make a Guess: "))
        if guessed_number > random_number:
            print("Too High")
            print("Guess Again")
        elif guessed_number == random_number:
            print(f"You got it. The correct answer was {random_number}")
            break
        else:
            print("Too Low")
            print("Guess Again")

    else:
        print("You've run out of guesses, you lose.")


if playing_mode == "easy":
    game(easy_attempts)
elif playing_mode == "hard":
    game(hard_attempts)
else:
    print("Incorrect. Please type again!")

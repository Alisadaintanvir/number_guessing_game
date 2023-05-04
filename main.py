import random
from art import logo

easy = 10
hard = 5
random_number = random.randint(1, 100)

print(logo)
print("Welcome to the number Guessing Game!")
print("I am thinking about a number 1 to 100.")
playing_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")


def make_a_guess(level):
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
    make_a_guess(easy)
elif playing_mode == "hard":
    make_a_guess(hard)
else:
    print("Incorrect. Please type Correctly.")



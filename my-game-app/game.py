import random
import sys

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except EOFError:
            print("Please provide your guess as a command-line argument.")
            sys.exit(1)

        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    if len(sys.argv) > 1:
        guess_number()
    else:
        print("Please provide your guess as a command-line argument.")

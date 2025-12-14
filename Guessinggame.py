print("Guess the number from 1 to 100")
import random
number = random.randint(1,100)
guess = None
while guess != number:
    guess = int(input("Enter your guess:"))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number.")
        
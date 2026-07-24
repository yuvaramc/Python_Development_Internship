import random

def guessing_game():
    random_number = random.randint(1, 100)
    attempts = 0

    print("🎯 Welcome to the Guessing Game!")
    print("Guess a number between 1 and 100")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < random_number:
                print("Too low! Try again.")

            elif guess > random_number:
                print("Too high! Try again.")

            else:
                print("🎉 Congratulations! You guessed the correct number.")
                print("The number was:", random_number)
                print("Total attempts:", attempts)
                break

        except ValueError:
            print("Please enter a valid number.")

guessing_game()
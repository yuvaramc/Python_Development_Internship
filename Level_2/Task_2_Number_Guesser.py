import random

def number_guesser():
    print("🎯 Number Guesser Game")

    start = int(input("Enter starting range: "))
    end = int(input("Enter ending range: "))

    random_number = random.randint(start, end)
    attempts = 0

    print(f"Guess the number between {start} and {end}")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < random_number:
            print("Too low! Try again.")

        elif guess > random_number:
            print("Too high! Try again.")

        else:
            print("🎉 Correct guess!")
            print("Number was:", random_number)
            print("Attempts:", attempts)
            break

number_guesser()
import random

# generate a random number between 1 and 100
answer = random.randint(1, 50)

while True:
    # get player's guess
    guess = int(input("Guess a number between 1 and 50: "))

    if guess == answer:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < answer:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")





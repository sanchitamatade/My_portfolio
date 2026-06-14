import random

secret_number = random.randint(1, 10)

print("🎮 Welcome to Number Guessing Game!")
print("Guess a number between 1 and 10")

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("🎉 Correct! You Won!")
        break
    elif guess < secret_number:
        print("📈 Too Low! Try Again.")
    else:
        print("📉 Too High! Try Again.")

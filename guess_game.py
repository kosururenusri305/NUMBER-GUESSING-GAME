import random

# Step 1: Generate random number
number = random.randint(1, 100)

# Step 2: Initialize variables
guess = None
attempts = 0

print("🎮 Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")

# Step 3: Loop until correct guess
while guess != number:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Step 4: Conditions
        if guess > number:
            print("📉 Too High! Try again.")
        elif guess < number:
            print("📈 Too Low! Try again.")
        else:
            print("🎉 Correct! You guessed it!")

    except ValueError:
        print("❌ Please enter a valid number!")

# Step 5: Show attempts
print(f"✅ You guessed the number in {attempts} attempts.")
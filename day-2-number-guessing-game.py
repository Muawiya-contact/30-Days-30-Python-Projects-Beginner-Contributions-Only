import random

name=input("What is your name please?")
print(name," Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess any number between 1 and 100: ")
    
    if not guess.isdigit():
        print(name,"❌ Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("📉 So low!")
    elif guess > secret_number:
        print("📈 So high!")
    else:
        print(f"✅ Correct! The number was {secret_number}.")
        print(f"🎉 You guessed it in {attempts} attempts.")
        print(name,"you won now try in fewer attempts.")
        break

import random

number = random.randint(1 , 100)
print("Welcome to the Number Guessing Game!")

count = 0
while True:
    X = int(input("Guess The Number (1 - 100) :"))
    count += 1 

    if X < 1 or  X > 100:
        print("invalid Choice!!")
        continue
    if 1 <= X <= 15:
        print("Too Close 🤏")
    elif 16 <= X <= 25:
        print("Try - Try 🤖")
    elif 26 <= X <= 35:
        print("You are cooked 💀")
    elif 36<= X <= 100:
        print("You Figure out 🫷")
    if X == number:
        print("You Guessed It 🚀")
        print(f"It took {count} Tries 🏳️")
        break
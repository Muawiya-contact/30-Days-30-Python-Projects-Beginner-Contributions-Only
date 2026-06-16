import random

def roll_dice(dice) :
    return random.randint(1, dice)

print("Hello! You are playing the game Dice-Roller. Which was made in 15 minutes.\nYour goal: guess the number that will come up on the dice")

dice = int(input("Which cube do you want? "))
attempts = 0

while True:

    x = int(input(f"Please enter a number between 1 and {dice}"))
    dice_roller = roll_dice(dice)

    if x==dice_roller :
        print(f"Congratulations! You guessed the number on the dice in {attempts} moves")
        break
    else :
        print("Sorry, you guessed wrong. Try again.")

    attempts = attempts + 1
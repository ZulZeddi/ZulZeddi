
import random

NUMBER = random.randint(1, 100)
GAME_GOING = True

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def difficulty():
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if diff == 'easy':
        return 10
    elif diff == 'hard':
        return 5
    else:
        return print("You typed incorrect answer.")
    
CHOSEN_DIFFICULTY = difficulty()

count = CHOSEN_DIFFICULTY
while GAME_GOING:
    if count == 0:
        GAME_GOING = False
        print("You loose!")
    else:
        print(f"You have {count} attempts to guess the number.")
        guess_number = int(input("Make a guess: "))
        if guess_number > NUMBER:
            print("Too high.")
            count -= 1
        elif guess_number < NUMBER:
            print("Too low.")
            count -= 1
        else:
            GAME_GOING = False
            print("You win!")
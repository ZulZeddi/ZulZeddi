
import data as dt
import grafic as gr
import random

# global variable for counting player's score
SCORE = 0

# function to compare two accounts
def compare(first, second, choice):
   followers_a = first.get('follower_count')
   followers_b = second.get('follower_count')
   if followers_a > followers_b and choice == 'A':
       return 'correct'
   elif followers_a > followers_b and choice == 'B':
       return 'game_over'
   elif followers_a < followers_b and choice == 'A':
       return 'game_over'
   else:
       return 'correct'
   
# logo printing
print(gr.logo)

# game
is_game_over = False
first_shit = dt.data[random.randint(0, len(dt.data)-1)]
while not is_game_over:
    second_shit = dt.data[random.randint(0, len(dt.data)-1)]
    
    print(f"Compare A: {first_shit.get('name')}, a {first_shit.get('description')}, from {first_shit.get('country')}.")
    
    
    if first_shit == second_shit:
            second_shit = dt.data[random.randint(0, len(dt.data)-1)]
    else:
        print(gr.vs)
            
        print(f"Against B: {second_shit.get('name')}, a {second_shit.get('description')}, from {second_shit.get('country')}.")
        
        choosing = input("Who has more followers? Type 'A' or 'B': ")
        
        if compare(first_shit, second_shit, choosing) == "correct":
            SCORE += 1
            print(f"Your currnet score is {SCORE}.")
            first_shit = second_shit
        else:
            is_game_over = True
            print(f"Your score is {SCORE}")
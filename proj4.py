import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

figures = [rock, paper, scissors]

player_choice_str = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
player_choice = int(player_choice_str)

print(f"You choose: {figures[player_choice]}")

pc_figure = random.randint(0, 2)

print(f"PC choose: {figures[pc_figure]}")

if int(player_choice) == 0:
    if pc_figure == 0:
        print("Draw!")
    elif pc_figure == 1:
        print("PC win!")
    else:
        print("You win!")
elif int(player_choice) == 1:
    if pc_figure == 0:
        print("You win!")
    elif pc_figure == 1:
        print("Draw!")
    else:
        print("PC win!")
else:
    if pc_figure == 0:
        print("PC win!")
    elif pc_figure == 1:
        print("You win!")
    else:
        print("Draw!")    
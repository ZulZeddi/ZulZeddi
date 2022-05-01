from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)
print("Welcome to the secret auction program")

any_other_bidders = True
bidders = {}

while any_other_bidders:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  bidders[bid] = name #adding to dict
  any_other = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if any_other == 'yes':
    clear()
  else:
    any_other_bidders = False

values = bidders.keys()
bigger_value = 0
for value in values:
  if value > bigger_value:
    bigger_value = value
  
print(f"The winner is {bidders[bigger_value]} with a bid of ${bigger_value}")
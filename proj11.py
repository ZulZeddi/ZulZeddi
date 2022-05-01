import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#starting with 2 cards on hands


def get_another_card(players_list):
    players_list.append(random.choice(cards))


def game():
    end_of_game = False
    while not end_of_game:
                
        if sum(my_hand) == 21:
            print("You have a BlackJack! You win!")
            end_of_game = True
            print(my_hand)
            print(comp_hand)
        elif sum(comp_hand) == 21:
            print("Dealer has a BlackJack! You lose!")
            end_of_game = True
            print(my_hand)
            print(comp_hand)
        else:
            if sum(my_hand) > 21:
                if 11 in my_hand:
                    if sum(my_hand) - 10 > 21:
                        print("You lose! You have over 21!")
                        end_of_game = True
                        print(my_hand)
                        print(comp_hand)
                    else:
                        if input("Do you want to get another card? Type 'yes' or 'no' ") == 'yes':
                            get_another_card(my_hand)
                            print(f"Your current set {my_hand}")
                        else:
                            get_another_card(comp_hand)
                            game()
                else:
                    print("You lose! You have over 21!")
                    end_of_game = True
                    print(my_hand)
                    print(comp_hand)
            else:
                choice = input("Do you want to get another card? Type 'yes' or 'no' ")
                if choice == 'yes':
                    get_another_card(my_hand)
                    print(f"Your current set {my_hand}")
                    if sum(my_hand) > 21:
                        print("You lose! You have over 21!")
                        end_of_game = True
                        print(my_hand)
                        print(comp_hand)
                    else:    
                        if sum(comp_hand) < 17:
                            get_another_card(comp_hand)
                            if sum(comp_hand) > 21:
                                print("Dealer has over 21! You win!")
                                end_of_game = True
                                print(my_hand)
                                print(comp_hand)
                        else:
                            if sum(my_hand) > sum(comp_hand):
                                print("You win!")
                                print(my_hand)
                                print(comp_hand)
                            elif sum(my_hand) < sum(comp_hand):
                                print("You lose!")
                                print(my_hand)
                                print(comp_hand)
                            else:
                                print("Draw!")
                                print(my_hand)
                                print(comp_hand)
                else:
                    if len(comp_hand) < len(my_hand):
                        get_another_card(comp_hand)
                    elif sum(my_hand) > sum(comp_hand):
                        print("You win!")
                        print(my_hand)
                        print(comp_hand)
                    elif sum(my_hand) < sum(comp_hand):
                        print("You lose!")
                        print(my_hand)
                        print(comp_hand)
                    else:
                        print("Draw!")
                        print(my_hand)
                        print(comp_hand)
                        
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    my_hand = []
    comp_hand = []
    my_hand.append(random.choice(cards)) 
    comp_hand.append(random.choice(cards))
    my_hand.append(random.choice(cards))
    comp_hand.append(random.choice(cards))
    print(f"Yout cards: {my_hand}, current score {sum(my_hand)}")
    print(f"Dealer's hand: {comp_hand[0]}")
    game()

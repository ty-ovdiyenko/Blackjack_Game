# Import statements
from p1_random import P1Random

# Global vars
card_value = 0

# Functions

def randcard(rng):
    global card_value #global so it can be accessed throughout the whole program 
    card_num = rng.next_int(13) + 1 #range 1-13

    if card_num == 1:
        card_value = 1
        card_type = "ACE"
    elif card_num >= 2 and card_num <= 10:
        card_value = card_num
        card_type = str(card_num)
    else:
        card_value = 10
        if card_num == 11:
            card_type = "JACK"
        elif card_num == 12:
            card_type = "QUEEN"
        else:
            card_type = "KING"

    return card_type, card_value

def main():
    # Initialize the random number generator
    rng = P1Random()

    # Variables
    end = 0
    game_count = 1
    player_wins = 0
    dealer_wins = 0
    num_ties = 0

    # Loop to count the number of games
    while end < 1:
        hand_val = 0  # Each game has to start with a hand value of 0

        print("START GAME #", game_count)

        card_type, card_val = randcard(rng)
        print("Your card is a", card_type + "!")
        hand_val += card_val
        print("Your hand is:", hand_val)

        while hand_val < 21:
            while True:
                choice = input("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n\nChoose an option: ")
                if choice.isdigit(): #checks to make sure the input is a digit to avoid error
                    choice = int(choice)
                    if choice in [1, 2, 3, 4]:
                        break #goes to choice booleans
                    else:
                        print("Invalid input!\n Please enter an integer value between 1 and 4.")
                else:
                    print("Invalid input!\n Please enter an integer value between 1 and 4.")
                    
            if choice == 1:
                card_type, card_val = randcard(rng)
                print("\nYour card is a", card_type + "!")
                hand_val += card_val
                print("\nYour hand is:", hand_val)

                if hand_val == 21:
                    print("BLACKJACK! You win!")
                    player_wins += 1
                    break
                elif hand_val > 21:
                    dealer_wins+=1
                    print("You exceeded 21! You lose.")
                    break

            elif choice == 2:
                dealer_hand = rng.next_int(11) + 16
                print("Dealer's hand:", dealer_hand)
                print("Your hand is:", hand_val)

                if dealer_hand == 21:
                    print("Dealer wins!")
                    dealer_wins += 1
                    break

                elif dealer_hand > 21:
                    print("You win!")
                    player_wins += 1
                    break

                elif hand_val == dealer_hand:
                    print("It's a tie! No one wins!")
                    num_ties += 1
                    break

                elif dealer_hand > hand_val:
                    print("Dealer wins!")
                    dealer_wins += 1
                    break

                else:
                    print("You win!")
                    player_wins += 1
                    break

            elif choice == 3:
                # i did individual print lines instead of one big line so its more readable
                print("Number of Player wins:", player_wins)
                print("Number of Dealer wins:", dealer_wins)
                print("Number of tie games:", num_ties)
                print("Total # of games played is:", game_count - 1)
                if game_count > 1:
                    print("Percentage of Player wins:", (player_wins / (game_count - 1)) * 100, "%\n")
                else:
                    print("Percentage of Player wins: 0.0 %\n")

            elif choice == 4:
                end += 1  # Exit the game loop
                break

        game_count += 1

if __name__ == "__main__": #calls main to start the game. 
    main()

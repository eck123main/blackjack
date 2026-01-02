import random
values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6,"7": 7, "8": 8, "9": 9, "10": 10,"J": 10, "Q": 10, "K": 10,"A": 11}
balance = 100
print("You start with $100 balance")

def bet_try(balance):
    while True:
        try:
            bet = int(input(f"You have ${balance}. How much would you like to bet? "))
            if 1 <= bet <= balance:
                return bet
            else:
                print(f"Bet must be between 1 and {balance}")
        except ValueError:
            print("Please enter a valid integer")


def ace_calc(total,ace):
    while total > 21 and ace > 0:
        total -= 10
        ace -= 1
    return total, ace

def player_turn(deck):
    total = 0
    ace = 0
    hand = []


    for i in range(2):
        card = deck.pop()
        hand.append(card)
        total += values[card]
        if card == "A":
            ace += 1

    total, ace = ace_calc(total, ace)



    print(f"Your total is now: {total}")
    print(f"Your hand: {hand}")

    while total < 21:
        while True:
            hit = input("\nWould you like to hit? yes/no input: ").strip().lower()
            if hit == "yes" or hit == "no":
                break
            print("Please only type yes or no as an answer")
        if hit == "no":
            break
        card = deck.pop()
        hand.append(card)
        total += values[card]
            
        if card == "A":
            ace += 1
        total, ace = ace_calc(total, ace)
            
        print(f"\nYour hand: {hand} total: {total}")
        if total >= 21:
            break

    if total == 21:
        print("Blackjack! You hit 21")
    elif total > 21:
        print("You busted!")

    return total, hand

def dealer_turn(deck, player_total, dealer_hand):
    total = values[dealer_hand[0]]  # value of the first card
    ace = 0
    if dealer_hand[0] == 'A':
        ace = 1
    
    total, ace = ace_calc(total, ace)
    
    print("\nDealers turn\n")


    second_card = deck.pop()
    dealer_hand.append(second_card)
    total += values[second_card]
    if second_card == 'A':
        ace += 1
    total, ace = ace_calc(total, ace)


    print(f"Dealer second card: {second_card}")
    print(f"Dealer total is now: {total}")
    print(f"Dealers hand: {dealer_hand}")
    print(f"Player total to beat: {player_total}\n")

    while total < 17:
        card = deck.pop()
        dealer_hand.append(card)
        total += values[card]
        if card == "A":
            ace += 1
        total, ace = ace_calc(total, ace)
        print(f"Dealer draws: {card}, their total now: {total}")
    
        if total >= 21:
            break
    if total == 21:
        print("dealer hit 21")
    elif total > 21:
        print("Dealer busted")
    
    print(f"Dealer final total: {total}")
    return total, dealer_hand

def main():
    global balance
    
    while balance > 0:
        deck = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] * 4 # full deck
        random.shuffle(deck)
        bet = bet_try(balance)
        
        dealer_hand = [deck.pop()]
        print(f"Dealer shows: {dealer_hand[0]}")
        print("Other card remains hidden")


        player_total, player_hand = player_turn(deck)
        
        if player_total > 21: # plaeyer bust
            print(f"player busted, dealer wins. You unfortunately lose your bet of ${bet}")
            balance -= bet
        else:      
            dealer_total, dealer_hand = dealer_turn(deck, player_total, dealer_hand)


            if dealer_total > 21: # dealer bust
                print(f"dealer busted, player wins. Congratulations! You win your bet of ${bet}")
                balance += bet
            else:

                print("\nFinal results")
                print(f"Player hand: {player_hand}, total: {player_total}")
                print(f"Dealer hand: {dealer_hand}, total: {dealer_total}")

                if dealer_total > player_total:
                    print(f"Dealer wins! You unfortunately lose your bet of ${bet}")
                    balance -= bet
                elif dealer_total == player_total:
                    print("Tie! no win")
                else:
                    print(f"Player wins! Congratulations! You win your bet of ${bet}")
                    balance += bet
            
        print(f"\nYour balance: ${balance}")
        if balance == 0:
            print("You have bet all your money and have none left. Game over.")
            break
        while True:
            play_again = input("\nDo you want to play another round? yes/no: ").strip().lower()
            if play_again == "yes":
                break
            elif play_again == "no":
                print(f"Thanks for playing! Your final balance is: {balance}")               
                return #exit
            else:
                print("Please only type yes/no")

if __name__ == "__main__":
    main()
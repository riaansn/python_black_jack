"""
   This is the game specific functions...
"""
from card_values import playing

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry only integers are acceptable...')
        else:
            if chips.bet > chips.total:
                print('Sorry!! You do not have enough chips for this bet! Available: {}'.format(chips.total))
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck,hand) # hit() function as defined above...
            return True
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing. ")
            playing = False
            return playing
        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's hand:")
    print(" <card hidden>")
    print('', dealer.cards[0])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player, dealer, chips):
    print("Player Busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player Wins!!!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer Busts!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer Wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")
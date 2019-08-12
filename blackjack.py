from deck import Deck
from hand import Hand
from chips import Chips
from blackjack_functions import *

global playing

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

    # Create & shuffle the deck, deal two cards to each player
    the_deck = Deck()
    the_deck.shuffle()

    player_one = Hand()
    dealer = Hand()

    player_one.add_card(the_deck.deal())
    dealer.add_card(the_deck.deal())
    player_one.add_card(the_deck.deal())
    dealer.add_card(the_deck.deal())    
    
    # Set up the Player's chips
    deposit_chips = int(input("How many chips do you want to deposit? "))
    player_chips = Chips(deposit_chips)
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_one, dealer)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        playing = hit_or_stand(the_deck, player_one)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_one, dealer)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_one.value > 21:
        	player_busts(player_one, dealer, player_chips)

        break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_one.value <= 21:
        
        while dealer.value < 17:
            hit(the_deck, dealer)
    
        # Show all cards
        show_all(player_one, dealer)

        # Run different winning scenarios
        if dealer.value > 21:
        	dealer_busts(player_one, dealer, player_chips)
        elif dealer.value > player_one.value:
        	dealer_wins(player_one, dealer, player_chips)
        elif dealer.value < player_one.value:
        	player_wins(player_one, dealer, player_chips)
        else:
        	push(player_one, dealer)
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break
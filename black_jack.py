'''
Black Jack
'''
from bj_module import dealers_card
from bj_module import players_card
# from colorama import Fore
import random
import os
import time

# Initiate global variables
game = True
first_game = True
dealer = True
player = True


# CLASS
class PlayerCredits():
    '''
    PlayerCred
    '''
    def __init__(self, credits):
        '''
        __init__
        '''
        # Set balance to credits bought by Player
        self.balance = credits
        self.bet = 0
        # Set Dealers bank to 1000
        self.bank = 1000


    def win(self, stake, player):
        '''
        win
        '''
        # Subtract bet from balance
        self.balance -= stake
        # Value of Player's hand
        self.player = player

        # If Player got BlackJack
        if player == 21:
            # Pot won is 2.5 times the bet
            pot = round(self.bet * 2.5)
            self.balance +=  pot
            # Dealer's bank lose bet times 1.5
            self.bank -= round(self.bet * 1.5)
                  
        # Else Player win
        else:
            # Pot won is 2 times bet
            pot = self.bet * 2
            self.balance += pot
            # Dealer's bank lose bet
            self.bank -= self.bet

        # If bank has money
        if self.bank > 0:
            print(f'\nCongratultions! You won ${pot}!')
            print(f'You now have ${credits.balance} in credits')
            
            # Game is still on
            return True

        # Else the bank was blown!
        else:
            print(f'\nYou BLEW the Bank and won ${pot}!')
            print(f'You now have ${credits.balance} in your pocket')
            print('\nThe Dealer got fired!')
            # No more bets possible!
            return False

    def lose(self):
        '''
        bet
        '''
        # Dealer win bet
        self.bank += self.bet
        # Player lose bet
        self.balance -= self.bet

        # If Player still have credits
        if self.balance > 0:
            print(f'\nYou have ${credits.balance} of credits left')
            
            # Game is still on
            return True
       
        # Else Player is out of credits!    
        else:
            print('You are broke, time to go home!')
            # No more bets allowed
            return False 


# FUNCTIONS
def new_deck():
    '''
    new_deck
    '''
    # Initiate empty deck
    shuffled_cards = []

    # Create shuffled deck of 52 individual cards
    while len(shuffled_cards) < 52:
        # Randomize suit and rank
        sr = [random.randint(0, 3), random.randint(0, 12)]
        # If suit and rank not present
        if sr not in shuffled_cards:
            # Add suit and rank to deck
            shuffled_cards.append(sr)

    # Return new shuffled deck
    return shuffled_cards


def buy_credits():
    '''
    buy_credits
    '''
    while True:
        # Bet must be an integer
        try:    
            # Ask for Player's bet
            chips = int(input('How much credits do you want to buy?\n$'))

        # Incorrect input!
        except:
            # Clear sceen before asking for credits
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nTry again, credits must be an integer!')

        else:
            break

    return chips


def comebacks_for_incorrect_input():
    '''
    comebacks_for_incorrect_input
    '''
    random_retries = ["\nHad too many drinks, did you? Please try again!", "\nAre you drunk? Please try again!",
    "\nThat is not how you spell MOON? Please try again!", "\nWhat are you doing Dave? Please try again!",
    "\nI ignored you just fine the first time! Please try again!",
    "\nUnless your name is Google, stop acting like you know everything! Please try again!",
    "\nIf you're gonna be a smart ass, first you have to be smart! Please try again!",
    "\nRoses are red, violets are blue, I've got five fingers, the middle one is for you! Please try again!",
    "\nYou're entitled to your incorrect opinion, but please try again!",
    "\nI'd agree with you, but then we'd both be wrong! Please try again!",
    "\nI bet your brain feels as good as new, seeing as how you've never used it! Please try again!",
    "\nIf you can't be a good example, then you'll have to be a terrible warning! Please try again!",
    "\nStupidity is not a crime so you are free to go, but please try again!",
    "\nI don't think you are stupid. You just have a bad luck when thinking! Please try again!"]

    i = random.randint(0,13)

    return print(random_retries[i])


def take_bet(credits):
    # Global variable to be able to set it permanent
    global first_game

    # If first_game equals True do not clear screen 
    if first_game == True:
        # Set first_game to False to skip Welcome message and buying of credits next time
        first_game = False

    # Else clear screen
    else:
        # Clear sceen before asking for bet
        os.system('cls' if os.name == 'nt' else 'clear') 
    
    # While Player hasn't placed bet
    while True: 
        # Bet must be an integer
        try:    
            # Ask for Player's bet
            credits.bet = int(input('How much would you like to bet?\n$'))

        # Incorrect input!
        except:
            # Clear sceen before asking for bet again
            os.system('cls' if os.name == 'nt' else 'clear')
            comebacks_for_incorrect_input()
            
        # Not enough credits!
        else:
            if credits.bet > credits.balance:
                print('\nYour bet is too high, place a lower bet!')
                print(f'\nYou have ${credits.balance} credits left')

            else:
                break

    # Bet is placed 
    if credits.balance > credits.bet:
        # Show Player's stake, and get ready to play!
        print(f'\nYour stake is ${credits.bet}')
        print('Get ready for your cards!\n')

    # Player bet all credits 
    else:
        print('\nALL IN!!!')
        print('You have no more credits left!')
        print('Get ready for your cards!\n')


def hit_or_stand():
    '''
    hit_or_stand
    '''
    # Global variables to be able to set them permanent
    global player, dealer

    # While Player wants new card/ is satisfied/ not have BlackJack
    while True:
        # Show first hidden card if Player not choose to stay
        if players_hand.turn == 1:
            # Player got BlackJack - Dealer's turn
            if players_hand.sum == 21:
                print(f'\nYou\'ve got BlackJack! Dealers is playing.')
                # End of Player turn
                player = False
                # Pause for Player to be able to read text
                time.sleep(2)
                # Break hit_or_stand loop
                break
            
            answer = input("\nWould you like to Hit or Stand? Enter 'h' or 's': ")
            # If Player choose Hit, show first hidden card
            if not answer == '' and answer[0].lower() == 'h':
                players_hand.player_three_open()
                players_hand.adjust_for_player_aces()
                # Clear sceen before showing new card
                os.system('cls' if os.name == 'nt' else 'clear')
                # Print Dealer's and Player's cards and value of Player's cards
                print('')
                print(dealers_hand.card)
                print(players_hand.card)
                print(f'You have: {players_hand.sum}') 
                # Break hit_or_stand loop
                break

            # No new cards
            elif not answer == '' and answer[0].lower() == 's':
                print("\nPlayer stands. Dealer is playing.")
                # End of Player turn
                player = False
                # Pause for Player to be able to read text
                time.sleep(2)
                # Break hit_or_stand loop
                break
            
            # Incorrect input
            else:
                print("\nSorry, please try again.")
                # Go to top of hit_or_stand loop
                continue

        answer = input("\nWould you like to Hit or Stand? Enter 'h' or 's': ")
        
        # If Player choose Hit, show new card
        if not answer == '' and answer[0].lower() == 'h':
            players_hand.player_new_card()
            players_hand.adjust_for_player_aces()
            # Clear sceen before showing new card
            os.system('cls' if os.name == 'nt' else 'clear')
            # Print Dealer's and Player's cards and value of Player's cards
            print('')
            print(dealers_hand.card)
            print(players_hand.card)
            print(f'You have: {players_hand.sum}')
            # Break hit_or_stand loop
            break

        # No new cards   
        elif not answer == '' and answer[0].lower() == 's':
            print("\nPlayer stands. Dealer is playing.")
            # End of Player turn
            player = False
            # Pause for Player to be able to read text
            time.sleep(2)
            # Break hit_or_stand loop
            break

        # Incorrect input
        else:
            comebacks_for_incorrect_input()
            # Go to top of hit_or_stand loop
            continue


def evaluate_player():
    '''
    evaluate_player
    '''
    # Global variables to be able to set them permanent
    global game, player, dealer

    # If Player Bust
    if players_hand.turn > 1 and players_hand.sum > 21:
        print(f'\nYou are Bust!')
        game = credits.lose()
        
        # Deal is over
        player = False
        dealer = False

    # If Player got BlackJack - Dealer's turn
    elif players_hand.turn > 1 and players_hand.sum == 21:
        print(f'\nYou\'ve got BlackJack! Dealers is playing.')
        # End of Player's turn
        player = False
        # Pause for Player to be able to read text
        time.sleep(2)


def evaluate_dealer():
    '''
    evaluate_dealer
    '''
    # Global variables to be able to set them permanent
    global game, dealer

    # Dealer lose
    # If Dealer Bust
    if dealers_hand.sum > 21:
        print_dealer_player_points()
        print('\nThe Dealer is Bust!')
        game = credits.win(credits.bet, players_hand.sum)
        # Deal is over
        dealer = False

    # Dealer lose
    # If Dealer reached 17 and Player's cards are higher
    elif dealers_hand.sum >=17 and dealers_hand.sum < players_hand.sum:
        print_dealer_player_points()
        game = credits.win(credits.bet, players_hand.sum)
        # Deal is over
        dealer = False

    # Dealer win
    # If Dealer hit 21 and no Push, or Dealer got higher than the Player's cards
    elif dealers_hand.sum == 21 and not players_hand.sum == 21\
    or dealers_hand.sum > 17 and dealers_hand.sum > players_hand.sum:
        print_dealer_player_points()
        print('\nThe Dealer Wins!')
        game = credits.lose()
        # Deal is over
        dealer = False

    # It's a draw
    # If both have the same total value of their cards
    elif dealers_hand.sum >=17 and dealers_hand.sum == players_hand.sum:
        print_dealer_player_points()
        print('\nIt\'s a Push!')
        print(f'Your bet of ${credits.bet} is returned')
        print(f'You still have ${credits.balance} of credits')
        # Deal is over
        dealer = False

    # Keep dealing
    # Dealer has not yet reached 17
    else:
        print_dealer_player_points()


def print_dealer_player_points():
    '''
    print_dealer_player_points
    '''
    # Print Dealer's and Player's cards and their values
    print(f'Dealer has: {dealers_hand.sum}')
    print(dealers_hand.card)
    print(players_hand.card)
    print(f'You have: {players_hand.sum}')


# __main__

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# Prepare new deck
deck = new_deck()
# Prepare Dealer's hand
dealers_hand = dealers_card.DealersCard(deck)
# Prepare Player's hand
players_hand = players_card.PlayersCard(deck)

while game:
    # Clear screen for new hands
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Prepare Dealer cards
    dealers_hand.dealer_one_open_one_closed()
    dealers_hand.adjust_for_dealer_aces()

    # Prepare Player cards
    players_hand.player_two_open_one_closed()
    players_hand.adjust_for_player_aces()

    # If first turn
    if first_game == True:
        # Welcome message
        print('Welcome to BlackJack!') 
        print('Get as close to 21 as you can without going over!')
        print('Dealer hits as long as Dealer is below 17.\nAces count as 1 or 11.\n')
        
        # Prepare Player's credits
        credits = PlayerCredits(buy_credits())
        
        # Clear sceen before asking for bet
        os.system('cls' if os.name == 'nt' else 'clear') 
        print(f'\nYou have ${credits.balance} of credits')

    take_bet(credits)

    # Pause for Player to be able to read text
    time.sleep(3)

    # Clear sceen before showing new card
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print Dealer's and Player's cards and value of Player's cards
    print('')
    print(dealers_hand.card)
    print(players_hand.card)
    print(f'You have: {players_hand.sum}') 

    # While Player hits:
    while player:
        # Ask Player if Player want to hit new card or stand
        hit_or_stand()
        # Look for Bust or BlackJack
        evaluate_player()

    if game == False:
        break

    # While Dealer hits  
    while dealer:
        # Show Dealer's hidden card
        # If first turn
        if dealers_hand.turn == 1:
            # Clear sceen before showing new card
            os.system('cls' if os.name == 'nt' else 'clear')
            dealers_hand.dealer_two_open()
            dealers_hand.adjust_for_dealer_aces()
            # Look for winner
            evaluate_dealer()

        # Dealer hits as long as Dealer is below 17, or until Dealer is Bust
        else:
            # Wait a bit until next card is shown
            time.sleep(0.7)
            # Clear sceen before showing new card
            os.system('cls' if os.name == 'nt' else 'clear')
            # Show Dealer's new card
            dealers_hand.dealer_new_card()
            dealers_hand.adjust_for_dealer_aces()
            # Look for winner
            evaluate_dealer()

    if game == False:
        break


    # Ask Player for new game until correct answer
    while True:
        # Wait 3 seconds until ask for new game
        time.sleep(3)

        new_game = input("\nWould you like to play again? Enter 'y' or 'n': ")
        
        # If Player want to play again
        if not new_game == '' and new_game[0].lower() == 'y':
            # Reset player and dealer
            dealer = True
            player = True
            # Reset sum of cards
            dealers_hand.reset_game_data()
            players_hand.reset_game_data()
            # Break want_to_play_again loop
            break

        # Else quit game 
        elif not new_game == '' and new_game[0].lower() == 'n':
            print('Thank you for playing, have a nice evening!')
            game = False
            # Break want_to_play_again loop
            break

        # Incorrect input
        else:
            # Clear sceen before asking for credits
            os.system('cls' if os.name == 'nt' else 'clear')

            print("\nHad too many drinks? Please try again!")
            # Go to top of want_to_play_again loop
            continue

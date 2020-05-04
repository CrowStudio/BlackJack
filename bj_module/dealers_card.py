'''
dealers_card
'''
# Suit ♠, ♥, ♣, ♦
suit = ['\u2660', '\u2665', '\u2663', '\u2666']
# Rank 2 - Ace
# Index 0 of list in index 0 in rank = rank in top left corner of card
# Index 1 of list in index 0 in rank = rank in bottom right corner of card
rank = [['2 ', ' 2'], ['3 ', ' 3'], ['4 ', ' 4'],
        ['5 ', ' 5'], ['6 ', ' 6'], ['7 ', ' 7'],
        ['8 ', ' 8'], ['9 ', ' 9'], ['10', '10'],
        ['Kn', 'Kn'], ['Q ', ' Q'], ['K ', ' K'],
        ['E ', ' E']]
# Value of rank
value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


class DealersCard():
    '''
    DealerCard
    '''
    # INIT
    def __init__(self, deck):
        '''
        __init__
        '''
        # Initiate variables
        self.deck = deck
        self.i = 0
        self.i1, self.i2, self.i3, self.i4, self.i5 = 0, 0, 0, 0, 0
        self.dealer_line0 = ''
        self.dealer_line1 = ''
        self.dealer_line2 = ''
        self.dealer_line3 = ''
        self.dealer_line4 = ''
        self.dealer_line5 = ''
        self.dealer_line6 = ''
        self.rank = []
        self.suit = []
        self.sum = 0
        self.aces = 0
        self.hand = []
        self.card = ''


    # PRIVATE METHODS
    def __set_hand(self):  
        '''
        __set_hand
        '''
        # List of cards - 
        # Index 0 = hidden card, index 1-5 = card rank and suit,
        # every +5 indexes is next card
        self.hand = ['#######',
        ' ' + self.rank[0][0] + '    ',
        '       ',
        '   ' + self.suit[0][0] + '   ',
        '       ',
        '    ' + self.rank[0][1] + ' ',
        ' ' + self.rank[1][0] + '    ',
        '       ',
        '   ' + self.suit[1][0] + '   ',
        '       ',
        '    ' + self.rank[1][1] + ' ']


    def __set_card(self):
        '''
        __set_card
        '''
        # Setup of card's suit looking through suit list
        for s in range(len(suit)):
            # If suit equals suit of index 0 0 in deck
            if s == self.deck[0][0]:
                # Add suit to list of Dealer suits
                self.suit.append(suit[s])
                # Break foor loop when suit is found
                break

        # Setup of card's rank looking through rank-list
        for r in range(len(rank)):
            # If rank equals rank of index 0 1 in deck
            if r == self.deck[0][1]:
                # Add rank to list of Dealer's ranks
                self.rank.append(rank[r])
                # Add value of rank
                self.sum += value[r]
                # Store latest value
                adjust_value = value[r]
                # Break foor loop when rank is found
                break

        # If value is of Ace
        if adjust_value == 11:
            # Keep count of aces
            self.aces += 1


    def __append_to_hand(self):
        '''
        __append_to_hand
        '''
        # Add Dealer's rank and suit, of index i, to hand
        self.hand.append(' ' + self.rank[self.i][0] + '    ')
        self.hand.append('       ')
        self.hand.append('   ' + self.suit[self.i][0] + '   ')
        self.hand.append('       ')
        self.hand.append('    ' + self.rank[self.i][1] + ' ')


    def __dealer_two_cards(self):
        '''
        __dealer_two_cards
        '''
        # Hide second card
        # If Dealer's first turn
        if self.turn == 1:
            self.i1, self.i2, self.i3, self.i4, self.i5 = 0, 0, 0, 0, 0

        # Else Show second card
        else:
            self.i1, self.i2, self.i3, self.i4, self.i5 = 6, 7, 8, 9, 10
        
        # Build Dealer's first cards
        self.dealer_line0 = '*********' + '   *********'
        self.dealer_line1 = '*' + self.hand[1] + '*' + '   *'+ self.hand[self.i1] + '*'
        self.dealer_line2 = '*' + self.hand[2] + '*' + '   *'+ self.hand[self.i2] + '*'
        self.dealer_line3 = '*' + self.hand[3] + '*' + '   *'+ self.hand[self.i3] + '*'
        self.dealer_line4 = '*' + self.hand[4] + '*' + '   *'+ self.hand[self.i4] + '*'
        self.dealer_line5 = '*' + self.hand[5] + '*' + '   *'+ self.hand[self.i5] + '*'
        self.dealer_line6 = '*********' + '   *********'


    def __new_dealer_card(self):
        '''
        __new_dealer_card
        '''
        # Set indexes for new card
        self.i1 += 5
        self.i2 += 5
        self.i3 += 5
        self.i4 += 5
        self.i5 += 5
     
        # Add new Dealer card
        self.dealer_line0 += '   *********'
        self.dealer_line1 += '   *'+ self.hand[self.i1] + '*'
        self.dealer_line2 += '   *'+ self.hand[self.i2] + '*'
        self.dealer_line3 += '   *'+ self.hand[self.i3] + '*'
        self.dealer_line4 += '   *'+ self.hand[self.i4] + '*'
        self.dealer_line5 += '   *'+ self.hand[self.i5] + '*'
        self.dealer_line6 += '   *********'      


    def dealer_one_open_one_closed(self):
        '''
        dealer_one_open_one_closed
        '''
        # Set turn
        self.turn = 1

        # Set card's rank of suit
        self.__set_card()
        # Add 1 to card index
        self.i += 1
        # Remove card from deck
        self.deck.pop(0)

        # Set card's rank of suit
        self.__set_card()
        # Add 1 to card index
        self.i += 1
        # Remove card from deck
        self.deck.pop(0)

        # Set initial Dealer hand
        self.__set_hand()

        # Create cards for Dealer's hand
        self.__dealer_two_cards()

        # Add a new line to enable print of Dealer's hand
        new_line = '\n'

        # Build Dealer's hand
        self.card = self.dealer_line0 + new_line + self.dealer_line1 + new_line\
         + self.dealer_line2 + new_line + self.dealer_line3 + new_line + self.dealer_line4\
         + new_line + self.dealer_line5 + new_line + self.dealer_line6 + new_line



    def dealer_two_open(self):
        '''
        dealer_two_open
        '''
        # Set turn
        self.turn = 2

        # Create cards for Dealer's hand
        self.__dealer_two_cards()

        # Add a new line to enable print of Dealer's hand
        new_line = '\n'

        # Build Dealer's hand
        self.card = self.dealer_line0 + new_line + self.dealer_line1 + new_line\
         + self.dealer_line2 + new_line + self.dealer_line3 + new_line + self.dealer_line4\
         + new_line + self.dealer_line5 + new_line + self.dealer_line6 + new_line


    def dealer_new_card(self):
        '''
        dealer_new_card
        '''
        # Set turn
        self.turn +=1
       
        # Set card's rank of suit
        self.__set_card()
        # Add new card to hand
        self.__append_to_hand()
        # Add 1 to card index
        self.i += 1
        # Remove card from deck
        self.deck.pop(0) 

        # Create card for Dealer's hand
        self.__new_dealer_card()

        # Add a new line to enable print of Dealer's hand
        new_line = '\n'

        # Build Dealer's hand
        self.card = self.dealer_line0 + new_line + self.dealer_line1 + new_line\
         + self.dealer_line2 + new_line + self.dealer_line3 + new_line + self.dealer_line4\
         + new_line + self.dealer_line5 + new_line + self.dealer_line6 + new_line
 
        
    def adjust_for_dealer_aces(self):
        '''
        __adjust_for_aces
        '''
        # While sum of cards is great than 21 and there is aces in hand
        while self.sum > 21 and self.aces:
            # Aces counts as 1 instead of 11
            self.sum -= 10
            # Remove aces from ace count
            self.aces -= 1  


    def reset_game_data(self):
        '''
        reset_sum
        '''
        # Reset Dealer's game data
        self.i = 0
        self.i1, self.i2, self.i3, self.i4, self.i5 = 0, 0, 0, 0, 0
        self.rank = []
        self.suit = []
        self.sum = 0
        self.aces = 0
        self.hand = []
        self.card = ''

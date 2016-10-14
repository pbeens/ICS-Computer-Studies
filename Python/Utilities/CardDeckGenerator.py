'''
This program generates a randomly sorted deck of cards, with the output as shown:

3S
6D
4S
.
.
.
'''

# import sections
import random

# prepare the deck
suits = ['S', 'C', 'D', 'H']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
cards = []

# build the deck of cards, in order -> cards[]
for suit in suits:
    for rank in ranks:
        cards.append(rank + suit)

# shuffle the deck
random.shuffle(cards)

# write the cards file
cardsFile = 'randomCards.txt' # << Change filename here!
file = open(cardsFile,'w')
for card in cards:
    file.write(card + '\n')
    print (card)
file.close()

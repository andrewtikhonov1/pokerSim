import csv
import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['d', 'h', 'c', 's'] 


full_deck = [rank + suit for rank in ranks for suit in suits]
csv_file_path = 'hands.csv'

with open(csv_file_path, mode='w', newline='') as file:
    csv_writer = csv.writer(file)

for i in range(1000):
    deck = full_deck.copy()

    card1 = random.choice(deck)
    card1val = 0
    if (card1[0] == 'A'):
        card1val = 14
    elif (card1[0] == 'K'):
        card1val = 13
    elif (card1[0] == 'Q'):
        card1val = 12
    elif (card1[0] == 'J'):
        card1val = 11
    elif (card1[0] == 'T'):
        card1val = 10
    else:
        card1val = int(card1[0])
    deck.remove(card1)

    card2 = random.choice(deck)
    card2val = 0
    if (card2[0] == 'A'):
        card2val = 14
    elif (card2[0] == 'K'):
        card2val = 13
    elif (card2[0] == 'Q'):
        card2val = 12
    elif (card2[0] == 'J'):
        card2val = 11
    elif (card2[0] == 'T'):
        card2val = 10
    else:
        card2val = int(card2[0])
    deck.remove(card2)

    print(card1, card2)

    hand = ""
    if (card2val > card1val):
        if (card1[1] == card2[1]):
            hand = str(card2[0]) + str(card1[0]) + "s"
        else:
            hand = str(card2[0]) + str(card1[0]) + "o"
    elif (card1val == card2val):
        hand = str(card2[0]) + str(card1[0])
    else:
        if (card1[1] == card2[1]):
            hand = str(card1[0]) + str(card2[0]) + "s"
        else:
            hand = str(card1[0]) + str(card2[0]) + "o"

    print(hand)

    with open(csv_file_path, mode='a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([hand])

import random
from itertools import combinations

def s(v):
  if v == 10:
    return "T"
  if v == 11:
    return "J"
  if v == 12:
    return "Q"
  if v == 13:
    return "K"
  if v == 14:
    return "A"
  return str(v)

def winPrint(wp, wh):
    if (len(wp) == 1):
        if (wh[0] == "RF"):
            print("Player "+str(wp[0])+" wins with a royal flush.")
        if (wh[0] == "SF"):
            print("Player "+str(wp[0])+" wins with a straight flush, "+s(wh[1])+" high.")
        if (wh[0] == "QUADS"):
            print("Player "+str(wp[0])+" wins with quad "+s(wh[1])+"s with "+s(wh[2])+" kicker.")
        if (wh[0] == "FH"):
            print("Player "+str(wp[0])+" wins with a full house, "+s(wh[1])+"s full of "+s(wh[2])+"s.")
        if (wh[0] == "FLUSH"):
            print("Player "+str(wp[0])+" wins with a flush of the following cards: "+s(wh[1])+", "+s(wh[2])+", "+s(wh[3])+", "+s(wh[4])+", "+s(wh[5])+".")
        if (wh[0] == "STR"):
            print("Player "+str(wp[0])+" wins with a straight, "+s(wh[1])+" high.")
        if (wh[0] == "3OAK"):
            print("Player "+str(wp[0])+" wins with three of a kind "+s(wh[1])+"s, with "+s(wh[2])+" and "+s(wh[3])+" kicker.")
        if (wh[0] == "2P"):
            print("Player "+str(wp[0])+" wins with two pair, "+s(wh[1])+"s and "+s(wh[2])+"s with "+s(wh[3])+" kicker.")
        if (wh[0] == "1P"):
            print("Player "+str(wp[0])+" wins with a pair of "+s(wh[1])+"s, with kickers "+s(wh[2])+", "+s(wh[3])+", "+s(wh[4])+".")
        if (wh[0] == "HC"):
            print("Player "+str(wp[0])+" wins with a high card, with a board of: "+s(wh[1])+", "+s(wh[2])+", "+s(wh[3])+", "+s(wh[4])+", "+s(wh[5])+".")
    else:
        if (wh[0] == "RF"):
            print("Players "+str(wp)+" chop with a royal flush.")
        if (wh[0] == "SF"):
            print("Players "+str(wp)+" chop with a straight flush, "+s(wh[1])+" high.")
        if (wh[0] == "QUADS"):
            print("Players "+str(wp)+" chop with quad "+s(wh[1])+"s with "+s(wh[2])+" kicker.")
        if (wh[0] == "FH"):
            print("Players "+str(wp)+" chop with a full house, "+s(wh[1])+"s full of "+s(wh[2])+"s.")
        if (wh[0] == "FLUSH"):
            print("Players "+str(wp)+" chop with a flush of the following cards: "+s(wh[1])+", "+s(wh[2])+", "+s(wh[3])+", "+s(wh[4])+", "+s(wh[5])+".")
        if (wh[0] == "STR"):
            print("Players "+str(wp)+" chop with a straight, "+s(wh[1])+" high.")
        if (wh[0] == "3OAK"):
            print("Players "+str(wp)+" chop with three of a kind "+s(wh[1])+"s, with "+s(wh[2])+" and "+s(wh[3])+" kicker.")
        if (wh[0] == "2P"):
            print("Players "+str(wp)+" chop with two pair, "+s(wh[1])+"s and "+s(wh[2])+"s with "+s(wh[3])+" kicker.")
        if (wh[0] == "1P"):
            print("Players "+str(wp)+" chop with a pair of "+s(wh[1])+"s, with kickers "+s(wh[2])+", "+s(wh[3])+", "+s(wh[4])+".")
        if (wh[0] == "HC"):
            print("Players "+str(wp)+" chop with a high card, with a board of: "+s(wh[1])+", "+s(wh[2])+", "+s(wh[3])+", "+s(wh[4])+", "+s(wh[5])+".")

# def handBetter(first, second):
#     rankings = ["HC", "1P", "2P", "3OAK", "STR", "FLUSH", "FH", "QUADS", "SF", "RF"]
#     if (first not in rankings or second not in rankings):
#         return -1
#     if (rankings.index(first) < rankings.index(second)):
#         return 0
#     if (rankings.index(first) > rankings.index(second)):
#         return 1
#     if (rankings.index(first) == rankings.index(second)):
#         return 2

def handRank(hand):
    rankings = ["HC", "1P", "2P", "3OAK", "STR", "FLUSH", "FH", "QUADS", "SF", "RF"]
    return rankings.index(hand)

cards = []

for i in range(13):
  cards.append([i + 2, "s"])
  cards.append([i + 2, "h"])
  cards.append([i + 2, "d"])
  cards.append([i + 2, "c"])

#print(cards)

numPlayers = input("How many players?\n")

cardsInDeck = 52
playerHands = []
board = []
madeHands = []

for i in range(int(numPlayers)):
  print("Player " + str(i + 1) + "'s hand:")
  for j in range(2):
    card = random.randint(0, cardsInDeck - 1)
    print(s(cards[card][0]) + cards[card][1])
    playerHands.append(cards[card])
    cardsInDeck -= 1
    cards.remove(cards[card])

for i in range(int(len(playerHands) / 2)):
  continue
  #print(playerHands[2 * i], playerHands[2 * i + 1])

print("Board: ")
for i in range(5):
  card = random.randint(0, cardsInDeck - 1)
  print(s(cards[card][0]) + cards[card][1])
  board.append(cards[card])
  cardsInDeck -= 1
  cards.remove(cards[card])


for i in range(int(numPlayers)):
# for testing
  #board = [[2, "s"], [3, "s"], [4, "s"], [5, "s"], [6, "s"]]
#
  sevenCards = board.copy()
  sevenCards.append(playerHands[2 * i])
  sevenCards.append(playerHands[2 * i + 1])

  madeHands.append(["HC", 7, 5, 4, 3, 2])

  for fiveCards in list(combinations(sevenCards, 5)):
    fiveCards = sorted(fiveCards, key=lambda x : x[0])
    #print(fiveCards)

    #### ROYAL FLUSH ####
    royal = ([14, "s"] in fiveCards and [13, "s"] in fiveCards and [12, "s"] in fiveCards and [11, "s"] in fiveCards and [10, "s"] in fiveCards) or ([14, "h"] in fiveCards and [13, "h"] in fiveCards and [12, "h"] in fiveCards and [11, "h"] in fiveCards and [10, "h"] in fiveCards) or ([14, "d"] in fiveCards and [13, "d"] in fiveCards and [12, "d"] in fiveCards and [11, "d"] in fiveCards and [10, "d"] in fiveCards) or ([14, "c"] in fiveCards and [13, "c"] in fiveCards and [12, "c"] in fiveCards and [11, "c"] in fiveCards and [10, "c"] in fiveCards)
    if royal:
        madeHands[i] = ["RF"]
        break

    wheel = fiveCards[0][0] == 2 and fiveCards[1][0] == 3 and fiveCards[2][0] == 4 and fiveCards[3][0] == 5 and fiveCards[4][0] == 14
    straight = fiveCards[0][0] == fiveCards[1][0]-1 and fiveCards[1][0] == fiveCards[2][0]-1 and fiveCards[2][0] == fiveCards[3][0]-1 and fiveCards[3][0] == fiveCards[4][0]-1
    flush = fiveCards[0][1] == fiveCards[1][1] and fiveCards[1][1] == fiveCards[2][1] and fiveCards[2][1] == fiveCards[3][1] and fiveCards[3][1] == fiveCards[4][1]

    #### STRAIGHT FLUSH ####
    if (straight and flush or wheel and flush):
        currHand = ["SF", fiveCards[4][0]]
        if (wheel and flush):
            currHand = ["SF", 5]
        if (handRank(currHand[0]) > handRank(madeHands[i][0])):
            madeHands[i] = currHand
            continue
        if (handRank(currHand[0]) == handRank(madeHands[i][0])):
            if (currHand[1] > madeHands[i][1]):
                madeHands[i] = currHand
                continue
    
    # calculate card frequency (useful for quads, full house, pairs, etc.)
    cardFreqs = [0] * 13
    for card in fiveCards:
        cardFreqs[card[0] - 2]+=1

    #### QUADS ####
    if (4 in cardFreqs):
        currHand = ["QUADS", cardFreqs.index(4)+2, cardFreqs.index(1)+2]
        if (handRank(currHand[0]) > handRank(madeHands[i][0])):
            madeHands[i] = currHand
            continue
        if (handRank(currHand[0]) == handRank(madeHands[i][0])):
            if (currHand[1] > madeHands[i][1]):
                madeHands[i] = currHand
                continue
            if (currHand[1] == madeHands[i][1]):
                if (currHand[2] > madeHands[i][2]):
                    madeHands[i] = currHand
                    continue

    #### FULL HOUSE ####
    if (3 in cardFreqs and 2 in cardFreqs):
        currHand = ["FH", cardFreqs.index(3)+2, cardFreqs.index(2)+2]
        if (handRank(currHand[0]) > handRank(madeHands[i][0])):
            madeHands[i] = currHand
            continue
        if (handRank(currHand[0]) == handRank(madeHands[i][0])):
            if (currHand[1] > madeHands[i][1]):
                madeHands[i] = currHand
                continue
            if (currHand[1] == madeHands[i][1]):
                if (currHand[2] > madeHands[i][2]):
                    madeHands[i] = currHand
                    continue

    #### FLUSH ####
    if (flush):
        currHand = ["FLUSH"]
        for j in range(12, -1, -1):
            if (cardFreqs[j] == 1):
                currHand.append(j+2)
        if (handRank(currHand[0]) > handRank(madeHands[i][0])):
            madeHands[i] = currHand
            continue
        if (handRank(currHand[0]) == handRank(madeHands[i][0])):
            for k in range(5):
                if (currHand[k+1] == madeHands[i][k+1]):
                    continue
                if (currHand[k+1] >= madeHands[i][k+1]):
                    madeHands[i] = currHand
                    break
                else:
                    break
            continue

    #### STRAIGHT ####
    if (straight or wheel):
        currHand = ["STR"]
        if (wheel):
            currHand.append(5)
        else:
            currHand.append(fiveCards[4][0])
        if (handRank(currHand[0]) > handRank(madeHands[i][0])):
            madeHands[i] = currHand
            continue
        if (handRank(currHand[0]) == handRank(madeHands[i][0])):
            if (currHand[1] > madeHands[i][1]):
                madeHands[i] = currHand
                continue

    #### THREE OF A KIND ####
    if (3 in cardFreqs):
        currHand = ["3OAK", cardFreqs.index(3)+2]
        for j in range(12, -1, -1):
            if (cardFreqs[j] == 1):
                currHand.append(j+2)
        if (handRank(currHand[0]) > handRank(madeHands[i][0])):
            madeHands[i] = currHand
            continue
        if (handRank(currHand[0]) == handRank(madeHands[i][0])):
            if (currHand[1] > madeHands[i][1]):
                madeHands[i] = currHand
                continue
            if (currHand[1] == madeHands[i][1]):
                if (currHand[2] > madeHands[i][2]):
                    madeHands[i] = currHand
                    continue
                if (currHand[2] == madeHands[i][2]):
                    if (currHand[3] > madeHands[i][3]):
                        madeHands[i] = currHand
                        continue

    #### TWO PAIR ####
    if (cardFreqs.count(2) == 2):
        currHand = ["2P"]
        for j in range(12, -1, -1):
            if (cardFreqs[j] == 2):
                currHand.append(j+2)
        currHand.append(cardFreqs.index(1)+2)
        if (handRank(currHand[0]) > handRank(madeHands[i][0])):
            madeHands[i] = currHand
            continue
        if (handRank(currHand[0]) == handRank(madeHands[i][0])):
            if (currHand[1] > madeHands[i][1]):
                madeHands[i] = currHand
                continue
            if (currHand[1] == madeHands[i][1]):
                if (currHand[2] > madeHands[i][2]):
                    madeHands[i] = currHand
                    continue
                if (currHand[2] == madeHands[i][2]):
                    if (currHand[3] > madeHands[i][3]):
                        madeHands[i] = currHand
                        continue

    #### ONE PAIR ####
    if (2 in cardFreqs):
        currHand = ["1P", cardFreqs.index(2)+2]
        for j in range(12, -1, -1):
            if (cardFreqs[j] == 1):
                currHand.append(j+2)
        if (handRank(currHand[0]) > handRank(madeHands[i][0])):
            madeHands[i] = currHand
            continue
        if (handRank(currHand[0]) == handRank(madeHands[i][0])):
            for k in range(4):
                if (currHand[k+1] == madeHands[i][k+1]):
                    continue
                if (currHand[k+1] >= madeHands[i][k+1]):
                    madeHands[i] = currHand
                    break
                else:
                    break
            continue

    #### HIGH CARD ####
    currHand = ["HC"]
    for j in range(12, -1, -1):
        if (cardFreqs[j] == 1):
            currHand.append(j+2)
    if (handRank(currHand[0]) == handRank(madeHands[i][0])):
        for k in range(5):
            if (currHand[k+1] == madeHands[i][k+1]):
                continue
            if (currHand[k+1] >= madeHands[i][k+1]):
                madeHands[i] = currHand
                break
            else:
                break
        continue

#print(madeHands)

bestHand = madeHands[0]
winningPlayers = [1]

for n in range(1, len(madeHands)):
    if (handRank(bestHand[0]) < handRank(madeHands[n][0])):
        bestHand = madeHands[n]
        winningPlayers = [n+1]
        continue
    if (bestHand == madeHands[n]):
        winningPlayers.append(n+1)
        continue
    #### TIEBREAK ####
    if (handRank(bestHand[0]) == handRank(madeHands[n][0])):
        # STRAIGHT FLUSH
        if (bestHand[0] == "SF"):
            if (bestHand[1] < madeHands[n][1]):
                bestHand = madeHands[n]
                winningPlayers = [n+1]
                continue
        # QUADS
        if (bestHand[0] == "QUADS"):
            if (bestHand[1] < madeHands[n][1]):
                bestHand = madeHands[n]
                winningPlayers = [n+1]
                continue
            if (bestHand[1] == madeHands[n][1]):
                if (bestHand[2] < madeHands[n][2]):
                    bestHand = madeHands[n]
                    winningPlayers = [n+1]
                    continue
        # FULL HOUSE
        if (bestHand[0] == "FH"):
            if (bestHand[1] < madeHands[n][1]):
                bestHand = madeHands[n]
                winningPlayers = [n+1]
                continue
            if (bestHand[1] == madeHands[n][1]):
                if (bestHand[2] < madeHands[n][2]):
                    bestHand = madeHands[n]
                    winningPlayers = [n+1]
                    continue
        # FLUSH
        if (bestHand[0] == "FLUSH"):
            for k in range(5):
                if (bestHand[k+1] == madeHands[n][k+1]):
                    continue
                if (bestHand[k+1] < madeHands[n][k+1]):
                    winningPlayers = [n+1]
                    bestHand = madeHands[n]
                    break
                else:
                    break
            continue
        # STRAIGHT
        if (bestHand[0] == "STR"):
            if (bestHand[1] < madeHands[n][1]):
                bestHand = madeHands[n]
                winningPlayers = [n+1]
                continue
        # THREE OF A KIND
        if (bestHand[0] == "3OAK"):
            if (bestHand[1] < madeHands[n][1]):
                bestHand = madeHands[n]
                winningPlayers = [n+1]
                continue
            if (bestHand[1] == madeHands[n][1]):
                if (bestHand[2] < madeHands[n][2]):
                    bestHand = madeHands[n]
                    winningPlayers = [n+1]
                    continue
                if (bestHand[2] == madeHands[n][2]):
                    if (bestHand[3] < madeHands[n][3]):
                        bestHand = madeHands[n]
                        winningPlayers = [n+1]
                        continue
        # TWO PAIR
        if (bestHand[0] == "2P"):
            if (bestHand[1] < madeHands[n][1]):
                bestHand = madeHands[n]
                winningPlayers = [n+1]
                continue
            if (bestHand[1] == madeHands[n][1]):
                if (bestHand[2] < madeHands[n][2]):
                    bestHand = madeHands[n]
                    winningPlayers = [n+1]
                    continue
                if (bestHand[2] == madeHands[n][2]):
                    if (bestHand[3] < madeHands[n][3]):
                        bestHand = madeHands[n]
                        winningPlayers = [n+1]
                        continue
        # PAIR
        if (bestHand[0] == "1P"):
            for k in range(4):
                if (bestHand[k+1] == madeHands[n][k+1]):
                    continue
                if (bestHand[k+1] < madeHands[n][k+1]):
                    winningPlayers = [n+1]
                    bestHand = madeHands[n]
                    break
                else:
                    break
            continue
        # HIGH CARD
        if (bestHand[0] == "HC"):
            for k in range(5):
                if (bestHand[k+1] == madeHands[n][k+1]):
                    continue
                if (bestHand[k+1] < madeHands[n][k+1]):
                    winningPlayers = [n+1]
                    bestHand = madeHands[n]
                    break
                else:
                    break
            continue

winPrint(winningPlayers, bestHand)
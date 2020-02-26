# Poker Hand Ranking
# Quiz URL:
# 	https://edabit.com/challenge/C6pHyc4iN6BNzmhsM
# Quiz description
# 	In this challenge, you have to establish which kind of Poker combination is present in a deck of five cards. Every card is a string containing the card value (with the upper-case initial for face-cards) and the lower-case initial for suits, as in the examples below:
# 	"Ah" ➞ Ace of hearts
# 	"Ks" ➞ King of spades
# 	"3d" ➞ Three of diamonds
# 	"Qc" ➞ Queen of clubs

def poker_hand_ranking(deck):

	# Error handling
	if len(deck) != 5:
		return "Invalid input - Deck should contain exactly 5 cards"

	deck = split_deck(deck)
	flush = False
	straight = True

	cards = deck[0]
	suits = deck[1]

	if(len(set(suits)) == 1):
		flush = True

	if(len(set(cards)) == len(cards)):
		noDuplicates = True
	elif(len(set(cards)) == 2):
		for card in cards:
			if(cards.count(card) == 4):
				return "Four of a Kind"
		return "Full House"
	elif(len(set(cards)) == 3):
		for card in cards:
			if(cards.count(card) == 3):
				return "Three of a Kind"
		return "Two Pair"
	elif(len(set(cards)) == 4):
		return "Pair"


	if(noDuplicates):
		for key, card in enumerate(cards):
			if(key <= (len(cards) - 2)):
				if((int(cards[key+1]) - int(cards[key])) != 1):
					straight = False

	if straight and flush and (cards[0] == "10"):
		return "Royal Flush"
	elif straight and flush:
		return "Straight Flush"
	elif straight:
		return "Straight"
	elif flush:
		return "Flush"
	else:
		return "High Card"

# Replace letters with numbers according to dictionary below, and sort deck
# Return object with two lists, one with only numbers of the cards and another one with the suits
def split_deck(deck):

	dictionary = {
		"J" : "11",
		"Q" : "12",
		"K" : "13",
		"A" : "14",
	}
	
	sortedDeck = []
	suits = []
	objectToReturn = []
	for card in deck:
		suits.append(card[-1])
		if card[0] in dictionary:
			sortedDeck.append(dictionary[card[0]])
		elif(len(card)==2):
			sortedDeck.append("0" + card[0])
		else:
			sortedDeck.append(card[0:2])

	sortedDeck.sort(key=int)
	objectToReturn.append(sortedDeck)
	objectToReturn.append(suits)

	return objectToReturn


print(poker_hand_ranking(["10h", "Jh", "Qh", "Ah", "Kh"]))
print(poker_hand_ranking(["3h", "5h", "Qs", "9h", "Ad"]))
print(poker_hand_ranking(["10s", "10c", "8d", "10d", "10h"]))
print(poker_hand_ranking(["4h", "9s", "2s", "2d", "Ad"]))
print(poker_hand_ranking(["10s", "9s", "8s", "6s", "7s"]))
print(poker_hand_ranking(["10c", "9c", "9s", "10s", "9h"]))
print(poker_hand_ranking(["8h", "2h", "8s", "3s", "3c"]))
print(poker_hand_ranking(["Jh", "9h", "7h", "5h", "2h"]))
print(poker_hand_ranking(["Ac", "Qc", "As", "Ah", "2d"]))
print(poker_hand_ranking(["Ad", "Kd", "Qd", "Jd", "9d"]))
print(poker_hand_ranking(["10h", "Jh", "Qs", "Ks", "Ac"]))
print(poker_hand_ranking(["3h", "8h", "2s", "3s", "3d"]))
print(poker_hand_ranking(["4h", "Ac", "4s", "4d", "4c"]))
print(poker_hand_ranking(["3h", "8h", "2s", "3s", "2d"]))
print(poker_hand_ranking(["8h", "8s", "As", "Qh", "Kh"]))
print(poker_hand_ranking(["Js", "Qs", "10s", "Ks", "As"]))
print(poker_hand_ranking(["Ah", "3s", "4d", "Js", "Qd"]))

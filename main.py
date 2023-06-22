from Deck import *
from Card import *
from replit import db

def same_suit(lst):
	Same_suit = True
	for i in range(0, len(lst)-1):
		if lst[i].suit != lst[i+1].suit:
			Same_suit = False
	return Same_suit 

def best(lst):
		v = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
		best = 0
		for i in lst:
			if v.index(i.value) == 0:
				return 14
			if v.index(i.value) > best:
				best  = v.index(i.value)
		return best+1
			
	
def hand(lst):
	c = [lst[0].value == lst[1].value, lst[1].value == lst[2].value, lst[0].value == lst[2].value]
	#Straight Flush
	if lst[0].add_one() == lst[1].value and lst[1].add_one() == lst[2].value and same_suit(lst):
		return (19, lst[2].value)
	# 3 of a kind
	elif lst[0].value == lst[1].value and lst[1].value == lst[2].value:
		return (18, lst[2].value)
	# Straight
	elif lst[0].add_one() == lst[1].value and lst[1].add_one() == lst[2].value:
		return (17, lst[2].value)
	#Flush
	elif same_suit(lst):
		return (16, best(lst))
	# Pair
	
	elif lst[0].value == lst[1].value or lst[1].value == lst[2].value or lst[0].value == lst[2].value:
		for i in range(len(c)):
			if c[i]:
				return(15, lst[i].value)
	#Highest card
	else:
		return (best(lst), best(lst))
			
	
def amount_won(playerlst, dealerlst, player_balance, antewager, wager):
	can_play = False
	for card in dealerlst:
		if card.value == "Queen" or card.value == "King" or card.value == "Ace" :
			can_play = True
	if can_play == False:
		return player_balance+antewager*2+wager 
	player_hand, y = hand(playerlst)
	dealer_hand, x = hand(dealerlst)
	if player_hand > dealer_hand:
		return player_balance+(antewager+wager)*2
	elif player_hand == dealer_hand:
		if y > x:
			return player_balance+(antewager+wager)*2
		elif best(playerlst) > best(dealerlst):
			return player_balance+(antewager+wager)*2	
	return player_balance



games = 0
rounds = 1
j =1
deck = Deck(1)
Player_balance = 5000
vaild_input = False
while j > 0:
	games +=1
	print("Game:", games)
	print("Your Balance Is: ", Player_balance)
	vaild_input = False
	while vaild_input == False:
		a = int(input("Please enter ante wager: "))
		if a > 5000 or a<0 or a> int(Player_balance/2):
			print("Please bid a different amount, max bid is 5000.")
		else: 
			vaild_input = True
	Player_balance -= a
	deck.remake_deck()
	deck.shuffle_deck()
	dealer = deck.pull_3_cards()
	player = deck.pull_3_cards()
	print()
	for i in player:
		i.print_card()
	print()
	vaild_input = False
	while vaild_input == False:
		b = int(input("Place wager (-1 to fold): "))
		if b < a and b!=-1:
			print("Wager must be equal or greater than ante wager or please enter -1 to fold")
		else: 
			vaild_input = True
	if b == -1:
		play_another = input("Would you want to play another round? ")
		if play_another == "yes":
			print("_______________________________________________________________________________________________________________________________________________")
			continue
		else:
			print("Thank you for playing")
			break
	print()
	print("Dealer's Cards:")
	for i in dealer:
		i.print_card()
	print()
	Player_balance -= b
	new_ammount = amount_won(player, dealer, Player_balance, a,b)
	if new_ammount == Player_balance:
		print("You Lost")
		play_another = input("Would you want to play another round? ")
		if play_another == "yes":
			Player_balance = new_ammount
			print("_______________________________________________________________________________________________________________________________________________")
			continue
		else:
			print("Thank you for playing")
			break
	else:
		print("You won!")
		play_another = input("Would you want to play another round?(yes or no) ")
		if play_another == "yes":
			Player_balance = new_ammount
			print("_______________________________________________________________________________________________________________________________________________")
			continue
		else:
			print("Thank you for playing")
			break
		
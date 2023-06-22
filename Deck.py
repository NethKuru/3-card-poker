from Card import *
import random
class Deck():
	card_list = []
	def __init__(self, num):
		self.num = num
		for i in range(num):
			for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
				for v in ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']:
					self.card_list.append(Card(v, s))

	def shuffle_deck(self):
		self.shuffled_cards = random.shuffle(self.card_list)


	def pull_card(self):
		self.pulled_card = self.card_list.pop()
		return self.pulled_card

	def remake_deck(self):
		self.card_list = []
		for i in range(self.num):
			for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
				for v in ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']:
					self.card_list.append(Card(v, s))

	def pull_3_cards(self):
		self.lst = [self.pull_card(),self.pull_card(),self.pull_card()]
		return self.lst
		

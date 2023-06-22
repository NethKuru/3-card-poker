class Card():

	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def print_card(self):
		print(str(self.value) + " of " + str(self.suit))

	def add_one(self):
		v = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
		index = v.index(self.value)
		if v[index] == "King":
			return "Ace"
		return v[index+1]
		

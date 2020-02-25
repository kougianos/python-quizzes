# Shiritori game
# Quiz URL:
# 	https://edabit.com/challenge/dLnZLi8FjaK6qKcvv

class Shiritori:

	def __init__(self):
		self.words = []
		self.game_over = False

	def play(self, word):

		# Append word without checking when list is empty
		if(len(self.words) == 0):
			self.words.append(word)
			print(self.words)
			return

		# Check if word is in words list
		if(word in self.words):
			self.game_over = True
			print("Game over")
			return
		
		# Get last letter of last word and compare it with first letter of word
		if(self.words[-1][-1] == word[0]):
			self.words.append(word)
			print(self.words)
			return
		else:
			self.game_over = True
			print("Game over")
			return

	def restart(self):
		self.words = []
		self.game_over = False
		print("Game restarted")
		print(self.words)


s = Shiritori()

print("Shiritori game, press R to restart or Q to quit - Single letter words are not allowed!")

while(1):

	if(s.game_over):
		print("Game is over - Restart if you want to play again")

	word = input("Give word: ")

	if(word=="R"):
		s.restart()
		continue
	elif(word=="Q"):
		exit("Goodbye")

	if s.game_over == False: s.play(word)

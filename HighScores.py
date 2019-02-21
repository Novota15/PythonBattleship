'''
Grant Novota
CSCI 1300
Rec 111
'''
from datetime import datetime

class HighScores:
	def __init__(self, name = "", turns = 0):
		self.data = {}
		self.datalist = []
		self.name = name
		self.turns = turns

	def makeScore(self, filename, turns):
		self.turns = turns
		self.name = raw_input("Please Enter Your Name:")
		self.datalist = [str(self.turns), str(datetime.now())] #List of player result and time they completed the game
		self.data[self.name] = self.datalist #Assigns the players score data to a dictionary. The score data is accessed by using their name as the key

		output_file = open(filename, 'a+') #Writing the score data to a file
		output_file.write(self.name + " - " + self.data[self.name][0] + " Turns " + " - " + self.data[self.name][1] + "\n")
		output_file.close()
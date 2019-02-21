'''
Grant Novota
CSCI 1300
Rec 111
'''
import pygame
import sys
from Ship import Ship
from GameBoard import GameBoard
from HighScores import HighScores

board = GameBoard()
scores = HighScores()

def printFile(filename): #Reads each line in the file and prints it to the screen
	with open(filename, 'r') as file_input:
		for line in file_input:
			print line
	file_input.close()

def PlayGame(): 
	board.printBoard() #This prints out the board that the game will be played on
	scores.makeScore("BattleshipScores.txt", board.getTurns()) #Once the game is over, this creates the scoreboard
	printFile("BattleshipScores.txt") #Prints out the scoreboard to the screen
	exit = None
	while True: #Once the user enters 2, the program quits
		try: 
			exit = raw_input("Enter 2 To Exit\n")
			if 2 == int(exit):
				break
		except:
			continue
	sys.exit()

def initializeGame(): 
	printFile("BattleshipInstructions.txt") #Prints the instructions
	start = None
	while True: #The game will only begin once the user inputs the number 1 
		try:
			start = raw_input("Enter 1 To Begin:")
			if 1 == int(start):
				break
		except:
			continue

	PlayGame() #Starts the game

def main():
	initializeGame()

if __name__ == '__main__':
	main()